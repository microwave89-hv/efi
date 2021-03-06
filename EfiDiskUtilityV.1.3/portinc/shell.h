/*
 * Copyright (c) 2008
 * Intel Corporation.
 * All rights reserved.
 * 
 * Redistribution and use in source and binary forms, with or without modification,
 * are permitted provided that the following conditions are met:
 * 
 * 1. Redistributions of source code must retain the above copyright notice,
 *    this list of conditions and the following disclaimer.
 * 
 * 2. Redistributions in binary form must reproduce the above copyright notice,
 *    this list of conditions and the following disclaimer in the documentation
 *    and/or other materials provided with the distribution.
 * 
 * 3. All advertising materials mentioning features or use of this software must
 *    display the following acknowledgement:
 * 
 *    This product includes software developed by Intel Corporation and its
 *    contributors.
 * 
 * 4. Neither the name of Intel Corporation or its contributors may be used to
 *    endorse or promote products derived from this software without specific
 *    prior written permission.
 * 
 * THIS SOFTWARE IS PROVIDED BY INTEL CORPORATION AND CONTRIBUTORS ``AS IS'' AND
 * ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED
 * WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE
 * DISCLAIMED.  IN NO EVENT SHALL INTEL CORPORATION OR CONTRIBUTORS BE LIABLE FOR
 * ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES
 * (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES;
 * LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON
 * ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT
 * (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS
 * SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
 *
 */
#ifndef _EFI_DISK_UTILITIES_SHELL_H_
#define _EFI_DISK_UTILITIES_SHELL_H_

#include "EfiShelllib.h"

#define D_INFO     EFI_D_INFO
#define D_ERROR    EFI_D_ERROR

#define EFI_DEVICE_PATH EFI_DEVICE_PATH_PROTOCOL
#define EFI_BLOCK_IO EFI_BLOCK_IO_PROTOCOL
#define EFI_DISK_IO EFI_DISK_IO_PROTOCOL
#define EFI_LOADED_IMAGE  EFI_LOADED_IMAGE_PROTOCOL

#define BLOCK_IO_PROTOCOL EFI_BLOCK_IO_PROTOCOL_GUID
#define DISK_IO_PROTOCOL EFI_DISK_IO_PROTOCOL_GUID
#define EFI_BLOCK_IO  EFI_BLOCK_IO_PROTOCOL

#define DevicePathToStr  LibDevicePathToStr

#define LoadedImageProtocol gEfiLoadedImageProtocolGuid
#define DevicePathProtocol  gEfiDevicePathProtocolGuid
#define BlockIoProtocol  gEfiBlockIoProtocolGuid
#define DiskIoProtocol gEfiDiskIoProtocolGuid
#define InitializeLib(a,b) EFI_SHELL_APP_INIT((a),(b))

#endif
