/*
 *      Hex-Rays Decompiler project
 *      Copyright (c) 2007-2008 by Hex-Rays, support@hex-rays.com
 *      ALL RIGHTS RESERVED.
 *
 *      Sample plugin for Hex-Rays Decompiler.
 *      It dumps all user-defined information about the current
 *      function to the messages window. Namely, it displays:
 *        - user defined label names
 *        - user defined indented comments
 *        - user defined number formats
 *        - user defined local variable names, types, comments
 *
 */

#include <hexrays.hpp>

// Hex-Rays API pointer
hexdsp_t *hexdsp = NULL;

//--------------------------------------------------------------------------
// Initialize the plugin.
int idaapi init(void)
{
  if ( !init_hexrays_plugin() )
    return PLUGIN_SKIP; // no decompiler
  const char *hxver = get_hexrays_version();
  msg("Hex-rays version %s has been detected, %s ready to use\n", hxver, PLUGIN.wanted_name);
  return PLUGIN_KEEP;
}

//--------------------------------------------------------------------------
void idaapi term(void)
{
  term_hexrays_plugin();
}

//--------------------------------------------------------------------------
void idaapi run(int)
{
  func_t *pfn = get_func(get_screen_ea());
  if ( pfn == NULL )
  {
    warning("AUTOHIDE NONE\nPlease move the cursor into a function");
    return;
  }
  ea_t entry_ea = pfn->startEA;
  msg("Dump of user-defined information for function at %a\n", entry_ea);

  // Display user defined labels.
  user_labels_t *labels = restore_user_labels(entry_ea);
  if ( labels != NULL )
  {
    msg("------- %" FMT_Z " user defined labels\n", user_labels_size(labels));
    user_labels_iterator_t p;
    for ( p=user_labels_begin(labels);
          p != user_labels_end(labels);
          p=user_labels_next(p) )
    {
      int org_label = user_labels_first(p);
      qstring &name = user_labels_second(p);
      msg("Label %d: %s\n", org_label, name.c_str());
    }
    user_labels_free(labels);
  }

  // Display user defined comments
  user_cmts_t *cmts = restore_user_cmts(entry_ea);
  if ( cmts != NULL )
  {
    msg("------- %" FMT_Z " user defined comments\n", user_cmts_size(cmts));
    user_cmts_iterator_t p;
    for ( p=user_cmts_begin(cmts);
          p != user_cmts_end(cmts);
          p=user_cmts_next(p) )
    {
      const treeloc_t &tl = user_cmts_first(p);
      citem_cmt_t &cmt = user_cmts_second(p);
      msg("Comment at %a, preciser %x:\n%s\n\n", tl.ea, tl.itp, cmt.c_str());
    }
    user_cmts_free(cmts);
  }

  // Display user defined citem iflags
  user_iflags_t *iflags = restore_user_iflags(entry_ea);
  if ( iflags != NULL )
  {
    msg("------- %" FMT_Z " user defined citem iflags\n", user_iflags_size(iflags));
    user_iflags_iterator_t p;
    for ( p=user_iflags_begin(iflags);
          p != user_iflags_end(iflags);
          p=user_iflags_next(p) )
    {
      const citem_locator_t &cl = user_iflags_first(p);
      int f = user_iflags_second(p);
      msg("%a(%d): %08X", cl.ea, cl.op, f);
      if ( f & CIT_COLLAPSED )
        msg(" CIT_COLLAPSED");
      msg("\n");
    }
    user_iflags_free(iflags);
  }

  // Display user defined number formats
  user_numforms_t *numforms = restore_user_numforms(entry_ea);
  if ( numforms != NULL )
  {
    msg("------- %" FMT_Z " user defined number formats\n", user_numforms_size(numforms));
    user_numforms_iterator_t p;
    for ( p=user_numforms_begin(numforms);
          p != user_numforms_end(numforms);
          p=user_numforms_next(p) )
    {
      const operand_locator_t &ol = user_numforms_first(p);
      number_format_t &nf = user_numforms_second(p);
      msg("Number format at %a, operand %d: %s",
          ol.ea, ol.opnum, (nf.props & NF_NEGATE) != 0 ? "negated " : "");
      if ( nf.isEnum() )
      {
        msg("enum %s (serial %d)\n", nf.type_name.c_str(), nf.serial);
      }
      else if ( nf.isChar() )
      {
        msg("char\n");
      }
      else if ( nf.isStroff() )
      {
        msg("struct offset %s\n", nf.type_name.c_str());
      }
      else
      {
        msg("number base=%d\n", getRadix(nf.flags, ol.opnum));
      }
    }
    user_numforms_free(numforms);
  }

  // Display user-defined local variable information
  // First defined the visitor class
  struct ida_local dump_lvar_info_t : public user_lvar_visitor_t
  {
    bool displayed_header;
    dump_lvar_info_t(void) : displayed_header(false) {}
    int idaapi get_info_qty_for_saving(void) { return 0; }
    bool idaapi get_info_for_saving(lvar_saved_info_t *) { return false; }
    int idaapi handle_retrieved_info(const lvar_saved_info_t &lv)
    {
      if ( !displayed_header )
      {
        displayed_header = true;
        msg("------- User defined local variable information\n");
      }
      msg("Lvar defined at %a ", lv.ll.defea);
      char buf[MAXSTR];
      const vdloc_t &vdloc = lv.ll.location;
      // we do not have the width info handy, so try 1 and sizeof(int)
      // this is not quite correct, but we just need to print something
      if ( print_vdloc(buf, sizeof(buf), vdloc, 1) == 0
        && print_vdloc(buf, sizeof(buf), vdloc, inf.cc.size_i) == 0 )
      {
        buf[0] = '?';
        buf[1] = '\0';
      }
      msg("%s", buf);
      if ( !lv.name.empty() )
        msg("  Name: %s\n", lv.name.c_str());
      if ( !lv.type.empty() )
      {
        qstring out;
        lv.type.print(&out);
        msg("  Type: %s\n", out.c_str());
      }
      if ( !lv.cmt.empty() )
        msg("  Comment: %s\n", lv.cmt.c_str());
      return 0;
    }
    int idaapi handle_retrieved_mapping(lvar_mapping_t &) { return 0; }
    const lvar_mapping_t *idaapi get_info_mapping_for_saving(void) { return NULL; }
  };

  // Now iterate over all user definitions
  dump_lvar_info_t dli;
  restore_user_lvar_settings(entry_ea, dli);
}

//--------------------------------------------------------------------------
static char comment[] = "Sample plugin4 for Hex-Rays decompiler";

//--------------------------------------------------------------------------
//
//      PLUGIN DESCRIPTION BLOCK
//
//--------------------------------------------------------------------------
plugin_t PLUGIN =
{
  IDP_INTERFACE_VERSION,
  0,                    // plugin flags
  init,                 // initialize
  term,                 // terminate. this pointer may be NULL.
  run,                  // invoke plugin
  comment,              // long comment about the plugin
                        // it could appear in the status line or as a hint
  "",                   // multiline help about the plugin
  "Hex-Rays Dump User Info", // the preferred short name of the plugin
  ""                    // the preferred hotkey to run the plugin
};
