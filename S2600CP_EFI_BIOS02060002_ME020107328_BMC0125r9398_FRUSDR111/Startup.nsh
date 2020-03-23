# FORCE_EFI_BOOT

echo -off
# +
# + ============================================================== +
#  Copyright (c) 2016, Intel Corporation.

#  This source code and any documentation accompanying it ("Material") is furnished
#  under license and may only be used or copied in accordance with the terms of that
#  license.  No license, express or implied, by estoppel or otherwise, to any
#  intellectual property rights is granted to you by disclosure or delivery of these
#  Materials.  The Materials are subject to change without notice and should not be
#  construed as a commitment by Intel Corporation to market, license, sell or support
#  any product or technology.  Unless otherwise provided for in the license under which
#  this Material is provided, the Material is provided AS IS, with no warranties of
#  any kind, express or implied, including without limitation the implied warranties
#  of fitness, merchantability, or non-infringement.  Except as expressly permitted by
#  the license for the Material, neither Intel Corporation nor its suppliers assumes
#  any responsibility for any errors or inaccuracies that may appear herein.  Except
#  as expressly permitted by the license for the Material, no part of the Material
#  may be reproduced, stored in a retrieval system, transmitted in any form, or
#  distributed by any means without the express written consent of Intel Corporation.

#  Module Name:  Startup.nsh

#  Abstract:  UEFI Script file for invoking system software updates.

# + ============================================================== +
#    Program all blocks of BIOS from capsule file 
# + ============================================================== +

@echo -off
mode 80 25
;foundimage section is simply to locate the correct drive
cls
if exist .\ipmi.efi then
 goto FOUNDIMAGE
endif
if exist fs0:\ipmi.efi then
 fs0:
 echo Found Update Packages on fs0:
 goto FOUNDIMAGE
endif
if exist fs1:\ipmi.efi then
 fs1:
 echo Found Update Packages on fs1:
 goto FOUNDIMAGE
endif
if exist fs2:\ipmi.efi then
 fs2:
 echo Found Update Packages on fs2:
 goto FOUNDIMAGE
endif
 echo "Unable to find Update Packages".  
 echo "Please mount the drive with the update package".
 echo ""
 goto END
:FOUNDIMAGE

echo ==========================================================================
echo "This utility will update the BMC firmware, system BIOS, ME firmware,"
echo "and FRU & SDR data on the following Intel products: 
echo ""
echo "      - Intel(R) Server System P4000CP"
echo "      - Intel(R) Server Board S2600CP"
echo ""
echo "Press 'Enter' to start all updates automatically or 'q' to quit."
echo ""
echo "Individual updates can be performed by running the specific .NSH "
echo "script files. (e.g. BIOS.nsh, BMC.NSH, etc...). The updates should be"
echo "performed in the following order:"
echo "  1): BMC firmware update"
echo "  2): System BIOS update"
echo "  3): Manageability Engine (ME) firmware update"
echo "  4): FRU & SDR data update"
echo ""
echo "Do NOT reboot the server during any update process. Updates that have"
echo "completed successfully will display an update completion message "
echo ==========================================================================
pause

echo ""
echo "BMC 01.25.9398 is being installed."
echo ""
FWPIAUPD -u -bin -ni -b -o -pia -nopc -if=usb BMC_i_0125r9398.bin
echo ""
echo "BMC update completed"

echo ""
echo "BIOS 02.06.0002 is being installed."
  iflash32 /u /ni R02.06.0002.cap
echo ""
echo "BIOS update completed."


echo ""
echo "ME firmware 02.01.07.328 is being installed."
  iflash32 /u /ni MEComplete_02.01.07.328.cap  
echo ""
echo "ME firmware update completed."


echo ""
echo "FRUSDR 1.11 is being installed."
frusdr -cfg master.cfg
echo ""
echo "FRUSDR update completed."
echo ""
echo ""
echo "Updates completed. Please remove the USB key and reboot using the front panel button."
echo ""

:END

