/*
 *      Hex-Rays Decompiler project
 *      Copyright (c) 2007-2008 by Hex-Rays, support@hex-rays.com
 *      ALL RIGHTS RESERVED.
 *
 *      Sample plugin for Hex-Rays Decompiler.
 *      It introduces a new command for the user: invert if-statement
 *      For example, a statement like
 *
 *      if ( cond )
 *      {
 *        statements1;
 *      }
 *      else
 *      {
 *        statements2;
 *      }
 *
 *      will be displayed as
 *
 *      if ( !cond )
 *      {
 *        statements2;
 *      }
 *      else
 *      {
 *        statements1;
 *      }
 *
 *      Please note that the plugin can not directly modify the current ctree.
 *      If the ctree is recreated, the changes will be lost.
 *      To make them persistent, we need to save information about the inverted
 *      if statements in the database and automatically reapply them
 *      for each new build. This approach makes all modifications
 *      persistent. The user can quit IDA and restart the session:
 *      his changes will be intact.
 *
 */

#include <hexrays.hpp>

// Hex-Rays API pointer
hexdsp_t *hexdsp = NULL;

static bool inited = false;

// The node to keep inverted-if information.
static const char nodename[] = "$ hexrays inverted-if";
static netnode node;

// Cached copy of inverted if-statement addresses
static eavec_t inverted_ifs;

#define ACTION_NAME "sample3:invertif"

//--------------------------------------------------------------------------
// The user has selected to invert the if statement. Update ctree
// and refresh the view.
static void do_invert_if(cinsn_t *i)
{
  QASSERT(30198, i->op == cit_if);
  cif_t &cif = *i->cif;
  // create an inverted condition and swap it with the if-condition
  cexpr_t *notcond = lnot(new cexpr_t(cif.expr));
  notcond->swap(cif.expr);
  delete notcond;
  // swap if branches
  qswap(cif.ielse, cif.ithen);
}

//--------------------------------------------------------------------------
static void add_inverted_if(ea_t ea)
{
  eavec_t::iterator p = inverted_ifs.find(ea);
  if ( p != inverted_ifs.end() ) // already present?
    inverted_ifs.erase(p);       // delete the mark
  else
    inverted_ifs.push_back(ea);  // remember if-statement address
  // immediately save data into the database
  node.setblob(&inverted_ifs[0], inverted_ifs.size()*sizeof(ea_t), 0, 'I');
  node.altset(-1, inverted_ifs.size());
}

//--------------------------------------------------------------------------
// Check if the item under the cursor is 'if' or 'else' keyword
// If yes, return pointer to the corresponding ctree item
static cinsn_t *find_if_statement(vdui_t &vu)
{
  // 'if' keyword: straightforward check
  if ( vu.item.is_citem() )
  {
    cinsn_t *i = vu.item.i;
    // we can handle only if-then-else statements, so check that the 'else'
    // clause exists
    if ( i->op == cit_if && i->cif->ielse != NULL )
      return i;
  }
  // check for 'else' line. The else lines do not correspond
  // to any ctree item. That's why we have to check for them separately.
  // we could extract the corresponding text line but this would be a bad approach
  // a line with single 'else' would not give us enough information to locate
  // the corresponding 'if'. That's why we use the line tail marks.
  // All 'else' line will have the ITP_ELSE mark
  if ( vu.tail.citype == VDI_TAIL && vu.tail.loc.itp == ITP_ELSE )
  {
    // for tail marks, we know only the corresponding ea,
    // not the pointer to if-statement
    // find it by walking the whole ctree
    struct ida_local if_finder_t : public ctree_visitor_t
    {
      ea_t ea;
      cinsn_t *found;
      if_finder_t(ea_t e) : ctree_visitor_t(CV_FAST|CV_INSNS), ea(e) {}
      int idaapi visit_insn(cinsn_t *i)
      {
        if ( i->op == cit_if && i->ea == ea )
        {
          found = i;
          return 1; // stop enumeration
        }
        return 0;
      }
    };
    if_finder_t iff(vu.tail.loc.ea);
    if ( iff.apply_to(&vu.cfunc->body, NULL) )
      return iff.found;
  }
  return NULL;
}

//--------------------------------------------------------------------------
static void convert_marked_ifs(cfunc_t *cfunc)
{
  // we walk the ctree and for each if-statement check if has to be inverted
  struct ida_local if_inverter_t : public ctree_visitor_t
  {
    if_inverter_t(void) : ctree_visitor_t(CV_FAST|CV_INSNS) {}
    int idaapi visit_insn(cinsn_t *i)
    {
      if ( i->op == cit_if && inverted_ifs.has(i->ea) )
        do_invert_if(i);
      return 0; // continue enumeration
    }
  };
  if_inverter_t ifi;
  ifi.apply_to(&cfunc->body, NULL); // go!
}

//--------------------------------------------------------------------------
// This callback handles various hexrays events.
static int idaapi callback(void *, hexrays_event_t event, va_list va)
{
  switch ( event )
  {
    case hxe_populating_popup:
      { // If the current item is an if-statement, then add the menu item
        TForm *form = va_arg(va, TForm *);
        TPopupMenu *popup = va_arg(va, TPopupMenu *);
        vdui_t &vu = *va_arg(va, vdui_t *);
        if ( find_if_statement(vu) != NULL )
          attach_action_to_popup(form, popup, ACTION_NAME);
      }
      break;

    case hxe_maturity:
      if ( !inverted_ifs.empty() )
      { // If the ctree is ready, invert marked ifs
        cfunc_t *cfunc = va_arg(va, cfunc_t *);
        ctree_maturity_t new_maturity = va_argi(va, ctree_maturity_t);
        if ( new_maturity == CMAT_FINAL ) // ctree is ready
          convert_marked_ifs(cfunc);
      }
      break;

    default:
      break;
  }
  return 0;
}

//-------------------------------------------------------------------------
struct invert_if_ah_t : public action_handler_t
{
  virtual int idaapi activate(action_activation_ctx_t *ctx)
  {
    vdui_t &vu = *get_tform_vdui(ctx->form);
    cinsn_t *i = find_if_statement(vu);
    add_inverted_if(i->ea);
    // we manually invert this if and recreate text.
    // this is faster than rebuilding ctree from scratch.
    do_invert_if(i);
    vu.refresh_ctext();
    return 1;
  }

  virtual action_state_t idaapi update(action_update_ctx_t *ctx)
  {
    vdui_t *vu = get_tform_vdui(ctx->form);
    if ( vu == NULL )
      return AST_DISABLE_FOR_FORM;
    return find_if_statement(*vu) == NULL ? AST_DISABLE : AST_ENABLE;
  }
};
static invert_if_ah_t invert_if_ah;
static const action_desc_t invert_if_action = ACTION_DESC_LITERAL(
        ACTION_NAME, "Invert if-statement", &invert_if_ah,
        NULL, NULL, -1);

//--------------------------------------------------------------------------
// Initialize the plugin.
int idaapi init(void)
{
  if ( !init_hexrays_plugin() )
    return PLUGIN_SKIP; // no decompiler
  if ( !node.create(nodename) ) // create failed -> node existed
  {
    size_t n = node.altval(-1);
    if ( n > 0 )
    { // initialize inverted-if cache from the database
      inverted_ifs.resize(n);
      n *= sizeof(ea_t);
      node.getblob(&inverted_ifs[0], &n, 0, 'I');
    }
  }
  install_hexrays_callback(callback, NULL);
  const char *hxver = get_hexrays_version();
  msg("Hex-rays version %s has been detected, %s ready to use\n", hxver, PLUGIN.wanted_name);
  register_action(invert_if_action);
  inited = true;
  return PLUGIN_KEEP;
}

//--------------------------------------------------------------------------
void idaapi term(void)
{
  if ( inited )
  {
    // clean up
    remove_hexrays_callback(callback, NULL);
    term_hexrays_plugin();
  }
}

//--------------------------------------------------------------------------
void idaapi run(int)
{
  // should not be called because of PLUGIN_HIDE
}

//--------------------------------------------------------------------------
static char comment[] = "Sample3 plugin for Hex-Rays decompiler";

//--------------------------------------------------------------------------
//
//      PLUGIN DESCRIPTION BLOCK
//
//--------------------------------------------------------------------------
plugin_t PLUGIN =
{
  IDP_INTERFACE_VERSION,
  PLUGIN_HIDE,          // plugin flags
  init,                 // initialize
  term,                 // terminate. this pointer may be NULL.
  run,                  // invoke plugin
  comment,              // long comment about the plugin
                        // it could appear in the status line
                        // or as a hint
  "",                   // multiline help about the plugin
  "Hex-Rays if-inverter", // the preferred short name of the plugin
  ""                    // the preferred hotkey to run the plugin
};
