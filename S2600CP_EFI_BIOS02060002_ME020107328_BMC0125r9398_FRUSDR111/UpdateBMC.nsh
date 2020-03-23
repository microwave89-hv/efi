echo -off
cls
echo ""
echo Integrated BMC Firmware Update Package 01.25
echo The BMC image being installed is revision 01.25.9398
echo ""

# Update everything including the boot block
FWPIAUPD -u -bin -ni -b -o -pia -nopc -if=usb BMC_i_0125r9398.bin
