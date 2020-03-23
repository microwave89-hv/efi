#
# Copyright (c) 1999, 2000
# Intel Corporation.
# All rights reserved.
# 
# Redistribution and use in source and binary forms, with or without modification,
# are permitted provided that the following conditions are met:
# 
# 1. Redistributions of source code must retain the above copyright notice,
#    this list of conditions and the following disclaimer.
# 
# 2. Redistributions in binary form must reproduce the above copyright notice,
#    this list of conditions and the following disclaimer in the documentation
#    and/or other materials provided with the distribution.
# 
# 3. All advertising materials mentioning features or use of this software must
#    display the following acknowledgement:
# 
#    This product includes software developed by Intel Corporation and its
#    contributors.
# 
# 4. Neither the name of Intel Corporation or its contributors may be used to
#    endorse or promote products derived from this software without specific
#    prior written permission.
# 
# THIS SOFTWARE IS PROVIDED BY INTEL CORPORATION AND CONTRIBUTORS ``AS IS'' AND
# ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED
# WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE
# DISCLAIMED.  IN NO EVENT SHALL INTEL CORPORATION OR CONTRIBUTORS BE LIABLE FOR
# ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES
# (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES;
# LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON
# ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT
# (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS
# SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
# 

####################################
#  Common inference rules
#
CC_LINE = $(CC) $(C_FLAGS) $(MODULE_CFLAGS) /c $< /Fo$@ /FR$(@R)

{$(SOURCE_DIR)}.c{$(DEST_DIR)}.obj:
	$(CC_LINE)

{$(SOURCE_DIR)}.cxx{$(DEST_DIR)}.obj:
	$(CC_LINE)

####################################
#
#  The following will force library targets to be out of date forcing their
#  makefiles to be invoked.  This will always lead to relinking with the
#  library even if the make did not produce a new binary.
#
!IFDEF FORCE_LIB_CHECK
FORCE_LIB = force
!ENDIF

force:

####################################
# Library targes
#

!IFDEF TARGET_LIB
TARGET_LIB = $(BIN_DIR)\$(TARGET_LIB).lib
BIN_TARGETS = $(BIN_TARGETS) $(TARGET_LIB)
$(TARGET_LIB) : $(OBJECTS)
    $(LIB) $(LIB_FLAGS) $** /OUT:$(TARGET_LIB)
!ENDIF

####################################
# Application targes
#

!IFDEF TARGET_APP
TARGET_APP = $(BIN_DIR)\$(TARGET_APP).efi
BIN_TARGETS = $(BIN_TARGETS) $(TARGET_APP)
$(TARGET_APP) : $(OBJECTS) $(LIBS)
    $(LINK) $(LINK_FLAGS_DLL) /ENTRY:$(IMAGE_ENTRY_POINT) $** /OUT:$(@R).dll
    $(FWIMAGE) app $(@R).dll $(TARGET_APP)
!ENDIF

####################################
# Boot service driver targes
#

!IFDEF TARGET_BS_DRIVER
TARGET_DRIVER = $(BIN_DIR)\$(TARGET_BS_DRIVER).efi
BIN_TARGETS = $(BIN_TARGETS) $(TARGET_DRIVER)
$(TARGET_DRIVER) : $(OBJECTS) $(LIBS)
    $(LINK) $(LINK_FLAGS_DLL) /ENTRY:$(IMAGE_ENTRY_POINT) $** /OUT:$(@R).dll
    $(FWIMAGE) bsdrv $(@R).dll $(TARGET_DRIVER)
!ENDIF

####################################
# Runtime service drivers
#

!IFDEF TARGET_RT_DRIVER
TARGET_DRIVER = $(BIN_DIR)\$(TARGET_RT_DRIVER).efi
BIN_TARGETS = $(OBJECTS) $(TARGET_DRIVER)
$(TARGET_DRIVER) : $(OBJECTS) $(LIBS)
    $(LINK) $(LINK_FLAGS_DLL) /ENTRY:$(IMAGE_ENTRY_POINT) $** /OUT:$(@R).dll
    $(FWIMAGE) rtdrv $(@R).dll $(TARGET_DRIVER)
!ENDIF

####################################
# Common targes
#
all : $(BIN_TARGETS)

clean :
    - rd  /s /q $(DEST_DIR)
    - del $(BIN_DIR)\$(BASE_NAME).*
