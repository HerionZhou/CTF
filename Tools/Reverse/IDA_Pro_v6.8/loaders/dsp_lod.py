# Loader for Motorola DSP ASCII object module format (.LOD)
# source: MOTOROLA DSP SIMULATOR REFERENCE MANUAL
# Copyright (c) 2011 Hex-Rays
# ALL RIGHTS RESERVED.

import idaapi
from idc import *
import struct
import string

FormatName = "Motorola DSP56000 .LOD"

# -----------------------------------------------------------------------
def gets(li):
    s = ""
    while True:
        if len(s) > 10240:
            return None     # too long strings indicate failure
        c = li.get_char()
        if c == None or c == '\n':
            break
        s += c
    if s == "" and c != '\n':
        return None
    return s

# -----------------------------------------------------------------------
def ishex(s):
    for c in s:
       if not c in string.hexdigits: return False
    return True

# -----------------------------------------------------------------------
def accept_file(li, n):
    """
    Check if the file is of supported format

    @param li: a file-like object which can be used to access the input data
    @param n : format number. The function will be called with incrementing 
               number until it returns zero
    @return: 0 - no more supported formats
             string "name" - format name to display in the chooser dialog
             dictionary { 'format': "name", 'options': integer }
               options: should be 1, possibly ORed with ACCEPT_FIRST (0x8000)
               to indicate preferred format
    """

    # we support only one format per file
    if n > 0:
        return 0

    while True:
        s = gets(li)
        if s == None:
            break
        s = s.strip()
        if len(s) == 0 or s.startswith("#") or s.startswith(".*: ") or s.startswith(" "):
            continue
        # _START DGE 0000 0000 0000 DSP56000 3.1
        # _DATA X 000000
        if (s.startswith("_START ") and s.find("DSP56") != -1) or s.startswith("_DATA "):
            idaapi.set_processor_type("dsp56k", SETPROC_ALL)
            return FormatName
        else:
            break

    # unrecognized format
    return 0

# -----------------------------------------------------------------------
def byte_size(mem_type):
    if mem_type == 'P':
      # program = code
      #nbits = idaapi.cvar.ph.cnbits
      nbits = 24
    else:
      # data
      #nbits = idaapi.cvar.ph.dnbits
      nbits = 24
    return (nbits+7) // 8

# ----------------------------------------------------------------------
def AdditionalSegment(size, offset, name):
  s = idaapi.segment_t()
  step = 0x1000000-1
  s.startEA = idaapi.freechunk(0x1000000, size, step)
  s.endEA   = s.startEA + size
  s.sel     = idaapi.setup_selector((s.startEA-offset) >> 4)
  s.type    = idaapi.SEG_DATA
  if byte_size('X') > 2:
    s.bitness = 1
  else:
    s.bitness = 0
  idaapi.add_segm_ex(s, name, "DATA", idaapi.ADDSEG_NOSREG|idaapi.ADDSEG_OR_DIE)
  return s.startEA - offset

# -----------------------------------------------------------------------
# parse a list of three-byte hex numbers
def make_chunk(words, mem_type):
    s = ""
    bs = byte_size(mem_type)
    for w in words:
      if not ishex(w):
        idaapi.error("Not a hex number: %s" % w)
      num = int(w, 16)
      # use little-endian byte order
      s += chr((num) & 0xFF)
      if bs > 1:
        s += chr((num>>8) & 0xFF)
      if bs > 2:
        s += chr((num>>16) & 0xFF)
      if bs > 3:
        s += chr((num>>24) & 0xFF)
    return s

# -----------------------------------------------------------------------
class MemChunk:
    def __init__(self, start_ea, chunk, mem_type):
        self.start_ea = start_ea
        self.chunk = chunk
        self.mem_type = mem_type
        bs = byte_size(mem_type)
        nbytes = len(chunk) // bs
        self.end_ea = start_ea + nbytes

    def load_to_idb(self, seg_start):
        load_ea = seg_start + self.start_ea
        print "%08X: loading %04X bytes of %s memory" % (load_ea, self.end_ea - self.start_ea, self.mem_type)
        idaapi.put_many_bytes(load_ea, self.chunk)

# -----------------------------------------------------------------------
def add_seg(start_ea, end_ea, name, cls, use32, align, comb):
    s = idaapi.segment_t()
    s.startEA     = start_ea
    s.endEA       = end_ea
    s.sel         = idaapi.setup_selector(0)
    s.bitness     = use32
    s.align       = align
    s.comb        = comb
    return idaapi.add_segm_ex(s, name, cls, idaapi.ADDSEG_NOSREG|idaapi.ADDSEG_OR_DIE)
    
# -----------------------------------------------------------------------
xmemsize = 0x10000
ymemsize = 0x10000

# -----------------------------------------------------------------------
class ChunkList:
    def __init__(self):
      self.chunklist = []
      self.memtypes = set()

    def add_chunk(self, start_ea, chunk, mem_type):
      if len(chunk):
        c = MemChunk(start_ea, chunk, mem_type)
        self.chunklist.append(c)
        self.memtypes.add(mem_type)

    def load_to_idb(self):
      if 'X' in self.memtypes:
        xstart = AdditionalSegment(xmemsize, 0, "XMEM");
      else:
        xstart = BADADDR
      if 'Y' in self.memtypes:
        ystart = AdditionalSegment(ymemsize, 0, "YMEM");
      else:
        ystart = BADADDR
      memmap = {'P': 0, 'X': xstart, 'Y': ystart }
      minprog = BADADDR
      maxprog = 0
      for c in self.chunklist:
        if c.mem_type == 'P':
          if c.start_ea < minprog:
              minprog = c.start_ea
          if c.end_ea > maxprog:
              maxprog = c.end_ea
      add_seg(minprog, maxprog, "ROM", "CODE", 1, idaapi.saRelByte, idaapi.scPub)
      for c in self.chunklist:
          c.load_to_idb(memmap[c.mem_type])

# -----------------------------------------------------------------------
def load_file(li, neflags, format):
    
    """
    Load the file into database

    @param li: a file-like object which can be used to access the input data
    @param neflags: options selected by the user, see loader.hpp
    @return: 0-failure, 1-ok
    """
    
    if format == FormatName:
        idaapi.set_processor_type("dsp56k", SETPROC_ALL|SETPROC_FATAL)
        li.seek(0)
        s = gets(li)
        minprog = BADADDR
        maxprog = 0
        start_addr = 0
        chunk = ""
        clist = ChunkList()
        while True:
            if s == None:
                break
            s = s.strip()
            if len(s) == 0 or s.startswith(" "):
                s = gets(li)
                continue
            words = s.split()
            if s.startswith("_START "):
                # skip
                s = gets(li)
                continue
            elif s.startswith("_DATA"):
                #_DATA <Memory space> <Address> <Code/data> ...
                if len(words) < 3:
                    idaapi.error("Bad _DATA record: %s" % s)
                # we handle only P (program) memory
                if not words[1] in ('P', 'X', 'Y'):
                    idaapi.error("Unhandled _DATA memory space: %s" % words[1])
                if not ishex(words[2]):
                    idaapi.error("Bad _DATA starting address: %s" % words[2])

                if len(chunk):
                  # append current chunk to the list
                  clist.add_chunk(start_addr, chunk, cur_mem)

                # start a new chunk
                cur_mem = words[1]
                start_addr = int(words[2], 16)
                chunk = make_chunk(words[3:], cur_mem)

                s = gets(li)
                continue
            elif s.startswith("_END"):
                if len(words) < 2 or not ishex(words[1]):
                    idaapi.error("Bad _END record: %s" % s)
                
                # append current chunk to the list
                clist.add_chunk(start_addr, chunk, cur_mem)

                # load all
                clist.load_to_idb()

                # add the entrypoint
                entry_ea = int(words[1], 16)
                idaapi.add_entry(entry_ea, entry_ea, "start", 1)
                break
            elif s.startswith("_"):
                idaapi.error("Unhandled record type: %s" % words[0])

            # we're inside a _DATA record
            chunk += make_chunk(words, cur_mem)
            s = gets(li)

        print "Load OK"
        return 1

    Warning("Unknown format name: '%s'" % format)
    return 0

# -----------------------------------------------------------------------
def move_segm(frm, to, sz, fileformatname):
    Warning("move_segm(from=%s, to=%s, sz=%d, formatname=%s" % (hex(frm), hex(to), sz, fileformatname))
    return 0
