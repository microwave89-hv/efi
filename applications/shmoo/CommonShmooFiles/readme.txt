iShmoo DDR Release v24 03/03/2009

Xiaohe Chen, Matt Herndon

Copyright @ 2008 Apple, Inc.

* Tyical DDR memory shmoo includes inbound/outbound data/vref eye in partition 0 and 1
* The DDR test will take up to 6 hours in standard mode, 1.5 hour in coarse mode and 15 minutes in fast mode.
* FSB shmoo will take about 4 hours
* The needed files include boot.efi, Register.cfg, Setup.cfg startup.nsh and iShmoo.efi.
* Register.cfg contains the register information.
* Setup.cfg specifies the test configuration.
* The output file(s) will be saved as status***.dat and shmoo*.csv, in the same directory with iShmoo.efi.


1. To manually execute the program, copy all necessary files to the root of a USB drive, or hard drive partition (Important: Volume has to be FAT formatted).
2. Root user under OSX double clicks run_shmoo app, system will automatically boot into EFI.
3. None-root user should restart the system, hold down the ALT key and select EFI boot.
4. The program will set the boot path to the location it resides, so restarts during testing will return to the test code.
5. After the test is finished, it will hand the boot path back to the default OSX partition.
