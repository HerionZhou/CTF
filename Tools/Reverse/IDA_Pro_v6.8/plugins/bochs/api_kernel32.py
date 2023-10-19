#//
#// Format: (triple slashes) func=function_name entry=entry_value purge=val retval=val

#// func
#//      specifies the function name. No need to specify the module name since
#//      it is deduced from the name of the script file. The file name has
#//      always the following format: api_modulename.idc
#//
#// entry
#//      module_name.function_name means to forward to another module
#//      idc_function_name         means to call the specified IDC function
#//                                The return value of the script controls the execution:
#//                                  - zero: means to continue execution
#//                                  - non-zero: suspend the application
#//      this attribute is optional.
#//      If it is missing, a dummy stub will be generated by IDA. The next
#//      two attributes are used by the stub generator:
#// purge
#//      How many bytes to purge from the stack. Do not specify this value
#//      if you are forwarding to another module.
#// retval
#//      The return value (this attribute is used only to generate stubs)
#//
#//

#//--------------------------------------------------------------------------
#// These are system definitions.
#// !! Do not change them unless you know what you are doing !!
#///func=GetModuleFileNameA entry=bochsys.BxGetModuleFileNameA
#///func=GetModuleFileNameW entry=bochsys.BxGetModuleFileNameW
#///func=GetModuleHandleA entry=bochsys.BxGetModuleHandleA
#///func=GetModuleHandleW entry=bochsys.BxGetModuleHandleW
#///func=GetCommandLineA entry=bochsys.BxWin32GetCommandLineA
#///func=GetCommandLineW entry=bochsys.BxWin32GetCommandLineW
#///func=LoadLibraryA entry=bochsys.BxLoadLibraryA
#///func=LoadLibraryW entry=bochsys.BxLoadLibraryW
#///func=GetEnvironmentStrings entry=bochsys.BxWin32GetEnvironmentStringsA
#///func=GetEnvironmentStringsA entry=bochsys.BxWin32GetEnvironmentStringsA
#///func=GetEnvironmentStringsW entry=bochsys.BxWin32GetEnvironmentStringsW
#///func=GetProcAddress entry=bochsys.BxGetProcAddress
#///func=ExitProcess entry=bochsys.BxExitProcess
#///func=VirtualAlloc entry=bochsys.BxVirtualAlloc
#///func=VirtualFree entry=bochsys.BxVirtualFree
#///func=VirtualProtect entry=bochsys.BxVirtualProtect
#///func=GetTickCount entry=bochsys.BxGetTickCount
#///func=GetLastError entry=ntdll.RtlGetLastWin32Error
#///func=SetLastError entry=ntdll.RtlSetLastWin32Error
#///func=TlsAlloc entry=bochsys.BxWin32TlsAlloc
#///func=TlsFree entry=bochsys.BxWin32TlsFree
#///func=TlsGetValue entry=bochsys.BxWin32TlsGetValue
#///func=TlsSetValue entry=bochsys.BxWin32TlsSetValue
#///func=FlsAlloc entry=bochsys.BxWin32FlsAlloc
#///func=FlsFree entry=bochsys.BxWin32TlsFree
#///func=FlsGetValue entry=bochsys.BxWin32TlsGetValue
#///func=FlsSetValue entry=bochsys.BxWin32TlsSetValue
#///func=HeapCreate retval=1
#///func=HeapFree retval=1 purge=12
#///func=InitializeCriticalSectionAndSpinCount retval=1
#///func=lstrcpyA entry=bochsys.BxStrCpyA
#///func=lstrcpyW entry=bochsys.BxStrCpyW
#///func=lstrcatA entry=bochsys.BxStrCatA
#///func=lstrcatW entry=bochsys.BxStrCatW

#// example: user dll implementation: func=GetCommandLineA entry=mydll.MyGetCommandLineA purge=0

# HMODULE WINAPI LoadLibraryExA(LPCSTR lpFileName, HANDLE hFile, DWORD dwFlags);
#///func=LoadLibraryExA entry=k32_LoadLibraryExA
def k32_LoadLibraryExA():
  hFile = BochsGetParam(2)
  if hFile != 0:
    cpu.eax = 0
    return 0
  lpFileName = GetString(BochsGetParam(1), -1, ASCSTR_C)
  dwFlags    = BochsGetParam(3)
  # Since Bochs plugin does not support dynamic DLL loading, we simply return the module handle.
  # (the DLL must be declared in startup.idc so it is pre-loaded)
  cpu.eax = BochsGetModuleHandle(lpFileName)
  return 0 # continue execution

#///func=WideCharToMultiByte entry=k32_WideCharToMultiByte
def k32_WideCharToMultiByte():
  len_wide  = BochsGetParam(4)
  len_multi = BochsGetParam(6) #  int cbMultiByte,
  if len_wide == 0:
    cpu.eax = 0
    return 0

  if len_multi == 0:
    len = 0
  elif len_wide == -1 or len_wide > len_multi:
    len = len_multi
  else:
    len = len_wide

  p_wide    = BochsGetParam(3) # LPCWSTR lpWideCharStr
  p_multi   = BochsGetParam(5) # LPSTR lpMultiByteStr

  i=0
  if len == 0:
    while True:
      if Byte(p_wide) == 0:
        break;
      p_wide += 2
      i+=1
  else:
    while i<len:
      BochsPatchDbgDword(p_multi, Byte(p_wide))
      p_wide  += 2
      p_multi += 1
      i += 1
  cpu.eax = i
  return 0

#///func=Beep entry=beep purge=8
def beep():
  param1 = BochsGetParam(1)
  param2 = BochsGetParam(2)

  Message("I am Beep(%d, %d)\n" % (param1, param2) )

  # The emulated function returns 1:
  SetRegValue(1, "EAX")

  # Our return value controls execution of the debugged application:
  #   1 = suspend execution (inside IDACALL)
  #   0 = continue transparently
  return 0

#///func=GlobalAlloc entry=k32_GlobalAlloc purge=8
def k32_GlobalAlloc():
  # Redirect GlobalAlloc -> VirtualAlloc
  SetRegValue(BochsVirtAlloc(0, BochsGetParam(2), 1), "EAX")
  return 0

#///func=GlobalFree entry=k32_GlobalFree purge=4
def k32_GlobalFree():
  # Redirect GlobalFree -> VirtualFree
  SetRegValue(BochsVirtFree(BochsGetParam(1), 0), "EAX")
  return 0

#///func=GetCurrentThread entry=k32_GetCurrentThread purge=0
def k32_GetCurrentThread():
  SetRegValue(-2, "EAX")
  return 0

STD_INPUT_HANDLE  = 0xFFFFFFF6
STD_OUTPUT_HANDLE = 0xFFFFFFF5
STD_ERROR_HANDLE  = 0xFFFFFFF4

# BOOL WINAPI WriteFile(HANDLE hFile,LPCVOID lpBuffer,DWORD nNumberOfBytesToWrite,LPDWORD lpNumberOfBytesWritten,LPOVERLAPPED lpOverlapped);
#///func=WriteFile entry=k32_writefile
def k32_writefile():
  hfile = BochsGetParam(1);
  ea   = BochsGetParam(2);
  len   = BochsGetParam(3);

  if hfile == STD_OUTPUT_HANDLE or hfile == STD_ERROR_HANDLE:
    print "WriteFile(STDOUT): %s\n" % GetString(ea, len, ASCSTR_C)
  else:
    of = idaapi.fopenM("writefile.bin")
    pos = idaapi.qfsize(of)
    if of:
      retval = idaapi.base2file(of, pos, ea, ea+len)
      print "fp=%X, written %d bytes"%(hfile, len)
      idaapi.eclose(of)

  buf = BochsGetParam(4)
  if buf:
    BochsPatchDbgDword(Dword(buf), len) # save the number of bytes written
  cpu.eax = 1 # success
  return 0

#///func=GetCurrentThreadId entry=k32_GetCurrentThreadId
def k32_GetCurrentThreadId():
  cpu.eax = GetCurrentThreadId()
  return 0

#///func=GetStdHandle entry=k32_GetStdHandle
def k32_GetStdHandle():
  # return same value
  h = BochsGetParam(1)
  print "GetStdHandle(%08X)"%h
  cpu.eax = h
  return 0

#///func=GlobalMemoryStatus entry=k32_GlobalMemoryStatus
def k32_GlobalMemoryStatus():
  """
  00000000 MEMORYSTATUS    struc
  00000000 dwLength        dd
  00000004 dwMemoryLoad    dd
  00000008 dwTotalPhys     dd
  0000000C dwAvailPhys     dd
  00000010 dwTotalPageFile dd
  00000014 dwAvailPageFile dd
  00000018 dwTotalVirtual  dd
  0000001C dwAvailVirtual  dd
  00000020 MEMORYSTATUS    ends
  """

  ms = BochsGetParam(1)
  avail = BochsGetFreeMem()
  total = BochsGetMaxMem()

  BochsPatchDbgDword(ms + 0x08, total) # total phys
  BochsPatchDbgDword(ms + 0x0C, avail) # avail phys
  BochsPatchDbgDword(ms + 0x10, 0    ) # total page
  BochsPatchDbgDword(ms + 0x14, 0    ) # avail page
  BochsPatchDbgDword(ms + 0x18, total) # total virt
  BochsPatchDbgDword(ms + 0x1C, avail) # avail virt

  return 0
