#----------------------------------------------------------------
# Apple Shmoo Tool Script
#    Author: Xiaohe Chen
#    2009 Apple Inc all rights reserved
#----------------------------------------------------------------
import array
import datetime
import os
import string
#----------------------------------------------------------------
"""Command to run shmoo"""
#----------------------------------------------------------------
cmd = '/usr/sbin/bless --mount / --file /Volumes/DIAG/boot.efi --setBoot --nextonly'
os.system(cmd)
cmd = 'shutdown -r now'
os.system(cmd)
#----------------------------------------------------------------
# End of File
#----------------------------------------------------------------