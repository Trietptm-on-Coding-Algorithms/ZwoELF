#!/usr/bin/python

# written by sqall
# twitter: https://twitter.com/sqall01
# blog: http://blog.h4des.org
# github: https://github.com/sqall01
# 
# Licensed under the GNU Public License, version 2.

from ctypes import c_uint
from ZwoELF import ElfParser


x86File = "simple"
elfFile = ElfParser(x86File)
jmpRelEntry = elfFile.getJmpRelEntryByName("printf")
jmpRelEntry.symbol.ElfN_Sym.st_value = 0x41414141
elfFile.writeElf("modified_simple")