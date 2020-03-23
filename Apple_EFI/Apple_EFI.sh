#!/bin/bash
function echob() {
	echo $(tput bold)"$1"$(tput sgr0)
}
# STLVNUB 31/10/2013
set -e
declare -r CMD=$([[ $0 == /* ]] && echo "$0" || echo "${PWD}/${0#./}")
declare -r Apple_EFI_Builder_Script=$(readlink "$CMD" || echo "$CMD")
declare -r workDIR="${Apple_EFI_Builder_Script%/*}"
dumpDIR="$workDIR"/Uncompressed_Dump
efiFile="$workDIR"/Files/AppleEfiList.txt
cd "$workDIR"
[ ! -d "$dumpDIR" ] && echob "cp Uncompressed_Dump folder here First!!" && exit 1 
fileTypes='APP DRV PEI SEC PEICORE DXECORE'
for a in $fileTypes; do
	[ ! -d Efi/$a ] && mkdir -p Efi/$a
done	
getTypes(){
	theCheck=
	theName=$1
	shift
	theType=$1
	shift
	theGuid=$1
	theCheck="${theGuid:0:24}"
	cd "$dumpDIR"
	theFile="${theGuid:0:2}*.MOD"
	if [ -f "${theCheck}"*.MOD ]; then
		theFileCount=$(ls "${theCheck}"*.MOD | wc -l)
	fi	
	#echo $theFileCount
	#return	
	if [ -f "$dumpDIR/$theGuid.MOD" ]; then
		echob "cp $theGuid.MOD ( $theType ) to $theName"
		cp -R "$dumpDIR/$theGuid.MOD" "$workDIR"/Efi/$theType/$theName
		echo  "COPIED $theName $theType $theGuid.MOD" >> "$workDIR"/FoundLog.txt
	elif [ -f "$dumpDIR"/$theCheck*.MOD ]; then
		 cp -R "$dumpDIR"/$theCheck*.MOD "$workDIR"/Efi/$theType/$theName
		 echo  "FIXED $theName $theType $theCheck*.MOD" >> "$workDIR"/FixedLog.txt
	else
	     echo  "SKIPPED $theName $theType $theGuid" >> "$workDIR"/SkippedLog.txt
	fi	
}
echo $(date) > "$workDIR"/FoundLog.txt
echo $(date) > "$workDIR"/SkippedLog.txt
echo $(date) > "$workDIR"/FixedLog.txt
echob "This script compares known modules in Files/AppleEfiList.txt"
echob "To a PhoenixTools Uncompressed_Dump folder"
echob "and renames found Guid's to known module names"	
while read line ; do
	getTypes $line
done < "$efiFile"
