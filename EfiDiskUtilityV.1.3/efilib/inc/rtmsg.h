/*++ BUILD Version: 0001    // Increment this if a change has global effects

Copyright (c) 1990-1999  Microsoft Corporation

Module Name:

    rtmsg.h

Abstract:

    This file contains the message definitions for the Win32 utilities
    library.

Revision History:

--*/
//----------------------
//
// DOS 5 chkdsk message.
//
//----------------------
//
//  Values are 32 bit values layed out as follows:
//
//   3 3 2 2 2 2 2 2 2 2 2 2 1 1 1 1 1 1 1 1 1 1
//   1 0 9 8 7 6 5 4 3 2 1 0 9 8 7 6 5 4 3 2 1 0 9 8 7 6 5 4 3 2 1 0
//  +---+-+-+-----------------------+-------------------------------+
//  |Sev|C|R|     Facility          |               Code            |
//  +---+-+-+-----------------------+-------------------------------+
//
//  where
//
//      Sev - is the severity code
//
//          00 - Success
//          01 - Informational
//          10 - Warning
//          11 - Error
//
//      C - is the Customer code flag
//
//      R - is a reserved bit
//
//      Facility - is the facility code
//
//      Code - is the facility's status code
//
//
// Define the facility codes
//


//
// Define the severity codes
//


//
// MessageId: MSG_CONVERT_LOST_CHAINS
//
// MessageText:
//
//  Convert lost chains to files (Y/N)? %0
//
#define MSG_CONVERT_LOST_CHAINS          0x000003E8L

//
// MessageId: MSG_CHK_ERROR_IN_DIR
//
// MessageText:
//
//  Unrecoverable error in folder %1.
//
#define MSG_CHK_ERROR_IN_DIR             0x000003E9L

//
// MessageId: MSG_CHK_CONVERT_DIR_TO_FILE
//
// MessageText:
//
//  Convert folder to file (Y/N)? %0
//
#define MSG_CHK_CONVERT_DIR_TO_FILE      0x000003EAL

//
// MessageId: MSG_TOTAL_DISK_SPACE
//
// MessageText:
//
//  
//  %1 bytes total disk space.
//
#define MSG_TOTAL_DISK_SPACE             0x000003EBL

//
// MessageId: MSG_BAD_SECTORS
//
// MessageText:
//
//  %1 bytes in bad sectors.
//
#define MSG_BAD_SECTORS                  0x000003ECL

//
// MessageId: MSG_HIDDEN_FILES
//
// MessageText:
//
//  %1 bytes in %2 hidden files.
//
#define MSG_HIDDEN_FILES                 0x000003EDL

//
// MessageId: MSG_DIRECTORIES
//
// MessageText:
//
//  %1 bytes in %2 folders.
//
#define MSG_DIRECTORIES                  0x000003EEL

//
// MessageId: MSG_USER_FILES
//
// MessageText:
//
//  %1 bytes in %2 files.
//
#define MSG_USER_FILES                   0x000003EFL

//
// MessageId: MSG_RECOVERED_FILES
//
// MessageText:
//
//  %1 bytes in %2 recovered files.
//
#define MSG_RECOVERED_FILES              0x000003F0L

//
// MessageId: MSG_WOULD_BE_RECOVERED_FILES
//
// MessageText:
//
//  %1 bytes in %2 recoverable files.
//
#define MSG_WOULD_BE_RECOVERED_FILES     0x000003F1L

//
// MessageId: MSG_AVAILABLE_DISK_SPACE
//
// MessageText:
//
//  %1 bytes available on disk.
//
#define MSG_AVAILABLE_DISK_SPACE         0x000003F2L

//
// MessageId: MSG_TOTAL_MEMORY
//
// MessageText:
//
//  %1 total bytes memory.
//
#define MSG_TOTAL_MEMORY                 0x000003F3L

//
// MessageId: MSG_AVAILABLE_MEMORY
//
// MessageText:
//
//  %1 bytes free.
//
#define MSG_AVAILABLE_MEMORY             0x000003F4L

//
// MessageId: MSG_CHK_CANT_NETWORK
//
// MessageText:
//
//  Windows cannot check a disk attached through a network.
//
#define MSG_CHK_CANT_NETWORK             0x000003F5L

//
// MessageId: MSG_1014
//
// MessageText:
//
//  Windows cannot check a disk that is substituted or
//  assigned using the SUBST or ASSIGN command.
//
#define MSG_1014                         0x000003F6L

//
// MessageId: MSG_PROBABLE_NON_DOS_DISK
//
// MessageText:
//
//  The specified disk appears to be a non-Windows 2000 disk.
//  Do you want to continue? (Y/N) %0
//
#define MSG_PROBABLE_NON_DOS_DISK        0x000003F7L

//
// MessageId: MSG_DISK_ERROR_READING_FAT
//
// MessageText:
//
//  An error occurred while reading the file allocation table (FAT %1).
//
#define MSG_DISK_ERROR_READING_FAT       0x000003F8L

//
// MessageId: MSG_DIRECTORY
//
// MessageText:
//
//  Folder %1.
//
#define MSG_DIRECTORY                    0x000003F9L

//
// MessageId: MSG_CONTIGUITY_REPORT
//
// MessageText:
//
//  %1 contains %2 non-contiguous blocks.
//
#define MSG_CONTIGUITY_REPORT            0x000003FAL

//
// MessageId: MSG_ALL_FILES_CONTIGUOUS
//
// MessageText:
//
//  All specified files are contiguous.
//
#define MSG_ALL_FILES_CONTIGUOUS         0x000003FBL

//
// MessageId: MSG_CORRECTIONS_WILL_NOT_BE_WRITTEN
//
// MessageText:
//
//  Windows found errors on the disk, but will not fix them
//  because disk checking was run without the /F (fix) parameter.
//
#define MSG_CORRECTIONS_WILL_NOT_BE_WRITTEN 0x000003FCL

//
// MessageId: MSG_BAD_FAT_DRIVE
//
// MessageText:
//
//     The file allocation table (FAT) on disk %1 is corrupted.
//
#define MSG_BAD_FAT_DRIVE                0x000003FDL

//
// MessageId: MSG_BAD_FIRST_UNIT
//
// MessageText:
//
//  %1  first allocation unit is not valid. The entry will be truncated.
//
#define MSG_BAD_FIRST_UNIT               0x000003FEL

//
// MessageId: MSG_CHK_DONE_CHECKING
//
// MessageText:
//
//  File and folder verification is complete.
//
#define MSG_CHK_DONE_CHECKING            0x000003FFL

//
// MessageId: MSG_DISK_TOO_LARGE_TO_CONVERT
//
// MessageText:
//
//  The volume is too large to convert.
//
#define MSG_DISK_TOO_LARGE_TO_CONVERT    0x00000400L

//
// MessageId: MSG_CONV_NTFS_CHKDSK
//
// MessageText:
//
//  The volume may have inconsistencies. Run Chkdsk, the disk checking utility.
//
#define MSG_CONV_NTFS_CHKDSK             0x00000401L

//
// MessageId: MSG_1028
//
// MessageText:
//
//     An allocation error occurred. The file size will be adjusted.
//
#define MSG_1028                         0x00000404L

//
// MessageId: MSG_1029
//
// MessageText:
//
//     Cannot recover .. entry, processing continued.
//
#define MSG_1029                         0x00000405L

//
// MessageId: MSG_1030
//
// MessageText:
//
//     Folder is totally empty, no . or ..
//
#define MSG_1030                         0x00000406L

//
// MessageId: MSG_1031
//
// MessageText:
//
//     Folder is joined.
//
#define MSG_1031                         0x00000407L

//
// MessageId: MSG_1032
//
// MessageText:
//
//     Cannot recover .. entry.
//
#define MSG_1032                         0x00000408L

//
// MessageId: MSG_BAD_LINK
//
// MessageText:
//
//  The %1 entry contains a nonvalid link.
//
#define MSG_BAD_LINK                     0x00000409L

//
// MessageId: MSG_BAD_ATTRIBUTE
//
// MessageText:
//
//     Windows has found an entry that contains a nonvalid attribute.
//
#define MSG_BAD_ATTRIBUTE                0x0000040AL

//
// MessageId: MSG_BAD_FILE_SIZE
//
// MessageText:
//
//  The size of the %1 entry is not valid.
//
#define MSG_BAD_FILE_SIZE                0x0000040BL

//
// MessageId: MSG_CROSS_LINK
//
// MessageText:
//
//  %1 is cross-linked on allocation unit %2.
//
#define MSG_CROSS_LINK                   0x0000040CL

//
// MessageId: MSG_1037
//
// MessageText:
//
//     Windows cannot find the %1 folder.
//     Disk check cannot continue past this point in the folder structure.
//
#define MSG_1037                         0x0000040DL

//
// MessageId: MSG_1038
//
// MessageText:
//
//     The folder structure past this point cannot be processed.
//
#define MSG_1038                         0x0000040EL

//
// MessageId: MSG_BYTES_FREED
//
// MessageText:
//
//  %1 bytes of free disk space added.
//
#define MSG_BYTES_FREED                  0x0000040FL

//
// MessageId: MSG_BYTES_WOULD_BE_FREED
//
// MessageText:
//
//  %1 bytes of free disk space would be added.
//
#define MSG_BYTES_WOULD_BE_FREED         0x00000410L

//
// MessageId: MSG_VOLUME_LABEL_AND_DATE
//
// MessageText:
//
//  Volume %1 created %2 %3
//
#define MSG_VOLUME_LABEL_AND_DATE        0x00000411L

//
// MessageId: MSG_TOTAL_ALLOCATION_UNITS
//
// MessageText:
//
//  %1 total allocation units on disk.
//
#define MSG_TOTAL_ALLOCATION_UNITS       0x00000412L

//
// MessageId: MSG_BYTES_PER_ALLOCATION_UNIT
//
// MessageText:
//
//  %1 bytes in each allocation unit.
//
#define MSG_BYTES_PER_ALLOCATION_UNIT    0x00000413L

//
// MessageId: MSG_1044
//
// MessageText:
//
//  Disk checking is not available on disk %1.
//
#define MSG_1044                         0x00000414L

//
// MessageId: MSG_1045
//
// MessageText:
//
//  A nonvalid parameter was specified.
//
#define MSG_1045                         0x00000415L

//
// MessageId: MSG_PATH_NOT_FOUND
//
// MessageText:
//
//  The specified path was not found.
//
#define MSG_PATH_NOT_FOUND               0x00000416L

//
// MessageId: MSG_FILE_NOT_FOUND
//
// MessageText:
//
//  The %1 file was not found.
//
#define MSG_FILE_NOT_FOUND               0x00000417L

//
// MessageId: MSG_LOST_CHAINS
//
// MessageText:
//
//     %1 lost allocation units were found in %2 chains.
//
#define MSG_LOST_CHAINS                  0x00000418L

//
// MessageId: MSG_BLANK_LINE
//
// MessageText:
//
//  
//
#define MSG_BLANK_LINE                   0x00000419L

//
// MessageId: MSG_1050
//
// MessageText:
//
//     The CHDIR command cannot switch to the root folder.
//
#define MSG_1050                         0x0000041AL

//
// MessageId: MSG_BAD_FAT_WRITE
//
// MessageText:
//
//     A disk error occurred during writing of the file allocation table.
//
#define MSG_BAD_FAT_WRITE                0x0000041BL

//
// MessageId: MSG_ONE_STRING
//
// MessageText:
//
//  %1.
//
#define MSG_ONE_STRING                   0x0000041CL

//
// MessageId: MSG_ONE_STRING_NEWLINE
//
// MessageText:
//
//  %1
//
#define MSG_ONE_STRING_NEWLINE           0x0000041EL

//
// MessageId: MSG_NO_ROOM_IN_ROOT
//
// MessageText:
//
//     The root folder on this volume is full. To perform a disk check,
//     Windows requires space in the root folder. Remove some files
//     from this folder, then run disk checking again.
//
#define MSG_NO_ROOM_IN_ROOT              0x0000041FL

//
// MessageId: MSG_1056
//
// MessageText:
//
//  %1 %2 %3.
//
#define MSG_1056                         0x00000420L

//
// MessageId: MSG_1057
//
// MessageText:
//
//  %1 %2, %3.
//
#define MSG_1057                         0x00000421L

//
// MessageId: MSG_1058
//
// MessageText:
//
//  %1%2%3%4%5.
//
#define MSG_1058                         0x00000422L

//
// MessageId: MSG_1059
//
// MessageText:
//
//  %1%2%3%4.
//
#define MSG_1059                         0x00000423L

//
// MessageId: MSG_UNITS_ON_DISK
//
// MessageText:
//
//  %1 available allocation units on disk.
//
#define MSG_UNITS_ON_DISK                0x00000424L

//
// MessageId: MSG_1061
//
// MessageText:
//
//  Windows disk checking cannot fix errors (/F) when run from an
//  MS-DOS window. Try again from the Windows 2000 shell or command prompt.
//
#define MSG_1061                         0x00000425L

//
// MessageId: MSG_CHK_NO_MEMORY
//
// MessageText:
//
//  An unspecified error occurred.
//
#define MSG_CHK_NO_MEMORY                0x00000426L

//
// MessageId: MSG_HIDDEN_STATUS
//
// MessageText:
//
//  This never gets printed.
//
#define MSG_HIDDEN_STATUS                0x00000427L

//
// MessageId: MSG_CHK_USAGE_HEADER
//
// MessageText:
//
//  Checks a disk and displays a status report.
//  
//
#define MSG_CHK_USAGE_HEADER             0x00000428L

//
// MessageId: MSG_CHK_COMMAND_LINE
//
// MessageText:
//
//  CHKDSK [volume[[path]filename]]] [/F] [/V] [/R] [/X] [/I] [/C] [/L[:size]]
//  
//
#define MSG_CHK_COMMAND_LINE             0x00000429L

//
// MessageId: MSG_CHK_DRIVE
//
// MessageText:
//
//    volume          Specifies the drive letter (followed by a colon),
//                    mount point, or volume name.
//
#define MSG_CHK_DRIVE                    0x0000042AL

//
// MessageId: MSG_CHK_USG_FILENAME
//
// MessageText:
//
//    filename        FAT only: Specifies the files to check for fragmentation.
//
#define MSG_CHK_USG_FILENAME             0x0000042BL

//
// MessageId: MSG_CHK_F_SWITCH
//
// MessageText:
//
//    /F              Fixes errors on the disk.
//
#define MSG_CHK_F_SWITCH                 0x0000042CL

//
// MessageId: MSG_CHK_V_SWITCH
//
// MessageText:
//
//    /V              On FAT/FAT32: Displays the full path and name of every file
//                    on the disk.
//                    On NTFS: Displays cleanup messages if any.
//    /R              Locates bad sectors and recovers readable information
//                    (implies /F).
//    /L:size         NTFS only:  Changes the log file size to the specified number
//                    of kilobytes.  If size is not specified, displays current
//                    size.
//    /X              Forces the volume to dismount first if necessary.
//                    All opened handles to the volume would then be invalid
//                    (implies /F).
//    /I              NTFS only: Performs a less vigorous check of index entries.
//    /C              NTFS only: Skips checking of cycles within the folder
//                    structure.
//  
//  The /I or /C switch reduces the amount of time required to run Chkdsk by
//  skipping certain checks of the volume.
//
#define MSG_CHK_V_SWITCH                 0x0000042DL

//
// MessageId: MSG_WITHOUT_PARAMETERS
//
// MessageText:
//
//  To check the current disk, type CHKDSK with no parameters.
//
#define MSG_WITHOUT_PARAMETERS           0x0000042EL

//
// MessageId: MSG_CHK_CANT_CDROM
//
// MessageText:
//
//  Windows cannot run disk checking on CD-ROM and DVD-ROM drives.
//
#define MSG_CHK_CANT_CDROM               0x0000042FL

//
// MessageId: MSG_CHK_RUNNING
//
// MessageText:
//
//  Checking file system on %1
//
#define MSG_CHK_RUNNING                  0x00000430L

//
// MessageId: MSG_CHK_VOLUME_CLEAN
//
// MessageText:
//
//  The volume is clean.
//
#define MSG_CHK_VOLUME_CLEAN             0x00000431L

//
// MessageId: MSG_CHK_TRAILING_DIRENTS
//
// MessageText:
//
//  Removing trailing folder entries from %1
//
#define MSG_CHK_TRAILING_DIRENTS         0x00000432L

//
// MessageId: MSG_CHK_BAD_CLUSTERS_IN_FILE_SUCCESS
//
// MessageText:
//
//  Windows replaced bad clusters in file %1
//  of name %2.
//
#define MSG_CHK_BAD_CLUSTERS_IN_FILE_SUCCESS 0x00000433L

//
// MessageId: MSG_CHK_BAD_CLUSTERS_IN_FILE_FAILURE
//
// MessageText:
//
//  The disk does not have enough space to replace bad clusters
//  detected in file %1 of name %2.
//  
//
#define MSG_CHK_BAD_CLUSTERS_IN_FILE_FAILURE 0x00000434L

//
// MessageId: MSG_CHK_RECOVERING_FREE_SPACE
//
// MessageText:
//
//  Windows is verifying free space...
//
#define MSG_CHK_RECOVERING_FREE_SPACE    0x00000435L

//
// MessageId: MSG_CHK_DONE_RECOVERING_FREE_SPACE
//
// MessageText:
//
//  Free space verification is complete.
//
#define MSG_CHK_DONE_RECOVERING_FREE_SPACE 0x00000436L

//
// MessageId: MSG_CHK_CHECKING_FILES
//
// MessageText:
//
//  Windows is verifying files and folders...
//
#define MSG_CHK_CHECKING_FILES           0x00000437L

//
// MessageId: MSG_CHK_CANNOT_UPGRADE_DOWNGRADE_FAT
//
// MessageText:
//
//  Windows cannot upgrade this FAT volume.
//
#define MSG_CHK_CANNOT_UPGRADE_DOWNGRADE_FAT 0x00000438L

//
// MessageId: MSG_CHK_NO_MOUNT_POINT_FOR_GUID_VOLNAME_PATH
//
// MessageText:
//
//  The specified volume name does not have a mount point or drive letter.
//
#define MSG_CHK_NO_MOUNT_POINT_FOR_GUID_VOLNAME_PATH 0x00000439L

//
// MessageId: MSG_CHK_VOLUME_IS_DIRTY
//
// MessageText:
//
//  The volume is dirty.
//
#define MSG_CHK_VOLUME_IS_DIRTY          0x0000043AL

//-----------------------
//
// Windows 2000 Chkdsk messages.
//
//-----------------------
//
// MessageId: MSG_CHK_ON_REBOOT
//
// MessageText:
//
//  Do you want to schedule Windows to check your disk the next time
//  you start your computer? (Y/N) %0
//
#define MSG_CHK_ON_REBOOT                0x0000044CL

//
// MessageId: MSG_CHK_VOLUME_SET_DIRTY
//
// MessageText:
//
//  Windows will check your disk the next time you start
//  your computer.
//
#define MSG_CHK_VOLUME_SET_DIRTY         0x0000044DL

//
// MessageId: MSG_CHK_BOOT_PARTITION_REBOOT
//
// MessageText:
//
//  
//  Windows has finished checking your disk.
//  Please wait while your computer restarts.
//
#define MSG_CHK_BOOT_PARTITION_REBOOT    0x0000044EL

//
// MessageId: MSG_CHK_BAD_LONG_NAME
//
// MessageText:
//
//  Removing nonvalid long folder entry from %1...
//
#define MSG_CHK_BAD_LONG_NAME            0x0000044FL

//
// MessageId: MSG_CHK_CHECKING_VOLUME
//
// MessageText:
//
//  Now checking %1...
//
#define MSG_CHK_CHECKING_VOLUME          0x00000450L

//
// MessageId: MSG_CHK_BAD_LONG_NAME_IS
//
// MessageText:
//
//  Removing orphaned long folder entry %1...
//
#define MSG_CHK_BAD_LONG_NAME_IS         0x00000451L

//
// MessageId: MSG_CHK_WONT_ZERO_LOGFILE
//
// MessageText:
//
//  The log file size must be greater than 0.
//
#define MSG_CHK_WONT_ZERO_LOGFILE        0x00000452L

//
// MessageId: MSG_CHK_LOGFILE_NOT_NTFS
//
// MessageText:
//
//  Windows can set log file size on NTFS volumes only.
//
#define MSG_CHK_LOGFILE_NOT_NTFS         0x00000453L

//
// MessageId: MSG_CHK_BAD_DRIVE_PATH_FILENAME
//
// MessageText:
//
//  The drive, the path, or the file name is not valid.
//
#define MSG_CHK_BAD_DRIVE_PATH_FILENAME  0x00000454L

//
// MessageId: MSG_KILOBYTES_IN_USER_FILES
//
// MessageText:
//
//  %1 KB in %2 files.
//
#define MSG_KILOBYTES_IN_USER_FILES      0x00000455L

//
// MessageId: MSG_KILOBYTES_IN_DIRECTORIES
//
// MessageText:
//
//  %1 KB in %2 folders.
//
#define MSG_KILOBYTES_IN_DIRECTORIES     0x00000456L

//
// MessageId: MSG_KILOBYTES_IN_HIDDEN_FILES
//
// MessageText:
//
//  %1 KB in %2 hidden files.
//
#define MSG_KILOBYTES_IN_HIDDEN_FILES    0x00000457L

//
// MessageId: MSG_KILOBYTES_IN_WOULD_BE_RECOVERED_FILES
//
// MessageText:
//
//  %1 KB in %2 recoverable files.
//
#define MSG_KILOBYTES_IN_WOULD_BE_RECOVERED_FILES 0x00000458L

//
// MessageId: MSG_KILOBYTES_IN_RECOVERED_FILES
//
// MessageText:
//
//  %1 KB in %2 recovered files.
//
#define MSG_KILOBYTES_IN_RECOVERED_FILES 0x00000459L

//
// MessageId: MSG_CHK_ABORT_AUTOCHK
//
// MessageText:
//
//  To skip disk checking, press any key within %1 seconds. %r%0
//
#define MSG_CHK_ABORT_AUTOCHK            0x0000045AL

//
// MessageId: MSG_CHK_AUTOCHK_ABORTED
//
// MessageText:
//
//  Disk checking has been cancelled.                       %b
//
#define MSG_CHK_AUTOCHK_ABORTED          0x0000045BL

//
// MessageId: MSG_CHK_AUTOCHK_RESUMED
//
// MessageText:
//
//  Windows will now check the disk.                        %b
//
#define MSG_CHK_AUTOCHK_RESUMED          0x0000045CL

//
// MessageId: MSG_KILOBYTES_FREED
//
// MessageText:
//
//  %1 KB of free disk space added.
//
#define MSG_KILOBYTES_FREED              0x0000045DL

//
// MessageId: MSG_KILOBYTES_WOULD_BE_FREED
//
// MessageText:
//
//  %1 KB of free disk space would be added.
//
#define MSG_KILOBYTES_WOULD_BE_FREED     0x0000045EL

//
// MessageId: MSG_CHK_SKIP_INDEX_NOT_NTFS
//
// MessageText:
//
//  The /I option functions only on NTFS volumes.
//
#define MSG_CHK_SKIP_INDEX_NOT_NTFS      0x0000045FL

//
// MessageId: MSG_CHK_SKIP_CYCLE_NOT_NTFS
//
// MessageText:
//
//  The /C option functions only on NTFS volumes.
//
#define MSG_CHK_SKIP_CYCLE_NOT_NTFS      0x00000460L

//
// MessageId: MSG_CHK_AUTOCHK_COMPLETE
//
// MessageText:
//
//  Windows has finished checking the disk.
//
#define MSG_CHK_AUTOCHK_COMPLETE         0x00000461L

//
// MessageId: MSG_CHK_AUTOCHK_SKIP_WARNING
//
// MessageText:
//
//  
//  One of your disks needs to be checked for consistency. You
//  may cancel the disk check, but it is strongly recommended
//  that you continue.
//
#define MSG_CHK_AUTOCHK_SKIP_WARNING     0x00000462L

//
// MessageId: MSG_CHK_USER_AUTOCHK_SKIP_WARNING
//
// MessageText:
//
//  
//  A disk check has been scheduled.
//
#define MSG_CHK_USER_AUTOCHK_SKIP_WARNING 0x00000463L

//
// MessageId: MSG_CHK_UNABLE_TO_TELL_IF_SYSTEM_DRIVE
//
// MessageText:
//
//  Windows was unable to determine if the specified volume is a system volume.
//
#define MSG_CHK_UNABLE_TO_TELL_IF_SYSTEM_DRIVE 0x00000464L

//
// MessageId: MSG_CHK_NO_PROBLEM_FOUND
//
// MessageText:
//
//  Windows has checked the file system and found no problem.
//
#define MSG_CHK_NO_PROBLEM_FOUND         0x00000465L

//
// MessageId: MSG_CHK_ERRORS_FIXED
//
// MessageText:
//
//  Windows has made corrections to the file system.
//
#define MSG_CHK_ERRORS_FIXED             0x00000466L

//
// MessageId: MSG_CHK_NEED_F_PARAMETER
//
// MessageText:
//
//  Windows found problems with the file system.
//  Run CHKDSK with the /F (fix) option to correct these.
//
#define MSG_CHK_NEED_F_PARAMETER         0x00000467L

//
// MessageId: MSG_CHK_ERRORS_NOT_FIXED
//
// MessageText:
//
//  Windows found problems with the file system that could not be corrected.
//
#define MSG_CHK_ERRORS_NOT_FIXED         0x00000468L

//-----------------------
//
// DOS 5 Format messages.
//
//-----------------------
//
// MessageId: MSG_PERCENT_COMPLETE
//
// MessageText:
//
//  %1 percent completed.               %r%0
//
#define MSG_PERCENT_COMPLETE             0x000007D0L

//
// MessageId: MSG_PERCENT_COMPLETE2
//
// MessageText:
//
//  %1 percent completed.%2             %r%0
//
#define MSG_PERCENT_COMPLETE2            0x000007D4L

//
// MessageId: MSG_FORMAT_COMPLETE
//
// MessageText:
//
//  Format complete.                        %b
//
#define MSG_FORMAT_COMPLETE              0x000007D1L

//
// MessageId: MSG_INSERT_DISK
//
// MessageText:
//
//  Insert new disk for drive %1
//
#define MSG_INSERT_DISK                  0x000007D2L

//
// MessageId: MSG_REINSERT_DISKETTE
//
// MessageText:
//
//  Reinsert disk for drive %1:
//
#define MSG_REINSERT_DISKETTE            0x000007D3L

//
// MessageId: MSG_BAD_IOCTL
//
// MessageText:
//
//  Error in IOCTL call.
//
#define MSG_BAD_IOCTL                    0x000007D6L

//
// MessageId: MSG_CANT_DASD
//
// MessageText:
//
//  Cannot open volume for direct access.
//
#define MSG_CANT_DASD                    0x000007D7L

//
// MessageId: MSG_CANT_WRITE_FAT
//
// MessageText:
//
//  Error writing File Allocation Table (FAT).
//
#define MSG_CANT_WRITE_FAT               0x000007D8L

//
// MessageId: MSG_CANT_WRITE_ROOT_DIR
//
// MessageText:
//
//  Error writing folder.
//
#define MSG_CANT_WRITE_ROOT_DIR          0x000007D9L

//
// MessageId: MSG_FORMAT_NO_NETWORK
//
// MessageText:
//
//  Cannot format a network drive.
//
#define MSG_FORMAT_NO_NETWORK            0x000007DCL

//
// MessageId: MSG_UNSUPPORTED_PARAMETER
//
// MessageText:
//
//  Parameters not supported.
//
#define MSG_UNSUPPORTED_PARAMETER        0x000007DDL

//
// MessageId: MSG_UNUSABLE_DISK
//
// MessageText:
//
//  Invalid media or Track 0 bad - disk unusable.
//
#define MSG_UNUSABLE_DISK                0x000007E0L

//
// MessageId: MSG_BAD_DIR_READ
//
// MessageText:
//
//  Error reading folder %1.
//
#define MSG_BAD_DIR_READ                 0x000007E2L

//
// MessageId: MSG_PRESS_ENTER_WHEN_READY
//
// MessageText:
//
//  and press ENTER when ready... %0
//
#define MSG_PRESS_ENTER_WHEN_READY       0x000007E3L

//
// MessageId: MSG_ENTER_CURRENT_LABEL
//
// MessageText:
//
//  Enter current volume label for drive %1 %0
//
#define MSG_ENTER_CURRENT_LABEL          0x000007E5L

//
// MessageId: MSG_INCOMPATIBLE_PARAMETERS_FOR_FIXED
//
// MessageText:
//
//  Parameters incompatible with fixed disk.
//
#define MSG_INCOMPATIBLE_PARAMETERS_FOR_FIXED 0x000007E6L

//
// MessageId: MSG_READ_PARTITION_TABLE
//
// MessageText:
//
//  Error reading partition table.
//
#define MSG_READ_PARTITION_TABLE         0x000007E7L

//
// MessageId: MSG_NOT_SUPPORTED_BY_DRIVE
//
// MessageText:
//
//  Parameters not supported by drive.
//
#define MSG_NOT_SUPPORTED_BY_DRIVE       0x000007ECL

//
// MessageId: MSG_2029
//
// MessageText:
//
//  
//
#define MSG_2029                         0x000007EDL

//
// MessageId: MSG_2030
//
// MessageText:
//
//  
//  
//
#define MSG_2030                         0x000007EEL

//
// MessageId: MSG_INSERT_DOS_DISK
//
// MessageText:
//
//  Insert Windows 2000 disk in drive %1:
//
#define MSG_INSERT_DOS_DISK              0x000007EFL

//
// MessageId: MSG_WARNING_FORMAT
//
// MessageText:
//
//  
//  WARNING, ALL DATA ON NON-REMOVABLE DISK
//  DRIVE %1 WILL BE LOST!
//  Proceed with Format (Y/N)? %0
//
#define MSG_WARNING_FORMAT               0x000007F0L

//
// MessageId: MSG_FORMAT_ANOTHER
//
// MessageText:
//
//  
//  Format another (Y/N)? %0
//
#define MSG_FORMAT_ANOTHER               0x000007F1L

//
// MessageId: MSG_WRITE_PARTITION_TABLE
//
// MessageText:
//
//  Error writing partition table.
//
#define MSG_WRITE_PARTITION_TABLE        0x000007F3L

//
// MessageId: MSG_INCOMPATIBLE_PARAMETERS
//
// MessageText:
//
//  Parameters not compatible.
//
#define MSG_INCOMPATIBLE_PARAMETERS      0x000007F4L

//
// MessageId: MSG_AVAILABLE_ALLOCATION_UNITS
//
// MessageText:
//
//  %1 allocation units available on disk.
//
#define MSG_AVAILABLE_ALLOCATION_UNITS   0x000007F5L

//
// MessageId: MSG_ALLOCATION_UNIT_SIZE
//
// MessageText:
//
//  
//  %1 bytes in each allocation unit.
//
#define MSG_ALLOCATION_UNIT_SIZE         0x000007F6L

//
// MessageId: MSG_PARAMETER_TWICE
//
// MessageText:
//
//  Same parameter entered twice.
//
#define MSG_PARAMETER_TWICE              0x000007F8L

//
// MessageId: MSG_NEED_BOTH_T_AND_N
//
// MessageText:
//
//  Must enter both /t and /n parameters.
//
#define MSG_NEED_BOTH_T_AND_N            0x000007F9L

//
// MessageId: MSG_2042
//
// MessageText:
//
//  Trying to recover allocation unit %1.                          %0
//
#define MSG_2042                         0x000007FAL

//
// MessageId: MSG_NO_LABEL_WITH_8
//
// MessageText:
//
//  Volume label is not supported with /8 parameter.
//
#define MSG_NO_LABEL_WITH_8              0x000007FFL

//
// MessageId: MSG_FMT_NO_MEMORY
//
// MessageText:
//
//  Insufficient memory.
//
#define MSG_FMT_NO_MEMORY                0x00000801L

//
// MessageId: MSG_QUICKFMT_ANOTHER
//
// MessageText:
//
//  
//  QuickFormat another (Y/N)? %0
//
#define MSG_QUICKFMT_ANOTHER             0x00000802L

//
// MessageId: MSG_CANT_QUICKFMT
//
// MessageText:
//
//  Invalid existing format.
//  This disk cannot be QuickFormatted.
//  Proceed with unconditional format (Y/N)? %0
//
#define MSG_CANT_QUICKFMT                0x00000804L

//
// MessageId: MSG_FORMATTING_KB
//
// MessageText:
//
//  Formatting %1K
//
#define MSG_FORMATTING_KB                0x00000805L

//
// MessageId: MSG_FORMATTING_MB
//
// MessageText:
//
//  Formatting %1M
//
#define MSG_FORMATTING_MB                0x00000806L

//
// MessageId: MSG_FORMATTING_DOT_MB
//
// MessageText:
//
//  Formatting %1.%2M
//
#define MSG_FORMATTING_DOT_MB            0x00000807L

//
// MessageId: MSG_VERIFYING_KB
//
// MessageText:
//
//  Verifying %1K
//
#define MSG_VERIFYING_KB                 0x00000809L

//
// MessageId: MSG_VERIFYING_MB
//
// MessageText:
//
//  Verifying %1M
//
#define MSG_VERIFYING_MB                 0x0000080AL

//
// MessageId: MSG_VERIFYING_DOT_MB
//
// MessageText:
//
//  Verifying %1.%2M
//
#define MSG_VERIFYING_DOT_MB             0x0000080BL

//
// MessageId: MSG_2060
//
// MessageText:
//
//  Saving UNFORMAT information.
//
#define MSG_2060                         0x0000080CL

//
// MessageId: MSG_2061
//
// MessageText:
//
//  Checking existing disk format.
//
#define MSG_2061                         0x0000080DL

//
// MessageId: MSG_QUICKFORMATTING_KB
//
// MessageText:
//
//  QuickFormatting %1K
//
#define MSG_QUICKFORMATTING_KB           0x0000080EL

//
// MessageId: MSG_QUICKFORMATTING_MB
//
// MessageText:
//
//  QuickFormatting %1M
//
#define MSG_QUICKFORMATTING_MB           0x0000080FL

//
// MessageId: MSG_QUICKFORMATTING_DOT_MB
//
// MessageText:
//
//  QuickFormatting %1.%2M
//
#define MSG_QUICKFORMATTING_DOT_MB       0x00000810L

//
// MessageId: MSG_FORMAT_INFO
//
// MessageText:
//
//  Formats a disk for use with Windows 2000.
//  
//
#define MSG_FORMAT_INFO                  0x00000811L

//
// MessageId: MSG_FORMAT_COMMAND_LINE_1
//
// MessageText:
//
//  FORMAT volume [/FS:file-system] [/V:label] [/Q] [/A:size] [/C] [/X]
//  FORMAT volume [/V:label] [/Q] [/F:size]
//
#define MSG_FORMAT_COMMAND_LINE_1        0x00000812L

//
// MessageId: MSG_FORMAT_COMMAND_LINE_2
//
// MessageText:
//
//  FORMAT volume [/V:label] [/Q] [/T:tracks /N:sectors]
//
#define MSG_FORMAT_COMMAND_LINE_2        0x00000813L

//
// MessageId: MSG_FORMAT_COMMAND_LINE_3
//
// MessageText:
//
//  FORMAT volume [/V:label] [/Q] [/1] [/4]
//
#define MSG_FORMAT_COMMAND_LINE_3        0x00000814L

//
// MessageId: MSG_FORMAT_COMMAND_LINE_4
//
// MessageText:
//
//  FORMAT volume [/Q] [/1] [/4] [/8]
//  
//    volume          Specifies the drive letter (followed by a colon),
//                    mount point, or volume name.
//    /FS:filesystem  Specifies the type of the file system (FAT, FAT32, or NTFS).
//
#define MSG_FORMAT_COMMAND_LINE_4        0x00000815L

//
// MessageId: MSG_FORMAT_SLASH_V
//
// MessageText:
//
//    /V:label        Specifies the volume label.
//
#define MSG_FORMAT_SLASH_V               0x00000816L

//
// MessageId: MSG_FORMAT_SLASH_Q
//
// MessageText:
//
//    /Q              Performs a quick format.
//
#define MSG_FORMAT_SLASH_Q               0x00000817L

//
// MessageId: MSG_FORMAT_SLASH_C
//
// MessageText:
//
//    /C              Files created on the new volume will be compressed by
//                    default.
//
#define MSG_FORMAT_SLASH_C               0x00000818L

//
// MessageId: MSG_FORMAT_SLASH_F
//
// MessageText:
//
//    /A:size         Overrides the default allocation unit size. Default settings
//                    are strongly recommended for general use.
//                    NTFS supports 512, 1024, 2048, 4096, 8192, 16K, 32K, 64K.
//                    FAT supports 512, 1024, 2048, 4096, 8192, 16K, 32K, 64K,
//                    (128K, 256K for sector size > 512 bytes).
//                    FAT32 supports 512, 1024, 2048, 4096, 8192, 16K, 32K, 64K,
//                    (128K, 256K for sector size > 512 bytes).
//  
//                        Note that the FAT and FAT32 files systems impose the
//                    following restrictions on the number of clusters on a volume:
//  
//                    FAT: Number of clusters <= 65526
//                    FAT32: 65526 < Number of clusters < 268435446
//  
//                    Format will immediately stop processing if it decides that
//                    the above requirements cannot be met using the specified
//                    cluster size.
//  
//                    NTFS compression is not supported for allocation unit sizes
//                    above 4096.
//    /F:size         Specifies the size of the floppy disk to format (160,
//
#define MSG_FORMAT_SLASH_F               0x00000819L

//
// MessageId: MSG_FORMAT_SUPPORTED_SIZES
//
// MessageText:
//
//                    180, 320, 360, 640, 720, 1.2, 1.23, 1.44, 2.88, or 20.8).
//
#define MSG_FORMAT_SUPPORTED_SIZES       0x0000081AL

//
// MessageId: MSG_WRONG_CURRENT_LABEL
//
// MessageText:
//
//  An incorrect volume label was entered for this drive.
//
#define MSG_WRONG_CURRENT_LABEL          0x0000081BL

//
// MessageId: MSG_FORMAT_SLASH_T
//
// MessageText:
//
//    /T:tracks       Specifies the number of tracks per disk side.
//
#define MSG_FORMAT_SLASH_T               0x0000081DL

//
// MessageId: MSG_FORMAT_SLASH_N
//
// MessageText:
//
//    /N:sectors      Specifies the number of sectors per track.
//
#define MSG_FORMAT_SLASH_N               0x0000081EL

//
// MessageId: MSG_FORMAT_SLASH_1
//
// MessageText:
//
//    /1              Formats a single side of a floppy disk.
//
#define MSG_FORMAT_SLASH_1               0x0000081FL

//
// MessageId: MSG_FORMAT_SLASH_4
//
// MessageText:
//
//    /4              Formats a 5.25-inch 360K floppy disk in a
//                    high-density drive.
//
#define MSG_FORMAT_SLASH_4               0x00000820L

//
// MessageId: MSG_FORMAT_SLASH_8
//
// MessageText:
//
//    /8              Formats eight sectors per track.
//
#define MSG_FORMAT_SLASH_8               0x00000821L

//
// MessageId: MSG_FORMAT_SLASH_X
//
// MessageText:
//
//    /X              Forces the volume to dismount first if necessary.  All opened
//                    handles to the volume would no longer be valid.
//
#define MSG_FORMAT_SLASH_X               0x00000822L

//
// MessageId: MSG_FORMAT_NO_CDROM
//
// MessageText:
//
//  Cannot format a CD-ROM drive.
//
#define MSG_FORMAT_NO_CDROM              0x00000823L

//
// MessageId: MSG_FORMAT_NO_RAMDISK
//
// MessageText:
//
//  Cannot format a RAM DISK drive.
//
#define MSG_FORMAT_NO_RAMDISK            0x00000824L

//
// MessageId: MSG_FORMAT_PLEASE_USE_FS_SWITCH
//
// MessageText:
//
//  Please use the /FS switch to specify the file system
//  you wish to use on this volume.
//
#define MSG_FORMAT_PLEASE_USE_FS_SWITCH  0x00000826L

//
// MessageId: MSG_NTFS_FORMAT_FAILED
//
// MessageText:
//
//  Format failed.
//
#define MSG_NTFS_FORMAT_FAILED           0x00000827L

//
// MessageId: MSG_FMT_WRITE_PROTECTED_MEDIA
//
// MessageText:
//
//  Cannot format.  This media is write protected.
//
#define MSG_FMT_WRITE_PROTECTED_MEDIA    0x00000828L

//
// MessageId: MSG_FMT_INSTALL_FILE_SYSTEM
//
// MessageText:
//
//  
//  WARNING!  The %1 file system is not enabled.
//  Would you like to enable it (Y/N)? %0
//
#define MSG_FMT_INSTALL_FILE_SYSTEM      0x00000829L

//
// MessageId: MSG_FMT_FILE_SYSTEM_INSTALLED
//
// MessageText:
//
//  
//  The file system will be enabled when you restart the system.
//
#define MSG_FMT_FILE_SYSTEM_INSTALLED    0x0000082AL

//
// MessageId: MSG_FMT_CANT_INSTALL_FILE_SYSTEM
//
// MessageText:
//
//  
//  FORMAT cannot enable the file system.
//
#define MSG_FMT_CANT_INSTALL_FILE_SYSTEM 0x0000082BL

//
// MessageId: MSG_FMT_VOLUME_TOO_SMALL
//
// MessageText:
//
//  The volume is too small for the specified file system.
//
#define MSG_FMT_VOLUME_TOO_SMALL         0x0000082CL

//
// MessageId: MSG_FMT_CREATING_FILE_SYSTEM
//
// MessageText:
//
//  Creating file system structures.
//
#define MSG_FMT_CREATING_FILE_SYSTEM     0x0000082DL

//
// MessageId: MSG_FMT_VARIABLE_CLUSTERS_NOT_SUPPORTED
//
// MessageText:
//
//  %1 FORMAT does not support user selected allocation unit sizes.
//
#define MSG_FMT_VARIABLE_CLUSTERS_NOT_SUPPORTED 0x0000082EL

//
// MessageId: MSG_DEVICE_BUSY
//
// MessageText:
//
//  The device is busy.
//
#define MSG_DEVICE_BUSY                  0x00000830L

//
// MessageId: MSG_FMT_DMF_NOT_SUPPORTED_ON_288_DRIVES
//
// MessageText:
//
//  The specified format cannot be mastered on 2.88MB drives.
//
#define MSG_FMT_DMF_NOT_SUPPORTED_ON_288_DRIVES 0x00000831L

//
// MessageId: MSG_HPFS_NO_FORMAT
//
// MessageText:
//
//  FORMAT does not support the HPFS file system type.
//
#define MSG_HPFS_NO_FORMAT               0x00000832L

//
// MessageId: MSG_FMT_ALLOCATION_SIZE_CHANGED
//
// MessageText:
//
//  Allocation unit size changed to %1 bytes.
//
#define MSG_FMT_ALLOCATION_SIZE_CHANGED  0x00000833L

//
// MessageId: MSG_FMT_ALLOCATION_SIZE_EXCEEDED
//
// MessageText:
//
//  Allocation unit size must be less than or equal to 64K.
//
#define MSG_FMT_ALLOCATION_SIZE_EXCEEDED 0x00000834L

//
// MessageId: MSG_FMT_TOO_MANY_CLUSTERS
//
// MessageText:
//
//  Number of clusters exceeds 32 bits.
//
#define MSG_FMT_TOO_MANY_CLUSTERS        0x00000835L

//
// MessageId: MSG_CONV_PAUSE_BEFORE_REBOOT
//
// MessageText:
//
//  
//  Preinstallation completed successfully.  Press any key to
//  shut down/reboot.
//
#define MSG_CONV_PAUSE_BEFORE_REBOOT     0x0000089BL

//
// MessageId: MSG_CONV_WILL_REBOOT
//
// MessageText:
//
//  
//  Convert will take some time to process the files on the volume.
//  When this phase of conversion is complete, the computer will restart.
//
#define MSG_CONV_WILL_REBOOT             0x0000089CL

//
// MessageId: MSG_FMT_FAT_ENTRY_SIZE
//
// MessageText:
//
//  %1 bits in each FAT entry.
//
#define MSG_FMT_FAT_ENTRY_SIZE           0x0000089DL

//
// MessageId: MSG_FMT_CLUSTER_SIZE_MISMATCH
//
// MessageText:
//
//  The cluster size chosen by the system is %1 bytes which
//  differs from the specified cluster size.
//  Proceed with Format using the cluster size chosen by the
//  system (Y/N)? %0
//
#define MSG_FMT_CLUSTER_SIZE_MISMATCH    0x0000089EL

//
// MessageId: MSG_FMT_CLUSTER_SIZE_TOO_SMALL
//
// MessageText:
//
//  The specified cluster size is too small for %1.
//
#define MSG_FMT_CLUSTER_SIZE_TOO_SMALL   0x0000089FL

//
// MessageId: MSG_FMT_CLUSTER_SIZE_TOO_BIG
//
// MessageText:
//
//  The specified cluster size is too big for %1.
//
#define MSG_FMT_CLUSTER_SIZE_TOO_BIG     0x000008A0L

//
// MessageId: MSG_FMT_VOL_TOO_BIG
//
// MessageText:
//
//  The volume is too big for %1.
//
#define MSG_FMT_VOL_TOO_BIG              0x000008A1L

//
// MessageId: MSG_FMT_VOL_TOO_SMALL
//
// MessageText:
//
//  The volume is too small for %1.
//
#define MSG_FMT_VOL_TOO_SMALL            0x000008A2L

//
// MessageId: MSG_FMT_ROOTDIR_WRITE_FAILED
//
// MessageText:
//
//  Failed to write to the root folder.
//
#define MSG_FMT_ROOTDIR_WRITE_FAILED     0x000008A3L

//
// MessageId: MSG_FMT_INIT_LABEL_FAILED
//
// MessageText:
//
//  Failed to initialize the volume label.
//
#define MSG_FMT_INIT_LABEL_FAILED        0x000008A4L

//
// MessageId: MSG_FMT_INITIALIZING_FATS
//
// MessageText:
//
//  Initializing the File Allocation Table (FAT)...
//
#define MSG_FMT_INITIALIZING_FATS        0x000008A5L

//
// MessageId: MSG_FMT_CLUSTER_SIZE_64K
//
// MessageText:
//
//  The cluster size for this volume, 64K bytes, may cause application
//  compatibility problems, particularly with setup applications.
//  The volume must be less than 2048 MB in size to change this if the
//  default cluster size is being used.
//  Proceed with Format using a 64K cluster (Y/N)? %0
//
#define MSG_FMT_CLUSTER_SIZE_64K         0x000008A6L

//
// MessageId: MSG_FMT_SECTORS
//
// MessageText:
//
//  Set number of sectors on drive to %1.
//
#define MSG_FMT_SECTORS                  0x000008A7L

//
// MessageId: MSG_FMT_BAD_SECTORS
//
// MessageText:
//
//  Environmental variable FORMAT_SECTORS error.
//
#define MSG_FMT_BAD_SECTORS              0x000008A8L

//
// MessageId: MSG_FMT_FORCE_DISMOUNT_PROMPT
//
// MessageText:
//
//  
//  Format cannot run because the volume is in use by another
//  process.  Format may run if this volume is dismounted first.
//  ALL OPENED HANDLES TO THIS VOLUME WOULD THEN BE INVALID.
//  Would you like to force a dismount on this volume? (Y/N) %0
//
#define MSG_FMT_FORCE_DISMOUNT_PROMPT    0x000008A9L

//
// MessageId: MSG_FORMAT_NO_MEDIA_IN_DRIVE
//
// MessageText:
//
//  There is no media in the drive.
//
#define MSG_FORMAT_NO_MEDIA_IN_DRIVE     0x000008AAL

//
// MessageId: MSG_FMT_NO_MOUNT_POINT_FOR_GUID_VOLNAME_PATH
//
// MessageText:
//
//  The given volume name does not have a mount point or drive letter.
//
#define MSG_FMT_NO_MOUNT_POINT_FOR_GUID_VOLNAME_PATH 0x000008ABL

//
// MessageId: MSG_FMT_INVALID_DRIVE_SPEC
//
// MessageText:
//
//  Invalid drive specification.
//
#define MSG_FMT_INVALID_DRIVE_SPEC       0x000008ACL

//
// MessageId: MSG_CONV_NO_MOUNT_POINT_FOR_GUID_VOLNAME_PATH
//
// MessageText:
//
//  The given volume name does not have a mount point or drive letter.
//
#define MSG_CONV_NO_MOUNT_POINT_FOR_GUID_VOLNAME_PATH 0x000008ADL

//
// MessageId: MSG_FMT_CLUSTER_SIZE_TOO_SMALL_MIN
//
// MessageText:
//
//  The specified cluster size is too small. The minimum valid
//  cluster size value for this drive is %1.
//
#define MSG_FMT_CLUSTER_SIZE_TOO_SMALL_MIN 0x000008AEL

//
// MessageId: MSG_FMT_FAT32_NO_FLOPPIES
//
// MessageText:
//
//  Floppy disk is too small to hold the FAT32 file system.
//
#define MSG_FMT_FAT32_NO_FLOPPIES        0x000008AFL

//----------------------
//
// Common ulib messages.
//
//----------------------
//
// MessageId: MSG_CANT_LOCK_THE_DRIVE
//
// MessageText:
//
//  Cannot lock the drive.  The volume is still in use.
//
#define MSG_CANT_LOCK_THE_DRIVE          0x00000BB8L

//
// MessageId: MSG_CANT_READ_BOOT_SECTOR
//
// MessageText:
//
//  Cannot read boot sector.
//
#define MSG_CANT_READ_BOOT_SECTOR        0x00000BBAL

//
// MessageId: MSG_VOLUME_SERIAL_NUMBER
//
// MessageText:
//
//  Volume Serial Number is %1-%2
//
#define MSG_VOLUME_SERIAL_NUMBER         0x00000BBBL

//
// MessageId: MSG_VOLUME_LABEL_PROMPT
//
// MessageText:
//
//  Volume label (11 characters, ENTER for none)? %0
//
#define MSG_VOLUME_LABEL_PROMPT          0x00000BBCL

//
// MessageId: MSG_INVALID_LABEL_CHARACTERS
//
// MessageText:
//
//  Invalid characters in volume label
//
#define MSG_INVALID_LABEL_CHARACTERS     0x00000BBDL

//
// MessageId: MSG_CANT_READ_ANY_FAT
//
// MessageText:
//
//  There are no readable file allocation tables (FAT).
//
#define MSG_CANT_READ_ANY_FAT            0x00000BBEL

//
// MessageId: MSG_SOME_FATS_UNREADABLE
//
// MessageText:
//
//  Some file allocation tables (FAT) are unreadable.
//
#define MSG_SOME_FATS_UNREADABLE         0x00000BBFL

//
// MessageId: MSG_CANT_WRITE_BOOT_SECTOR
//
// MessageText:
//
//  Cannot write boot sector.
//
#define MSG_CANT_WRITE_BOOT_SECTOR       0x00000BC0L

//
// MessageId: MSG_SOME_FATS_UNWRITABLE
//
// MessageText:
//
//  Some file allocation tables (FAT) are unwriteable.
//
#define MSG_SOME_FATS_UNWRITABLE         0x00000BC1L

//
// MessageId: MSG_INSUFFICIENT_DISK_SPACE
//
// MessageText:
//
//  Insufficient disk space.
//
#define MSG_INSUFFICIENT_DISK_SPACE      0x00000BC2L

//
// MessageId: MSG_TOTAL_KILOBYTES
//
// MessageText:
//
//  %1 KB total disk space.
//
#define MSG_TOTAL_KILOBYTES              0x00000BC3L

//
// MessageId: MSG_AVAILABLE_KILOBYTES
//
// MessageText:
//
//  %1 KB are available.
//
#define MSG_AVAILABLE_KILOBYTES          0x00000BC4L

//
// MessageId: MSG_NOT_FAT
//
// MessageText:
//
//  Disk not formatted or not FAT.
//
#define MSG_NOT_FAT                      0x00000BC5L

//
// MessageId: MSG_REQUIRED_PARAMETER
//
// MessageText:
//
//  Required parameter missing -
//
#define MSG_REQUIRED_PARAMETER           0x00000BC6L

//
// MessageId: MSG_FILE_SYSTEM_TYPE
//
// MessageText:
//
//  The type of the file system is %1.
//
#define MSG_FILE_SYSTEM_TYPE             0x00000BC7L

//
// MessageId: MSG_NEW_FILE_SYSTEM_TYPE
//
// MessageText:
//
//  The new file system is %1.
//
#define MSG_NEW_FILE_SYSTEM_TYPE         0x00000BC8L

//
// MessageId: MSG_FMT_AN_ERROR_OCCURRED
//
// MessageText:
//
//  An error occurred while running Format.
//
#define MSG_FMT_AN_ERROR_OCCURRED        0x00000BC9L

//
// MessageId: MSG_FS_NOT_SUPPORTED
//
// MessageText:
//
//  %1 is not available for %2 drives.
//
#define MSG_FS_NOT_SUPPORTED             0x00000BCAL

//
// MessageId: MSG_FS_NOT_DETERMINED
//
// MessageText:
//
//  Cannot determine file system of drive %1.
//
#define MSG_FS_NOT_DETERMINED            0x00000BCBL

//
// MessageId: MSG_CANT_DISMOUNT
//
// MessageText:
//
//  Cannot dismount the drive.
//
#define MSG_CANT_DISMOUNT                0x00000BCCL

//
// MessageId: MSG_NOT_FULL_PATH_NAME
//
// MessageText:
//
//  %1 is not a complete name.
//
#define MSG_NOT_FULL_PATH_NAME           0x00000BCDL

//
// MessageId: MSG_YES
//
// MessageText:
//
//  Yes
//
#define MSG_YES                          0x00000BCEL

//
// MessageId: MSG_NO
//
// MessageText:
//
//  No
//
#define MSG_NO                           0x00000BCFL

//
// MessageId: MSG_DISK_NOT_FORMATTED
//
// MessageText:
//
//  Disk is not formatted.
//
#define MSG_DISK_NOT_FORMATTED           0x00000BD0L

//
// MessageId: MSG_NONEXISTENT_DRIVE
//
// MessageText:
//
//  Specified drive does not exist.
//
#define MSG_NONEXISTENT_DRIVE            0x00000BD1L

//
// MessageId: MSG_INVALID_PARAMETER
//
// MessageText:
//
//  Invalid parameter - %1
//
#define MSG_INVALID_PARAMETER            0x00000BD2L

//
// MessageId: MSG_INSUFFICIENT_MEMORY
//
// MessageText:
//
//  Out of memory.
//
#define MSG_INSUFFICIENT_MEMORY          0x00000BD3L

//
// MessageId: MSG_ACCESS_DENIED
//
// MessageText:
//
//  Access denied - %1
//
#define MSG_ACCESS_DENIED                0x00000BD4L

//
// MessageId: MSG_DASD_ACCESS_DENIED
//
// MessageText:
//
//  Access denied.
//
#define MSG_DASD_ACCESS_DENIED           0x00000BD5L

//
// MessageId: MSG_CANT_LOCK_CURRENT_DRIVE
//
// MessageText:
//
//  Cannot lock current drive.
//
#define MSG_CANT_LOCK_CURRENT_DRIVE      0x00000BD6L

//
// MessageId: MSG_INVALID_LABEL
//
// MessageText:
//
//  Invalid volume label
//
#define MSG_INVALID_LABEL                0x00000BD7L

//
// MessageId: MSG_DISK_TOO_LARGE_TO_FORMAT
//
// MessageText:
//
//  The disk is too large to format for the specified file system.
//
#define MSG_DISK_TOO_LARGE_TO_FORMAT     0x00000BD8L

//
// MessageId: MSG_VOLUME_LABEL_NO_MAX
//
// MessageText:
//
//  Volume label (ENTER for none)? %0
//
#define MSG_VOLUME_LABEL_NO_MAX          0x00000BD9L

//
// MessageId: MSG_CHKDSK_ON_REBOOT_PROMPT
//
// MessageText:
//
//  
//  Chkdsk cannot run because the volume is in use by another
//  process.  Would you like to schedule this volume to be
//  checked the next time the system restarts? (Y/N) %0
//
#define MSG_CHKDSK_ON_REBOOT_PROMPT      0x00000BDAL

//
// MessageId: MSG_CHKDSK_CANNOT_SCHEDULE
//
// MessageText:
//
//  
//  Chkdsk could not schedule this volume to be checked
//  the next time the system restarts.
//
#define MSG_CHKDSK_CANNOT_SCHEDULE       0x00000BDBL

//
// MessageId: MSG_CHKDSK_SCHEDULED
//
// MessageText:
//
//  
//  This volume will be checked the next time the system restarts.
//
#define MSG_CHKDSK_SCHEDULED             0x00000BDCL

//
// MessageId: MSG_COMPRESSION_NOT_AVAILABLE
//
// MessageText:
//
//  Compression is not available for %1.
//
#define MSG_COMPRESSION_NOT_AVAILABLE    0x00000BDDL

//
// MessageId: MSG_CANNOT_ENABLE_COMPRESSION
//
// MessageText:
//
//  Cannot enable compression for the volume.
//
#define MSG_CANNOT_ENABLE_COMPRESSION    0x00000BDEL

//
// MessageId: MSG_CANNOT_COMPRESS_HUGE_CLUSTERS
//
// MessageText:
//
//  Compression is not supported on volumes with clusters larger than
//  4096 bytes.
//
#define MSG_CANNOT_COMPRESS_HUGE_CLUSTERS 0x00000BDFL

//
// MessageId: MSG_CANT_UNLOCK_THE_DRIVE
//
// MessageText:
//
//  Cannot unlock the drive.
//
#define MSG_CANT_UNLOCK_THE_DRIVE        0x00000BE0L

//
// MessageId: MSG_CHKDSK_FORCE_DISMOUNT_PROMPT
//
// MessageText:
//
//  
//  Chkdsk cannot run because the volume is in use by another
//  process.  Chkdsk may run if this volume is dismounted first.
//  ALL OPENED HANDLES TO THIS VOLUME WOULD THEN BE INVALID.
//  Would you like to force a dismount on this volume? (Y/N) %0
//
#define MSG_CHKDSK_FORCE_DISMOUNT_PROMPT 0x00000BE1L

//
// MessageId: MSG_VOLUME_DISMOUNTED
//
// MessageText:
//
//  Volume dismounted.  All opened handles to this volume are now invalid.
//
#define MSG_VOLUME_DISMOUNTED            0x00000BE2L

//
// MessageId: MSG_CHKDSK_DISMOUNT_ON_REBOOT_PROMPT
//
// MessageText:
//
//  
//  Chkdsk cannot dismount the volume because it is a system drive or
//  there is an active paging file on it.  Would you like to schedule
//  this volume to be checked the next time the system restarts? (Y/N) %0
//
#define MSG_CHKDSK_DISMOUNT_ON_REBOOT_PROMPT 0x00000BE3L

//
// MessageId: MSG_TOTAL_MEGABYTES
//
// MessageText:
//
//  %1 MB total disk space.
//
#define MSG_TOTAL_MEGABYTES              0x00000BE4L

//
// MessageId: MSG_AVAILABLE_MEGABYTES
//
// MessageText:
//
//  %1 MB are available.
//
#define MSG_AVAILABLE_MEGABYTES          0x00000BE5L

//---------------------
//
// FAT ChkDsk Messages.
//
//---------------------
//
// MessageId: MSG_CHK_ERRORS_IN_FAT
//
// MessageText:
//
//  Errors in file allocation table (FAT) corrected.
//
#define MSG_CHK_ERRORS_IN_FAT            0x00001388L

//
// MessageId: MSG_CHK_EAFILE_HAS_HANDLE
//
// MessageText:
//
//  Extended attribute file has handle.  Handle removed.
//
#define MSG_CHK_EAFILE_HAS_HANDLE        0x00001389L

//
// MessageId: MSG_CHK_EMPTY_EA_FILE
//
// MessageText:
//
//  Extended attribute file contains no extended attributes.  File deleted.
//
#define MSG_CHK_EMPTY_EA_FILE            0x0000138AL

//
// MessageId: MSG_CHK_ERASING_INVALID_LABEL
//
// MessageText:
//
//  Erasing invalid label.
//
#define MSG_CHK_ERASING_INVALID_LABEL    0x0000138BL

//
// MessageId: MSG_CHK_EA_SIZE
//
// MessageText:
//
//  %1 bytes in extended attributes.
//
#define MSG_CHK_EA_SIZE                  0x0000138CL

//
// MessageId: MSG_CHK_CANT_CHECK_EA_LOG
//
// MessageText:
//
//  Unreadable extended attribute header.
//  Cannot check extended attribute log.
//
#define MSG_CHK_CANT_CHECK_EA_LOG        0x0000138DL

//
// MessageId: MSG_CHK_BAD_LOG
//
// MessageText:
//
//  Extended attribute log is unintelligible.
//  Ignore log and continue? (Y/N) %0
//
#define MSG_CHK_BAD_LOG                  0x0000138EL

//
// MessageId: MSG_CHK_UNUSED_EA_PORTION
//
// MessageText:
//
//  Unused, unreadable, or unwriteable portion of extended attribute file removed.
//
#define MSG_CHK_UNUSED_EA_PORTION        0x0000138FL

//
// MessageId: MSG_CHK_EASET_SIZE
//
// MessageText:
//
//  Total size entry for extended attribute set at cluster %1 corrected.
//
#define MSG_CHK_EASET_SIZE               0x00001390L

//
// MessageId: MSG_CHK_EASET_NEED_COUNT
//
// MessageText:
//
//  Need count entry for extended attribute set at cluster %1 corrected.
//
#define MSG_CHK_EASET_NEED_COUNT         0x00001391L

//
// MessageId: MSG_CHK_UNORDERED_EA_SETS
//
// MessageText:
//
//  Extended attribute file is unsorted.
//  Sorting extended attribute file.
//
#define MSG_CHK_UNORDERED_EA_SETS        0x00001392L

//
// MessageId: MSG_CHK_NEED_MORE_HEADER_SPACE
//
// MessageText:
//
//  Insufficient space in extended attribute file for its header.
//  Attempting to allocate more disk space.
//
#define MSG_CHK_NEED_MORE_HEADER_SPACE   0x00001393L

//
// MessageId: MSG_CHK_INSUFFICIENT_DISK_SPACE
//
// MessageText:
//
//  Insufficient disk space to correct disk error.
//  Please free some disk space and run CHKDSK again.
//
#define MSG_CHK_INSUFFICIENT_DISK_SPACE  0x00001394L

//
// MessageId: MSG_CHK_RELOCATED_EA_HEADER
//
// MessageText:
//
//  Bad clusters in extended attribute file header relocated.
//
#define MSG_CHK_RELOCATED_EA_HEADER      0x00001395L

//
// MessageId: MSG_CHK_ERROR_IN_EA_HEADER
//
// MessageText:
//
//  Errors in extended attribute file header corrected.
//
#define MSG_CHK_ERROR_IN_EA_HEADER       0x00001396L

//
// MessageId: MSG_CHK_MORE_THAN_ONE_DOT
//
// MessageText:
//
//  More than one dot entry in folder %1.  Entry removed.
//
#define MSG_CHK_MORE_THAN_ONE_DOT        0x00001397L

//
// MessageId: MSG_CHK_DOT_IN_ROOT
//
// MessageText:
//
//  Dot entry found in root folder.  Entry removed.
//
#define MSG_CHK_DOT_IN_ROOT              0x00001398L

//
// MessageId: MSG_CHK_DOTDOT_IN_ROOT
//
// MessageText:
//
//  Dot-dot entry found in root folder.  Entry removed.
//
#define MSG_CHK_DOTDOT_IN_ROOT           0x00001399L

//
// MessageId: MSG_CHK_ERR_IN_DOT
//
// MessageText:
//
//  Dot entry in folder %1 has incorrect link.  Link corrected.
//
#define MSG_CHK_ERR_IN_DOT               0x0000139AL

//
// MessageId: MSG_CHK_ERR_IN_DOTDOT
//
// MessageText:
//
//  Dot-dot entry in folder %1 has incorrect link.  Link corrected.
//
#define MSG_CHK_ERR_IN_DOTDOT            0x0000139BL

//
// MessageId: MSG_CHK_DELETE_REPEATED_ENTRY
//
// MessageText:
//
//  More than one %1 entry in folder %2.  Entry removed.
//
#define MSG_CHK_DELETE_REPEATED_ENTRY    0x0000139CL

//
// MessageId: MSG_CHK_CYCLE_IN_TREE
//
// MessageText:
//
//  Folder %1 causes cycle in folder structure.
//  Folder entry removed.
//
#define MSG_CHK_CYCLE_IN_TREE            0x0000139DL

//
// MessageId: MSG_CHK_BAD_CLUSTERS_IN_DIR
//
// MessageText:
//
//  Folder %1 has bad clusters.
//  Bad clusters removed from folder.
//
#define MSG_CHK_BAD_CLUSTERS_IN_DIR      0x0000139EL

//
// MessageId: MSG_CHK_BAD_DIR
//
// MessageText:
//
//  Folder %1 is entirely unreadable.
//  Folder entry removed.
//
#define MSG_CHK_BAD_DIR                  0x0000139FL

//
// MessageId: MSG_CHK_FILENAME
//
// MessageText:
//
//  %1
//
#define MSG_CHK_FILENAME                 0x000013A0L

//
// MessageId: MSG_CHK_DIR_TRUNC
//
// MessageText:
//
//  Folder truncated.
//
#define MSG_CHK_DIR_TRUNC                0x000013A1L

//
// MessageId: MSG_CHK_CROSS_LINK_COPY
//
// MessageText:
//
//  Cross link resolved by copying.
//
#define MSG_CHK_CROSS_LINK_COPY          0x000013A2L

//
// MessageId: MSG_CHK_CROSS_LINK_TRUNC
//
// MessageText:
//
//  Insufficient disk space to copy cross-linked portion.
//  File being truncated.
//
#define MSG_CHK_CROSS_LINK_TRUNC         0x000013A3L

//
// MessageId: MSG_CHK_INVALID_NAME
//
// MessageText:
//
//  %1  Invalid name.  Folder entry removed.
//
#define MSG_CHK_INVALID_NAME             0x000013A4L

//
// MessageId: MSG_CHK_INVALID_TIME_STAMP
//
// MessageText:
//
//  %1  Invalid time stamp.
//
#define MSG_CHK_INVALID_TIME_STAMP       0x000013A5L

//
// MessageId: MSG_CHK_DIR_HAS_FILESIZE
//
// MessageText:
//
//  %1  Folder has non-zero file size.
//
#define MSG_CHK_DIR_HAS_FILESIZE         0x000013A6L

//
// MessageId: MSG_CHK_UNRECOG_EA_HANDLE
//
// MessageText:
//
//  %1  Unrecognized extended attribute handle.
//
#define MSG_CHK_UNRECOG_EA_HANDLE        0x000013A7L

//
// MessageId: MSG_CHK_SHARED_EA
//
// MessageText:
//
//  %1  Has handle extended attribute set belonging to another file.
//      Handle removed.
//
#define MSG_CHK_SHARED_EA                0x000013A8L

//
// MessageId: MSG_CHK_UNUSED_EA_SET
//
// MessageText:
//
//  Unused extended attribute set with handle %1 deleted from
//  extended attribute file.
//
#define MSG_CHK_UNUSED_EA_SET            0x000013A9L

//
// MessageId: MSG_CHK_NEW_OWNER_NAME
//
// MessageText:
//
//  Extended attribute set with handle %1 owner changed
//  from %2 to %3.
//
#define MSG_CHK_NEW_OWNER_NAME           0x000013AAL

//
// MessageId: MSG_CHK_BAD_LINKS_IN_ORPHANS
//
// MessageText:
//
//  Bad links in lost chain at cluster %1 corrected.
//
#define MSG_CHK_BAD_LINKS_IN_ORPHANS     0x000013ABL

//
// MessageId: MSG_CHK_CROSS_LINKED_ORPHAN
//
// MessageText:
//
//  Lost chain cross-linked at cluster %1.  Orphan truncated.
//
#define MSG_CHK_CROSS_LINKED_ORPHAN      0x000013ACL

//
// MessageId: MSG_ORPHAN_DISK_SPACE
//
// MessageText:
//
//  Insufficient disk space to recover lost data.
//
#define MSG_ORPHAN_DISK_SPACE            0x000013ADL

//
// MessageId: MSG_TOO_MANY_ORPHANS
//
// MessageText:
//
//  Insufficient disk space to recover lost data.
//
#define MSG_TOO_MANY_ORPHANS             0x000013AEL

//
// MessageId: MSG_CHK_ERROR_IN_LOG
//
// MessageText:
//
//  Error in extended attribute log.
//
#define MSG_CHK_ERROR_IN_LOG             0x000013AFL

//
// MessageId: MSG_CHK_ERRORS_IN_DIR_CORR
//
// MessageText:
//
//  %1 Errors in . and/or .. corrected.
//
#define MSG_CHK_ERRORS_IN_DIR_CORR       0x000013B0L

//
// MessageId: MSG_CHK_RENAMING_FAILURE
//
// MessageText:
//
//  More than one %1 entry in folder %2.
//  Renamed to %3 but still could not resolve the name conflict.
//
#define MSG_CHK_RENAMING_FAILURE         0x000013B1L

//
// MessageId: MSG_CHK_RENAMED_REPEATED_ENTRY
//
// MessageText:
//
//  More than one %1 entry in folder %2.
//  Renamed to %3.
//
#define MSG_CHK_RENAMED_REPEATED_ENTRY   0x000013B2L

//
// MessageId: MSG_CHK_UNHANDLED_INVALID_NAME
//
// MessageText:
//
//  %1 may be an invalid name in folder %2.
//
#define MSG_CHK_UNHANDLED_INVALID_NAME   0x000013B3L

//
// MessageId: MSG_CHK_INVALID_NAME_CORRECTED
//
// MessageText:
//
//  Corrected name %1 in folder %2.
//
#define MSG_CHK_INVALID_NAME_CORRECTED   0x000013B4L

//
// MessageId: MSG_RECOV_BYTES_RECOVERED
//
// MessageText:
//
//  
//  %1 of %2 bytes recovered.
//
#define MSG_RECOV_BYTES_RECOVERED        0x00003A9EL

//
// MessageId: MSG_CHK_NTFS_BAD_SECTORS_REPORT_IN_KB
//
// MessageText:
//
//  %1 KB in bad sectors.
//
#define MSG_CHK_NTFS_BAD_SECTORS_REPORT_IN_KB 0x000065B5L

//
// MessageId: MSG_CHK_NTFS_CORRECTING_ERROR_IN_DIRECTORY
//
// MessageText:
//
//  Correcting error in directory %1
//
#define MSG_CHK_NTFS_CORRECTING_ERROR_IN_DIRECTORY 0x000065BFL

//---------------
//
// Common messages.
//
//---------------
//
// MessageId: MSG_UTILS_HELP
//
// MessageText:
//
//  There is no help for this utility.
//
#define MSG_UTILS_HELP                   0x00007530L

//
// MessageId: MSG_UTILS_ERROR_FATAL
//
// MessageText:
//
//  Critical error encountered.
//
#define MSG_UTILS_ERROR_FATAL            0x00007531L

//
// MessageId: MSG_UTILS_ERROR_INVALID_VERSION
//
// MessageText:
//
//  Incorrect Windows 2000 version
//
#define MSG_UTILS_ERROR_INVALID_VERSION  0x00007532L

//-------------------------------------
//
// Messages for FAT and NTFS boot code
//
//-------------------------------------
//
// MessageId: MSG_BOOT_FAT_NTLDR_MISSING
//
// MessageText:
//
//  NTLDR is missing%0
//
#define MSG_BOOT_FAT_NTLDR_MISSING       0x00007756L

//
// MessageId: MSG_BOOT_FAT_IO_ERROR
//
// MessageText:
//
//  Disk error%0
//
#define MSG_BOOT_FAT_IO_ERROR            0x00007757L

//
// MessageId: MSG_BOOT_FAT_PRESS_KEY
//
// MessageText:
//
//  Press any key to restart%0
//
#define MSG_BOOT_FAT_PRESS_KEY           0x00007758L

//
// MessageId: MSG_BOOT_NTFS_NTLDR_MISSING
//
// MessageText:
//
//  NTLDR is missing%0
//
#define MSG_BOOT_NTFS_NTLDR_MISSING      0x00007759L

//
// MessageId: MSG_BOOT_NTFS_NTLDR_COMPRESSED
//
// MessageText:
//
//  NTLDR is compressed%0
//
#define MSG_BOOT_NTFS_NTLDR_COMPRESSED   0x0000775AL

//
// MessageId: MSG_BOOT_NTFS_IO_ERROR
//
// MessageText:
//
//  A disk read error occurred%0
//
#define MSG_BOOT_NTFS_IO_ERROR           0x0000775BL

//
// MessageId: MSG_BOOT_NTFS_PRESS_KEY
//
// MessageText:
//
//  Press Ctrl+Alt+Del to restart%0
//
#define MSG_BOOT_NTFS_PRESS_KEY          0x0000775CL

#define MSG_CHK_BAD_BACKUP_BS            0x0000775DL


