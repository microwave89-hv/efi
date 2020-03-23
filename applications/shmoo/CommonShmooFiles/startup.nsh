###############################################################################
# Apple Confidential : Need to know
# 	All the file in this directory is for internal team use
# 	For INDY release, uncomment reset line to allow system reboot back to OSX
###############################################################################
for %x in 0 1 2 3 4 5 6 7 8 9
ls fs%x:\iShmoo.efi
if %lasterror% == 0 then
fs%x:
goto Done
endif
endfor
:Done

smbiosview -t 17 > Smbios.out
smbiosview -t 130 > SPD.out
ver > version.out
iShmoo
#set AppleOS:ResetNVRam yes
reset