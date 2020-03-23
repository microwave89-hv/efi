#
# Tpm20.py
#
# Copyright (C) 2015 efipy.core@gmail.com All rights reserved.
#
# Tpm20.py is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, version 2 of the License.
#
# EfiPy is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with EfiPy.  If not, see <http://www.gnu.org/licenses/>.
#

from EfiPy.MdePkg.IndustryStandard    import *

import Tpm12

SHA1_DIGEST_SIZE = 20
SHA1_BLOCK_SIZE  = 64

SHA256_DIGEST_SIZE = 32
SHA256_BLOCK_SIZE  = 64

SHA384_DIGEST_SIZE = 48
SHA384_BLOCK_SIZE  = 128

SHA512_DIGEST_SIZE = 64
SHA512_BLOCK_SIZE  = 128

SM3_256_DIGEST_SIZE = 32
SM3_256_BLOCK_SIZE  = 64

MAX_SESSION_NUMBER = 3

YES   = 1
NO    = 0
SET   = 1
CLEAR = 0

MAX_RSA_KEY_BITS  = 2048
MAX_RSA_KEY_BYTES = ((MAX_RSA_KEY_BITS + 7) / 8)

MAX_ECC_KEY_BITS  = 256
MAX_ECC_KEY_BYTES = ((MAX_ECC_KEY_BITS + 7) / 8)

MAX_AES_KEY_BITS         = 128
MAX_AES_BLOCK_SIZE_BYTES = 16
MAX_AES_KEY_BYTES        = ((MAX_AES_KEY_BITS + 7) / 8)

MAX_SM4_KEY_BITS         = 128
MAX_SM4_BLOCK_SIZE_BYTES = 16
MAX_SM4_KEY_BYTES        = ((MAX_SM4_KEY_BITS + 7) / 8)

MAX_SYM_KEY_BITS   = MAX_AES_KEY_BITS
MAX_SYM_KEY_BYTES  = MAX_AES_KEY_BYTES
MAX_SYM_BLOCK_SIZE = MAX_AES_BLOCK_SIZE_BYTES

BSIZE                         = UINT16
BUFFER_ALIGNMENT              = 4
IMPLEMENTATION_PCR            = 24
PLATFORM_PCR                  = 24
DRTM_PCR                      = 17
NUM_LOCALITIES                = 5
MAX_HANDLE_NUM                = 3
MAX_ACTIVE_SESSIONS           = 64
CONTEXT_SLOT                  = UINT16
CONTEXT_COUNTER               = UINT64
MAX_LOADED_SESSIONS           = 3
MAX_SESSION_NUM               = 3
MAX_LOADED_OBJECTS            = 3
MIN_EVICT_OBJECTS             = 2
PCR_SELECT_MIN                = ((PLATFORM_PCR + 7) / 8)
PCR_SELECT_MAX                = ((IMPLEMENTATION_PCR + 7) / 8)
NUM_POLICY_PCR_GROUP          = 1
NUM_AUTHVALUE_PCR_GROUP       = 1
MAX_CONTEXT_SIZE              = 4000
MAX_DIGEST_BUFFER             = 1024
MAX_NV_INDEX_SIZE             = 1024
MAX_CAP_BUFFER                = 1024
NV_MEMORY_SIZE                = 16384
NUM_STATIC_PCR                = 16
MAX_ALG_LIST_SIZE             = 64
TIMER_PRESCALE                = 100000
PRIMARY_SEED_SIZE             = 32

TPM_ALG_ID                    = UINT16
TPM_ALG_AES                   = TPM_ALG_ID(0x0006).value
CONTEXT_ENCRYPT_ALG           = TPM_ALG_AES

CONTEXT_ENCRYPT_KEY_BITS      = MAX_SYM_KEY_BITS
CONTEXT_ENCRYPT_KEY_BYTES     = ((CONTEXT_ENCRYPT_KEY_BITS + 7) / 8)

TPM_ALG_SHA256                = TPM_ALG_ID(0x000B).value
CONTEXT_INTEGRITY_HASH_ALG    = TPM_ALG_SHA256

CONTEXT_INTEGRITY_HASH_SIZE   = SHA256_DIGEST_SIZE
PROOF_SIZE                    = CONTEXT_INTEGRITY_HASH_SIZE
NV_CLOCK_UPDATE_INTERVAL      = 12
NUM_POLICY_PCR                = 1
MAX_COMMAND_SIZE              = 4096
MAX_RESPONSE_SIZE             = 4096
ORDERLY_BITS                  = 8
MAX_ORDERLY_COUNT             = ((1 << ORDERLY_BITS) - 1)

TPM_ALG_FIRST                 = TPM_ALG_ID(0x0001).value
ALG_ID_FIRST                  = TPM_ALG_FIRST


TPM_ALG_LAST                  = TPM_ALG_ID(0x0044).value
ALG_ID_LAST                   = TPM_ALG_LAST

MAX_SYM_DATA                  = 128
MAX_RNG_ENTROPY_SIZE          = 64
RAM_INDEX_SPACE               = 512
RSA_DEFAULT_PUBLIC_EXPONENT   = 0x00010001
CRT_FORMAT_RSA                = YES
PRIVATE_VENDOR_SPECIFIC_BYTES = ((MAX_RSA_KEY_BYTES / 2) * ( 3 + CRT_FORMAT_RSA * 2))

TPM_CAP            = UINT32

MAX_CAP_DATA       = (MAX_CAP_BUFFER - sizeof(TPM_CAP) - sizeof(UINT32))

# MAX_CAP_ALGS       = (MAX_CAP_DATA / sizeof(TPMS_ALG_PROPERTY))

MAX_CAP_HANDLES    = (MAX_CAP_DATA / sizeof(Tpm12.TPM_HANDLE))

TPM_CC             = UINT32
MAX_CAP_CC         = (MAX_CAP_DATA / sizeof(TPM_CC))


# MAX_TPM_PROPERTIES = (MAX_CAP_DATA / sizeof(TPMS_TAGGED_PROPERTY))


# MAX_PCR_PROPERTIES = (MAX_CAP_DATA / sizeof(TPMS_TAGGED_PCR_SELECT))

TPM_ECC_CURVE      = UINT16
MAX_ECC_CURVES     = (MAX_CAP_DATA / sizeof(TPM_ECC_CURVE))

HASH_COUNT = 5

BYTE = UINT8
BOOL = UINT8
TPM_AUTHORIZATION_SIZE  = UINT32
TPM_PARAMETER_SIZE      = UINT32
TPM_KEY_SIZE            = UINT16
TPM_KEY_BITS            = UINT16

TPM_GENERATED           = UINT32
TPM_GENERATED_VALUE     = TPM_GENERATED(0xff544347).value

# TPM_ALG_ID              = UINT16

TPM_ALG_ERROR          = TPM_ALG_ID(0x0000).value

# TPM_ALG_FIRST          = TPM_ALG_ID(0x0001).value

TPM_ALG_SHA1           = TPM_ALG_ID(0x0004).value
# TPM_ALG_AES            = TPM_ALG_ID(0x0006).value


TPM_ALG_KEYEDHASH      = TPM_ALG_ID(0x0008).value

# TPM_ALG_SHA256         = TPM_ALG_ID(0x000B).value

TPM_ALG_SHA384         = TPM_ALG_ID(0x000C).value
TPM_ALG_SHA512         = TPM_ALG_ID(0x000D).value
TPM_ALG_NULL           = TPM_ALG_ID(0x0010).value
TPM_ALG_SM3_256        = TPM_ALG_ID(0x0012).value
TPM_ALG_SM4            = TPM_ALG_ID(0x0013).value
TPM_ALG_RSASSA         = TPM_ALG_ID(0x0014).value
TPM_ALG_RSAES          = TPM_ALG_ID(0x0015).value
TPM_ALG_RSAPSS         = TPM_ALG_ID(0x0016).value
TPM_ALG_OAEP           = TPM_ALG_ID(0x0017).value
TPM_ALG_ECDSA          = TPM_ALG_ID(0x0018).value
TPM_ALG_ECDH           = TPM_ALG_ID(0x0019).value
TPM_ALG_ECDAA          = TPM_ALG_ID(0x001A).value
TPM_ALG_SM2            = TPM_ALG_ID(0x001B).value
TPM_ALG_ECSCHNORR      = TPM_ALG_ID(0x001C).value
TPM_ALG_ECMQV          = TPM_ALG_ID(0x001D).value
TPM_ALG_KDF1_SP800_56a = TPM_ALG_ID(0x0020).value
TPM_ALG_KDF2           = TPM_ALG_ID(0x0021).value
TPM_ALG_KDF1_SP800_108 = TPM_ALG_ID(0x0022).value
TPM_ALG_ECC            = TPM_ALG_ID(0x0023).value
TPM_ALG_SYMCIPHER      = TPM_ALG_ID(0x0025).value
TPM_ALG_CTR            = TPM_ALG_ID(0x0040).value
TPM_ALG_OFB            = TPM_ALG_ID(0x0041).value
TPM_ALG_CBC            = TPM_ALG_ID(0x0042).value
TPM_ALG_CFB            = TPM_ALG_ID(0x0043).value
TPM_ALG_ECB            = TPM_ALG_ID(0x0044).value

# TPM_ALG_LAST           = TPM_ALG_ID(0x0044).value


# TPM_ECC_CURVE     = UINT16

TPM_ECC_NONE      = TPM_ECC_CURVE(0x0000).value
TPM_ECC_NIST_P192 = TPM_ECC_CURVE(0x0001).value
TPM_ECC_NIST_P224 = TPM_ECC_CURVE(0x0002).value
TPM_ECC_NIST_P256 = TPM_ECC_CURVE(0x0003).value
TPM_ECC_NIST_P384 = TPM_ECC_CURVE(0x0004).value
TPM_ECC_NIST_P521 = TPM_ECC_CURVE(0x0005).value
TPM_ECC_BN_P256   = TPM_ECC_CURVE(0x0010).value
TPM_ECC_BN_P638   = TPM_ECC_CURVE(0x0011).value
TPM_ECC_SM2_P256  = TPM_ECC_CURVE(0x0020).value


# TPM_CC                            = UINT32

TPM_CC_FIRST                      = TPM_CC(0x0000011F).value
TPM_CC_PP_FIRST                   = TPM_CC(0x0000011F).value
TPM_CC_NV_UndefineSpaceSpecial    = TPM_CC(0x0000011F).value
TPM_CC_EvictControl               = TPM_CC(0x00000120).value
TPM_CC_HierarchyControl           = TPM_CC(0x00000121).value
TPM_CC_NV_UndefineSpace           = TPM_CC(0x00000122).value
TPM_CC_ChangeEPS                  = TPM_CC(0x00000124).value
TPM_CC_ChangePPS                  = TPM_CC(0x00000125).value
TPM_CC_Clear                      = TPM_CC(0x00000126).value
TPM_CC_ClearControl               = TPM_CC(0x00000127).value
TPM_CC_ClockSet                   = TPM_CC(0x00000128).value
TPM_CC_HierarchyChangeAuth        = TPM_CC(0x00000129).value
TPM_CC_NV_DefineSpace             = TPM_CC(0x0000012A).value
TPM_CC_PCR_Allocate               = TPM_CC(0x0000012B).value
TPM_CC_PCR_SetAuthPolicy          = TPM_CC(0x0000012C).value
TPM_CC_PP_Commands                = TPM_CC(0x0000012D).value
TPM_CC_SetPrimaryPolicy           = TPM_CC(0x0000012E).value
TPM_CC_FieldUpgradeStart          = TPM_CC(0x0000012F).value
TPM_CC_ClockRateAdjust            = TPM_CC(0x00000130).value
TPM_CC_CreatePrimary              = TPM_CC(0x00000131).value
TPM_CC_NV_GlobalWriteLock         = TPM_CC(0x00000132).value
TPM_CC_PP_LAST                    = TPM_CC(0x00000132).value
TPM_CC_GetCommandAuditDigest      = TPM_CC(0x00000133).value
TPM_CC_NV_Increment               = TPM_CC(0x00000134).value
TPM_CC_NV_SetBits                 = TPM_CC(0x00000135).value
TPM_CC_NV_Extend                  = TPM_CC(0x00000136).value
TPM_CC_NV_Write                   = TPM_CC(0x00000137).value
TPM_CC_NV_WriteLock               = TPM_CC(0x00000138).value
TPM_CC_DictionaryAttackLockReset  = TPM_CC(0x00000139).value
TPM_CC_DictionaryAttackParameters = TPM_CC(0x0000013A).value
TPM_CC_NV_ChangeAuth              = TPM_CC(0x0000013B).value
TPM_CC_PCR_Event                  = TPM_CC(0x0000013C).value
TPM_CC_PCR_Reset                  = TPM_CC(0x0000013D).value
TPM_CC_SequenceComplete           = TPM_CC(0x0000013E).value
TPM_CC_SetAlgorithmSet            = TPM_CC(0x0000013F).value
TPM_CC_SetCommandCodeAuditStatus  = TPM_CC(0x00000140).value
TPM_CC_FieldUpgradeData           = TPM_CC(0x00000141).value
TPM_CC_IncrementalSelfTest        = TPM_CC(0x00000142).value
TPM_CC_SelfTest                   = TPM_CC(0x00000143).value
TPM_CC_Startup                    = TPM_CC(0x00000144).value
TPM_CC_Shutdown                   = TPM_CC(0x00000145).value
TPM_CC_StirRandom                 = TPM_CC(0x00000146).value
TPM_CC_ActivateCredential         = TPM_CC(0x00000147).value
TPM_CC_Certify                    = TPM_CC(0x00000148).value
TPM_CC_PolicyNV                   = TPM_CC(0x00000149).value
TPM_CC_CertifyCreation            = TPM_CC(0x0000014A).value
TPM_CC_Duplicate                  = TPM_CC(0x0000014B).value
TPM_CC_GetTime                    = TPM_CC(0x0000014C).value
TPM_CC_GetSessionAuditDigest      = TPM_CC(0x0000014D).value
TPM_CC_NV_Read                    = TPM_CC(0x0000014E).value
TPM_CC_NV_ReadLock                = TPM_CC(0x0000014F).value
TPM_CC_ObjectChangeAuth           = TPM_CC(0x00000150).value
TPM_CC_PolicySecret               = TPM_CC(0x00000151).value
TPM_CC_Rewrap                     = TPM_CC(0x00000152).value
TPM_CC_Create                     = TPM_CC(0x00000153).value
TPM_CC_ECDH_ZGen                  = TPM_CC(0x00000154).value
TPM_CC_HMAC                       = TPM_CC(0x00000155).value
TPM_CC_Import                     = TPM_CC(0x00000156).value
TPM_CC_Load                       = TPM_CC(0x00000157).value
TPM_CC_Quote                      = TPM_CC(0x00000158).value
TPM_CC_RSA_Decrypt                = TPM_CC(0x00000159).value
TPM_CC_HMAC_Start                 = TPM_CC(0x0000015B).value
TPM_CC_SequenceUpdate             = TPM_CC(0x0000015C).value
TPM_CC_Sign                       = TPM_CC(0x0000015D).value
TPM_CC_Unseal                     = TPM_CC(0x0000015E).value
TPM_CC_PolicySigned               = TPM_CC(0x00000160).value
TPM_CC_ContextLoad                = TPM_CC(0x00000161).value
TPM_CC_ContextSave                = TPM_CC(0x00000162).value
TPM_CC_ECDH_KeyGen                = TPM_CC(0x00000163).value
TPM_CC_EncryptDecrypt             = TPM_CC(0x00000164).value
TPM_CC_FlushContext               = TPM_CC(0x00000165).value
TPM_CC_LoadExternal               = TPM_CC(0x00000167).value
TPM_CC_MakeCredential             = TPM_CC(0x00000168).value
TPM_CC_NV_ReadPublic              = TPM_CC(0x00000169).value
TPM_CC_PolicyAuthorize            = TPM_CC(0x0000016A).value
TPM_CC_PolicyAuthValue            = TPM_CC(0x0000016B).value
TPM_CC_PolicyCommandCode          = TPM_CC(0x0000016C).value
TPM_CC_PolicyCounterTimer         = TPM_CC(0x0000016D).value
TPM_CC_PolicyCpHash               = TPM_CC(0x0000016E).value
TPM_CC_PolicyLocality             = TPM_CC(0x0000016F).value
TPM_CC_PolicyNameHash             = TPM_CC(0x00000170).value
TPM_CC_PolicyOR                   = TPM_CC(0x00000171).value
TPM_CC_PolicyTicket               = TPM_CC(0x00000172).value
TPM_CC_ReadPublic                 = TPM_CC(0x00000173).value
TPM_CC_RSA_Encrypt                = TPM_CC(0x00000174).value
TPM_CC_StartAuthSession           = TPM_CC(0x00000176).value
TPM_CC_VerifySignature            = TPM_CC(0x00000177).value
TPM_CC_ECC_Parameters             = TPM_CC(0x00000178).value
TPM_CC_FirmwareRead               = TPM_CC(0x00000179).value
TPM_CC_GetCapability              = TPM_CC(0x0000017A).value
TPM_CC_GetRandom                  = TPM_CC(0x0000017B).value
TPM_CC_GetTestResult              = TPM_CC(0x0000017C).value
TPM_CC_Hash                       = TPM_CC(0x0000017D).value
TPM_CC_PCR_Read                   = TPM_CC(0x0000017E).value
TPM_CC_PolicyPCR                  = TPM_CC(0x0000017F).value
TPM_CC_PolicyRestart              = TPM_CC(0x00000180).value
TPM_CC_ReadClock                  = TPM_CC(0x00000181).value
TPM_CC_PCR_Extend                 = TPM_CC(0x00000182).value
TPM_CC_PCR_SetAuthValue           = TPM_CC(0x00000183).value
TPM_CC_NV_Certify                 = TPM_CC(0x00000184).value
TPM_CC_EventSequenceComplete      = TPM_CC(0x00000185).value
TPM_CC_HashSequenceStart          = TPM_CC(0x00000186).value
TPM_CC_PolicyPhysicalPresence     = TPM_CC(0x00000187).value
TPM_CC_PolicyDuplicationSelect    = TPM_CC(0x00000188).value
TPM_CC_PolicyGetDigest            = TPM_CC(0x00000189).value
TPM_CC_TestParms                  = TPM_CC(0x0000018A).value
TPM_CC_Commit                     = TPM_CC(0x0000018B).value
TPM_CC_PolicyPassword             = TPM_CC(0x0000018C).value
TPM_CC_ZGen_2Phase                = TPM_CC(0x0000018D).value
TPM_CC_EC_Ephemeral               = TPM_CC(0x0000018E).value
TPM_CC_LAST                       = TPM_CC(0x0000018E).value

TPM_RC                   = UINT32
TPM_RC_SUCCESS           = TPM_RC(0x000).value
TPM_RC_BAD_TAG           = TPM_RC(0x030).value
RC_VER1                  = TPM_RC(0x100).value
TPM_RC_INITIALIZE        = TPM_RC(RC_VER1 + 0x000).value
TPM_RC_FAILURE           = TPM_RC(RC_VER1 + 0x001).value
TPM_RC_SEQUENCE          = TPM_RC(RC_VER1 + 0x003).value
TPM_RC_PRIVATE           = TPM_RC(RC_VER1 + 0x00B).value
TPM_RC_HMAC              = TPM_RC(RC_VER1 + 0x019).value
TPM_RC_DISABLED          = TPM_RC(RC_VER1 + 0x020).value
TPM_RC_EXCLUSIVE         = TPM_RC(RC_VER1 + 0x021).value
TPM_RC_AUTH_TYPE         = TPM_RC(RC_VER1 + 0x024).value
TPM_RC_AUTH_MISSING      = TPM_RC(RC_VER1 + 0x025).value
TPM_RC_POLICY            = TPM_RC(RC_VER1 + 0x026).value
TPM_RC_PCR               = TPM_RC(RC_VER1 + 0x027).value
TPM_RC_PCR_CHANGED       = TPM_RC(RC_VER1 + 0x028).value
TPM_RC_UPGRADE           = TPM_RC(RC_VER1 + 0x02D).value
TPM_RC_TOO_MANY_CONTEXTS = TPM_RC(RC_VER1 + 0x02E).value
TPM_RC_AUTH_UNAVAILABLE  = TPM_RC(RC_VER1 + 0x02F).value
TPM_RC_REBOOT            = TPM_RC(RC_VER1 + 0x030).value
TPM_RC_UNBALANCED        = TPM_RC(RC_VER1 + 0x031).value
TPM_RC_COMMAND_SIZE      = TPM_RC(RC_VER1 + 0x042).value
TPM_RC_COMMAND_CODE      = TPM_RC(RC_VER1 + 0x043).value
TPM_RC_AUTHSIZE          = TPM_RC(RC_VER1 + 0x044).value
TPM_RC_AUTH_CONTEXT      = TPM_RC(RC_VER1 + 0x045).value
TPM_RC_NV_RANGE          = TPM_RC(RC_VER1 + 0x046).value
TPM_RC_NV_SIZE           = TPM_RC(RC_VER1 + 0x047).value
TPM_RC_NV_LOCKED         = TPM_RC(RC_VER1 + 0x048).value
TPM_RC_NV_AUTHORIZATION  = TPM_RC(RC_VER1 + 0x049).value
TPM_RC_NV_UNINITIALIZED  = TPM_RC(RC_VER1 + 0x04A).value
TPM_RC_NV_SPACE          = TPM_RC(RC_VER1 + 0x04B).value
TPM_RC_NV_DEFINED        = TPM_RC(RC_VER1 + 0x04C).value
TPM_RC_BAD_CONTEXT       = TPM_RC(RC_VER1 + 0x050).value
TPM_RC_CPHASH            = TPM_RC(RC_VER1 + 0x051).value
TPM_RC_PARENT            = TPM_RC(RC_VER1 + 0x052).value
TPM_RC_NEEDS_TEST        = TPM_RC(RC_VER1 + 0x053).value
TPM_RC_NO_RESULT         = TPM_RC(RC_VER1 + 0x054).value
TPM_RC_SENSITIVE         = TPM_RC(RC_VER1 + 0x055).value
RC_MAX_FM0               = TPM_RC(RC_VER1 + 0x07F).value
RC_FMT1                  = TPM_RC(0x080).value
TPM_RC_ASYMMETRIC        = TPM_RC(RC_FMT1 + 0x001).value
TPM_RC_ATTRIBUTES        = TPM_RC(RC_FMT1 + 0x002).value
TPM_RC_HASH              = TPM_RC(RC_FMT1 + 0x003).value
TPM_RC_VALUE             = TPM_RC(RC_FMT1 + 0x004).value
TPM_RC_HIERARCHY         = TPM_RC(RC_FMT1 + 0x005).value
TPM_RC_KEY_SIZE          = TPM_RC(RC_FMT1 + 0x007).value
TPM_RC_MGF               = TPM_RC(RC_FMT1 + 0x008).value
TPM_RC_MODE              = TPM_RC(RC_FMT1 + 0x009).value
TPM_RC_TYPE              = TPM_RC(RC_FMT1 + 0x00A).value
TPM_RC_HANDLE            = TPM_RC(RC_FMT1 + 0x00B).value
TPM_RC_KDF               = TPM_RC(RC_FMT1 + 0x00C).value
TPM_RC_RANGE             = TPM_RC(RC_FMT1 + 0x00D).value
TPM_RC_AUTH_FAIL         = TPM_RC(RC_FMT1 + 0x00E).value
TPM_RC_NONCE             = TPM_RC(RC_FMT1 + 0x00F).value
TPM_RC_PP                = TPM_RC(RC_FMT1 + 0x010).value
TPM_RC_SCHEME            = TPM_RC(RC_FMT1 + 0x012).value
TPM_RC_SIZE              = TPM_RC(RC_FMT1 + 0x015).value
TPM_RC_SYMMETRIC         = TPM_RC(RC_FMT1 + 0x016).value
TPM_RC_TAG               = TPM_RC(RC_FMT1 + 0x017).value
TPM_RC_SELECTOR          = TPM_RC(RC_FMT1 + 0x018).value
TPM_RC_INSUFFICIENT      = TPM_RC(RC_FMT1 + 0x01A).value
TPM_RC_SIGNATURE         = TPM_RC(RC_FMT1 + 0x01B).value
TPM_RC_KEY               = TPM_RC(RC_FMT1 + 0x01C).value
TPM_RC_POLICY_FAIL       = TPM_RC(RC_FMT1 + 0x01D).value
TPM_RC_INTEGRITY         = TPM_RC(RC_FMT1 + 0x01F).value
TPM_RC_TICKET            = TPM_RC(RC_FMT1 + 0x020).value
TPM_RC_RESERVED_BITS     = TPM_RC(RC_FMT1 + 0x021).value
TPM_RC_BAD_AUTH          = TPM_RC(RC_FMT1 + 0x022).value
TPM_RC_EXPIRED           = TPM_RC(RC_FMT1 + 0x023).value
TPM_RC_POLICY_CC         = TPM_RC(RC_FMT1 + 0x024 ).value
TPM_RC_BINDING           = TPM_RC(RC_FMT1 + 0x025).value
TPM_RC_CURVE             = TPM_RC(RC_FMT1 + 0x026).value
TPM_RC_ECC_POINT         = TPM_RC(RC_FMT1 + 0x027).value
RC_WARN                  = TPM_RC(0x900).value
TPM_RC_CONTEXT_GAP       = TPM_RC(RC_WARN + 0x001).value
TPM_RC_OBJECT_MEMORY     = TPM_RC(RC_WARN + 0x002).value
TPM_RC_SESSION_MEMORY    = TPM_RC(RC_WARN + 0x003).value
TPM_RC_MEMORY            = TPM_RC(RC_WARN + 0x004).value
TPM_RC_SESSION_HANDLES   = TPM_RC(RC_WARN + 0x005).value
TPM_RC_OBJECT_HANDLES    = TPM_RC(RC_WARN + 0x006).value
TPM_RC_LOCALITY          = TPM_RC(RC_WARN + 0x007).value
TPM_RC_YIELDED           = TPM_RC(RC_WARN + 0x008).value
TPM_RC_CANCELED          = TPM_RC(RC_WARN + 0x009).value
TPM_RC_TESTING           = TPM_RC(RC_WARN + 0x00A).value
TPM_RC_REFERENCE_H0      = TPM_RC(RC_WARN + 0x010).value
TPM_RC_REFERENCE_H1      = TPM_RC(RC_WARN + 0x011).value
TPM_RC_REFERENCE_H2      = TPM_RC(RC_WARN + 0x012).value
TPM_RC_REFERENCE_H3      = TPM_RC(RC_WARN + 0x013).value
TPM_RC_REFERENCE_H4      = TPM_RC(RC_WARN + 0x014).value
TPM_RC_REFERENCE_H5      = TPM_RC(RC_WARN + 0x015).value
TPM_RC_REFERENCE_H6      = TPM_RC(RC_WARN + 0x016).value
TPM_RC_REFERENCE_S0      = TPM_RC(RC_WARN + 0x018).value
TPM_RC_REFERENCE_S1      = TPM_RC(RC_WARN + 0x019).value
TPM_RC_REFERENCE_S2      = TPM_RC(RC_WARN + 0x01A).value
TPM_RC_REFERENCE_S3      = TPM_RC(RC_WARN + 0x01B).value
TPM_RC_REFERENCE_S4      = TPM_RC(RC_WARN + 0x01C).value
TPM_RC_REFERENCE_S5      = TPM_RC(RC_WARN + 0x01D).value
TPM_RC_REFERENCE_S6      = TPM_RC(RC_WARN + 0x01E).value
TPM_RC_NV_RATE           = TPM_RC(RC_WARN + 0x020).value
TPM_RC_LOCKOUT           = TPM_RC(RC_WARN + 0x021).value
TPM_RC_RETRY             = TPM_RC(RC_WARN + 0x022).value
TPM_RC_NV_UNAVAILABLE    = TPM_RC(RC_WARN + 0x023).value
TPM_RC_NOT_USED          = TPM_RC(RC_WARN + 0x7F).value
TPM_RC_H                 = TPM_RC(0x000).value
TPM_RC_P                 = TPM_RC(0x040).value
TPM_RC_S                 = TPM_RC(0x800).value
TPM_RC_1                 = TPM_RC(0x100).value
TPM_RC_2                 = TPM_RC(0x200).value
TPM_RC_3                 = TPM_RC(0x300).value
TPM_RC_4                 = TPM_RC(0x400).value
TPM_RC_5                 = TPM_RC(0x500).value
TPM_RC_6                 = TPM_RC(0x600).value
TPM_RC_7                 = TPM_RC(0x700).value
TPM_RC_8                 = TPM_RC(0x800).value
TPM_RC_9                 = TPM_RC(0x900).value
TPM_RC_A                 = TPM_RC(0xA00).value
TPM_RC_B                 = TPM_RC(0xB00).value
TPM_RC_C                 = TPM_RC(0xC00).value
TPM_RC_D                 = TPM_RC(0xD00).value
TPM_RC_E                 = TPM_RC(0xE00).value
TPM_RC_F                 = TPM_RC(0xF00).value
TPM_RC_N_MASK            = TPM_RC(0xF00).value

TPM_CLOCK_ADJUST        = INT8
TPM_CLOCK_COARSE_SLOWER = TPM_CLOCK_ADJUST(-3).value
TPM_CLOCK_MEDIUM_SLOWER = TPM_CLOCK_ADJUST(-2).value
TPM_CLOCK_FINE_SLOWER   = TPM_CLOCK_ADJUST(-1).value
TPM_CLOCK_NO_CHANGE     = TPM_CLOCK_ADJUST(0).value
TPM_CLOCK_FINE_FASTER   = TPM_CLOCK_ADJUST(1).value
TPM_CLOCK_MEDIUM_FASTER = TPM_CLOCK_ADJUST(2).value
TPM_CLOCK_COARSE_FASTER = TPM_CLOCK_ADJUST(3).value

TPM_EO             = UINT16
TPM_EO_EQ          = TPM_EO(0x0000).value
TPM_EO_NEQ         = TPM_EO(0x0001).value
TPM_EO_SIGNED_GT   = TPM_EO(0x0002).value
TPM_EO_UNSIGNED_GT = TPM_EO(0x0003).value
TPM_EO_SIGNED_LT   = TPM_EO(0x0004).value
TPM_EO_UNSIGNED_LT = TPM_EO(0x0005).value
TPM_EO_SIGNED_GE   = TPM_EO(0x0006).value
TPM_EO_UNSIGNED_GE = TPM_EO(0x0007).value
TPM_EO_SIGNED_LE   = TPM_EO(0x0008).value
TPM_EO_UNSIGNED_LE = TPM_EO(0x0009).value
TPM_EO_BITSET      = TPM_EO(0x000A).value
TPM_EO_BITCLEAR    = TPM_EO(0x000B).value

TPM_ST                      = UINT16
TPM_ST_RSP_COMMAND          = TPM_ST(0x00C4).value
TPM_ST_NULL                 = TPM_ST(0X8000).value
TPM_ST_NO_SESSIONS          = TPM_ST(0x8001).value
TPM_ST_SESSIONS             = TPM_ST(0x8002).value
TPM_ST_ATTEST_NV            = TPM_ST(0x8014).value
TPM_ST_ATTEST_COMMAND_AUDIT = TPM_ST(0x8015).value
TPM_ST_ATTEST_SESSION_AUDIT = TPM_ST(0x8016).value
TPM_ST_ATTEST_CERTIFY       = TPM_ST(0x8017).value
TPM_ST_ATTEST_QUOTE         = TPM_ST(0x8018).value
TPM_ST_ATTEST_TIME          = TPM_ST(0x8019).value
TPM_ST_ATTEST_CREATION      = TPM_ST(0x801A).value
TPM_ST_CREATION             = TPM_ST(0x8021).value
TPM_ST_VERIFIED             = TPM_ST(0x8022).value
TPM_ST_AUTH_SECRET          = TPM_ST(0x8023).value
TPM_ST_HASHCHECK            = TPM_ST(0x8024).value
TPM_ST_AUTH_SIGNED          = TPM_ST(0x8025).value
TPM_ST_FU_MANIFEST          = TPM_ST(0x8029).value

TPM_SU       = UINT16
TPM_SU_CLEAR = TPM_SU(0x0000).value
TPM_SU_STATE = TPM_SU(0x0001).value

TPM_SE        = UINT8
TPM_SE_HMAC   = TPM_SE(0x00).value
TPM_SE_POLICY = TPM_SE(0x01).value
TPM_SE_TRIAL  = TPM_SE(0x03).value


# TPM_CAP                 = UINT32

TPM_CAP_FIRST           = TPM_CAP(0x00000000).value
TPM_CAP_ALGS            = TPM_CAP(0x00000000).value
TPM_CAP_HANDLES         = TPM_CAP(0x00000001).value
TPM_CAP_COMMANDS        = TPM_CAP(0x00000002).value
TPM_CAP_PP_COMMANDS     = TPM_CAP(0x00000003).value
TPM_CAP_AUDIT_COMMANDS  = TPM_CAP(0x00000004).value
TPM_CAP_PCRS            = TPM_CAP(0x00000005).value
TPM_CAP_TPM_PROPERTIES  = TPM_CAP(0x00000006).value
TPM_CAP_PCR_PROPERTIES  = TPM_CAP(0x00000007).value
TPM_CAP_ECC_CURVES      = TPM_CAP(0x00000008).value
TPM_CAP_LAST            = TPM_CAP(0x00000008).value
TPM_CAP_VENDOR_PROPERTY = TPM_CAP(0x00000100).value

TPM_PT                     = UINT32
TPM_PT_NONE                = TPM_PT(0x00000000).value
PT_GROUP                   = TPM_PT(0x00000100).value
PT_FIXED                   = TPM_PT(PT_GROUP * 1).value
TPM_PT_FAMILY_INDICATOR    = TPM_PT(PT_FIXED + 0).value
TPM_PT_LEVEL               = TPM_PT(PT_FIXED + 1).value
TPM_PT_REVISION            = TPM_PT(PT_FIXED + 2).value
TPM_PT_DAY_OF_YEAR         = TPM_PT(PT_FIXED + 3).value
TPM_PT_YEAR                = TPM_PT(PT_FIXED + 4).value
TPM_PT_MANUFACTURER        = TPM_PT(PT_FIXED + 5).value
TPM_PT_VENDOR_STRING_1     = TPM_PT(PT_FIXED + 6).value
TPM_PT_VENDOR_STRING_2     = TPM_PT(PT_FIXED + 7).value
TPM_PT_VENDOR_STRING_3     = TPM_PT(PT_FIXED + 8).value
TPM_PT_VENDOR_STRING_4     = TPM_PT(PT_FIXED + 9).value
TPM_PT_VENDOR_TPM_TYPE     = TPM_PT(PT_FIXED + 10).value
TPM_PT_FIRMWARE_VERSION_1  = TPM_PT(PT_FIXED + 11).value
TPM_PT_FIRMWARE_VERSION_2  = TPM_PT(PT_FIXED + 12).value
TPM_PT_INPUT_BUFFER        = TPM_PT(PT_FIXED + 13).value
TPM_PT_HR_TRANSIENT_MIN    = TPM_PT(PT_FIXED + 14).value
TPM_PT_HR_PERSISTENT_MIN   = TPM_PT(PT_FIXED + 15).value
TPM_PT_HR_LOADED_MIN       = TPM_PT(PT_FIXED + 16).value
TPM_PT_ACTIVE_SESSIONS_MAX = TPM_PT(PT_FIXED + 17).value
TPM_PT_PCR_COUNT           = TPM_PT(PT_FIXED + 18).value
TPM_PT_PCR_SELECT_MIN      = TPM_PT(PT_FIXED + 19).value
TPM_PT_CONTEXT_GAP_MAX     = TPM_PT(PT_FIXED + 20).value
TPM_PT_NV_COUNTERS_MAX     = TPM_PT(PT_FIXED + 22).value
TPM_PT_NV_INDEX_MAX        = TPM_PT(PT_FIXED + 23).value
TPM_PT_MEMORY              = TPM_PT(PT_FIXED + 24).value
TPM_PT_CLOCK_UPDATE        = TPM_PT(PT_FIXED + 25).value
TPM_PT_CONTEXT_HASH        = TPM_PT(PT_FIXED + 26).value
TPM_PT_CONTEXT_SYM         = TPM_PT(PT_FIXED + 27).value
TPM_PT_CONTEXT_SYM_SIZE    = TPM_PT(PT_FIXED + 28).value
TPM_PT_ORDERLY_COUNT       = TPM_PT(PT_FIXED + 29).value
TPM_PT_MAX_COMMAND_SIZE    = TPM_PT(PT_FIXED + 30).value
TPM_PT_MAX_RESPONSE_SIZE   = TPM_PT(PT_FIXED + 31).value
TPM_PT_MAX_DIGEST          = TPM_PT(PT_FIXED + 32).value
TPM_PT_MAX_OBJECT_CONTEXT  = TPM_PT(PT_FIXED + 33).value
TPM_PT_MAX_SESSION_CONTEXT = TPM_PT(PT_FIXED + 34).value
TPM_PT_PS_FAMILY_INDICATOR = TPM_PT(PT_FIXED + 35).value
TPM_PT_PS_LEVEL            = TPM_PT(PT_FIXED + 36).value
TPM_PT_PS_REVISION         = TPM_PT(PT_FIXED + 37).value
TPM_PT_PS_DAY_OF_YEAR      = TPM_PT(PT_FIXED + 38).value
TPM_PT_PS_YEAR             = TPM_PT(PT_FIXED + 39).value
TPM_PT_SPLIT_MAX           = TPM_PT(PT_FIXED + 40).value
TPM_PT_TOTAL_COMMANDS      = TPM_PT(PT_FIXED + 41).value
TPM_PT_LIBRARY_COMMANDS    = TPM_PT(PT_FIXED + 42).value
TPM_PT_VENDOR_COMMANDS     = TPM_PT(PT_FIXED + 43).value
PT_VAR                     = TPM_PT(PT_GROUP * 2).value
TPM_PT_PERMANENT           = TPM_PT(PT_VAR + 0).value
TPM_PT_STARTUP_CLEAR       = TPM_PT(PT_VAR + 1).value
TPM_PT_HR_NV_INDEX         = TPM_PT(PT_VAR + 2).value
TPM_PT_HR_LOADED           = TPM_PT(PT_VAR + 3).value
TPM_PT_HR_LOADED_AVAIL     = TPM_PT(PT_VAR + 4).value
TPM_PT_HR_ACTIVE           = TPM_PT(PT_VAR + 5).value
TPM_PT_HR_ACTIVE_AVAIL     = TPM_PT(PT_VAR + 6).value
TPM_PT_HR_TRANSIENT_AVAIL  = TPM_PT(PT_VAR + 7).value
TPM_PT_HR_PERSISTENT       = TPM_PT(PT_VAR + 8).value
TPM_PT_HR_PERSISTENT_AVAIL = TPM_PT(PT_VAR + 9).value
TPM_PT_NV_COUNTERS         = TPM_PT(PT_VAR + 10).value
TPM_PT_NV_COUNTERS_AVAIL   = TPM_PT(PT_VAR + 11).value
TPM_PT_ALGORITHM_SET       = TPM_PT(PT_VAR + 12).value
TPM_PT_LOADED_CURVES       = TPM_PT(PT_VAR + 13).value
TPM_PT_LOCKOUT_COUNTER     = TPM_PT(PT_VAR + 14).value
TPM_PT_MAX_AUTH_FAIL       = TPM_PT(PT_VAR + 15).value
TPM_PT_LOCKOUT_INTERVAL    = TPM_PT(PT_VAR + 16).value
TPM_PT_LOCKOUT_RECOVERY    = TPM_PT(PT_VAR + 17).value
TPM_PT_NV_WRITE_RECOVERY   = TPM_PT(PT_VAR + 18).value
TPM_PT_AUDIT_COUNTER_0     = TPM_PT(PT_VAR + 19).value
TPM_PT_AUDIT_COUNTER_1     = TPM_PT(PT_VAR + 20).value

TPM_PT_PCR              = UINT32
TPM_PT_PCR_FIRST        = TPM_PT_PCR(0x00000000).value
TPM_PT_PCR_SAVE         = TPM_PT_PCR(0x00000000).value
TPM_PT_PCR_EXTEND_L0    = TPM_PT_PCR(0x00000001).value
TPM_PT_PCR_RESET_L0     = TPM_PT_PCR(0x00000002).value
TPM_PT_PCR_EXTEND_L1    = TPM_PT_PCR(0x00000003).value
TPM_PT_PCR_RESET_L1     = TPM_PT_PCR(0x00000004).value
TPM_PT_PCR_EXTEND_L2    = TPM_PT_PCR(0x00000005).value
TPM_PT_PCR_RESET_L2     = TPM_PT_PCR(0x00000006).value
TPM_PT_PCR_EXTEND_L3    = TPM_PT_PCR(0x00000007).value
TPM_PT_PCR_RESET_L3     = TPM_PT_PCR(0x00000008).value
TPM_PT_PCR_EXTEND_L4    = TPM_PT_PCR(0x00000009).value
TPM_PT_PCR_RESET_L4     = TPM_PT_PCR(0x0000000A).value
TPM_PT_PCR_NO_INCREMENT = TPM_PT_PCR(0x00000011).value
TPM_PT_PCR_DRTM_RESET   = TPM_PT_PCR(0x00000012).value
TPM_PT_PCR_POLICY       = TPM_PT_PCR(0x00000013).value
TPM_PT_PCR_AUTH         = TPM_PT_PCR(0x00000014).value
TPM_PT_PCR_LAST         = TPM_PT_PCR(0x00000014).value

TPM_PS                = UINT32
TPM_PS_MAIN           = TPM_PS(0x00000000).value
TPM_PS_PC             = TPM_PS(0x00000001).value
TPM_PS_PDA            = TPM_PS(0x00000002).value
TPM_PS_CELL_PHONE     = TPM_PS(0x00000003).value
TPM_PS_SERVER         = TPM_PS(0x00000004).value
TPM_PS_PERIPHERAL     = TPM_PS(0x00000005).value
TPM_PS_TSS            = TPM_PS(0x00000006).value
TPM_PS_STORAGE        = TPM_PS(0x00000007).value
TPM_PS_AUTHENTICATION = TPM_PS(0x00000008).value
TPM_PS_EMBEDDED       = TPM_PS(0x00000009).value
TPM_PS_HARDCOPY       = TPM_PS(0x0000000A).value
TPM_PS_INFRASTRUCTURE = TPM_PS(0x0000000B).value
TPM_PS_VIRTUALIZATION = TPM_PS(0x0000000C).value
TPM_PS_TNC            = TPM_PS(0x0000000D).value
TPM_PS_MULTI_TENANT   = TPM_PS(0x0000000E).value
TPM_PS_TC             = TPM_PS(0x0000000F).value

TPM_HT                = UINT8
TPM_HT_PCR            = TPM_HT(0x00).value
TPM_HT_NV_INDEX       = TPM_HT(0x01).value
TPM_HT_HMAC_SESSION   = TPM_HT(0x02).value
TPM_HT_LOADED_SESSION = TPM_HT(0x02).value
TPM_HT_POLICY_SESSION = TPM_HT(0x03).value
TPM_HT_ACTIVE_SESSION = TPM_HT(0x03).value
TPM_HT_PERMANENT      = TPM_HT(0x40).value
TPM_HT_TRANSIENT      = TPM_HT(0x80).value
TPM_HT_PERSISTENT     = TPM_HT(0x81).value

TPM_RH             = UINT32
TPM_RH_FIRST       = TPM_RH(0x40000000).value
TPM_RH_SRK         = TPM_RH(0x40000000).value
TPM_RH_OWNER       = TPM_RH(0x40000001).value
TPM_RH_REVOKE      = TPM_RH(0x40000002).value
TPM_RH_TRANSPORT   = TPM_RH(0x40000003).value
TPM_RH_OPERATOR    = TPM_RH(0x40000004).value
TPM_RH_ADMIN       = TPM_RH(0x40000005).value
TPM_RH_EK          = TPM_RH(0x40000006).value
TPM_RH_NULL        = TPM_RH(0x40000007).value
TPM_RH_UNASSIGNED  = TPM_RH(0x40000008).value
TPM_RS_PW          = TPM_RH(0x40000009).value
TPM_RH_LOCKOUT     = TPM_RH(0x4000000A).value
TPM_RH_ENDORSEMENT = TPM_RH(0x4000000B).value
TPM_RH_PLATFORM    = TPM_RH(0x4000000C).value
TPM_RH_LAST        = TPM_RH(0x4000000C).value

TPM_HC               = Tpm12.TPM_HANDLE
HR_HANDLE_MASK       = TPM_HC(0x00FFFFFF).value
HR_RANGE_MASK        = TPM_HC(0xFF000000).value
HR_SHIFT             = TPM_HC(24).value
HR_PCR               = TPM_HC(TPM_HC(TPM_HT_PCR).value << HR_SHIFT).value
HR_HMAC_SESSION      = TPM_HC(TPM_HC(TPM_HT_HMAC_SESSION).value << HR_SHIFT).value
HR_POLICY_SESSION    = TPM_HC(TPM_HC(TPM_HT_POLICY_SESSION).value << HR_SHIFT).value
HR_TRANSIENT         = TPM_HC(TPM_HC(TPM_HT_TRANSIENT).value << HR_SHIFT).value
HR_PERSISTENT        = TPM_HC(TPM_HC(TPM_HT_PERSISTENT).value << HR_SHIFT).value
HR_NV_INDEX          = TPM_HC(TPM_HC(TPM_HT_NV_INDEX).value << HR_SHIFT).value
HR_PERMANENT         = TPM_HC(TPM_HC(TPM_HT_PERMANENT).value << HR_SHIFT).value
PCR_FIRST            = TPM_HC(HR_PCR + 0).value
PCR_LAST             = TPM_HC(PCR_FIRST + IMPLEMENTATION_PCR - 1).value
HMAC_SESSION_FIRST   = TPM_HC(HR_HMAC_SESSION + 0).value
HMAC_SESSION_LAST    = TPM_HC(HMAC_SESSION_FIRST + MAX_ACTIVE_SESSIONS - 1).value
LOADED_SESSION_FIRST = TPM_HC(HMAC_SESSION_FIRST).value
LOADED_SESSION_LAST  = TPM_HC(HMAC_SESSION_LAST).value
POLICY_SESSION_FIRST = TPM_HC(HR_POLICY_SESSION + 0).value
POLICY_SESSION_LAST  = TPM_HC(POLICY_SESSION_FIRST + MAX_ACTIVE_SESSIONS - 1).value
TRANSIENT_FIRST      = TPM_HC(HR_TRANSIENT + 0).value
ACTIVE_SESSION_FIRST = TPM_HC(POLICY_SESSION_FIRST).value
ACTIVE_SESSION_LAST  = TPM_HC(POLICY_SESSION_LAST).value
TRANSIENT_LAST       = TPM_HC(TRANSIENT_FIRST+MAX_LOADED_OBJECTS - 1).value
PERSISTENT_FIRST     = TPM_HC(HR_PERSISTENT + 0).value
PERSISTENT_LAST      = TPM_HC(PERSISTENT_FIRST + 0x00FFFFFF).value
PLATFORM_PERSISTENT  = TPM_HC(PERSISTENT_FIRST + 0x00800000).value
NV_INDEX_FIRST       = TPM_HC(HR_NV_INDEX + 0).value
NV_INDEX_LAST        = TPM_HC(NV_INDEX_FIRST + 0x00FFFFFF).value
PERMANENT_FIRST      = TPM_HC(TPM_RH_FIRST).value
PERMANENT_LAST       = TPM_HC(TPM_RH_LAST).value

class TPMA_ALGORITHM (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("asymmetric",    UINT32, 1),
    ("symmetric",     UINT32, 1),
    ("hash",          UINT32, 1),
    ("object",        UINT32, 1),
    ("reserved4_7",   UINT32, 4),
    ("signing",       UINT32, 1),
    ("encrypting",    UINT32, 1),
    ("method",        UINT32, 1),
    ("reserved11_31", UINT32, 21)
  ]

class TPMA_OBJECT (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("reserved1",             UINT32, 1),
    ("fixedTPM",              UINT32, 1),
    ("stClear",               UINT32, 1),
    ("reserved4",             UINT32, 1),
    ("fixedParent",           UINT32, 1),
    ("sensitiveDataOrigin",   UINT32, 1),
    ("userWithAuth",          UINT32, 1),
    ("adminWithPolicy",       UINT32, 1),
    ("reserved8_9",           UINT32, 2),
    ("noDA",                  UINT32, 1),
    ("encryptedDuplication",  UINT32, 1),
    ("reserved12_15",         UINT32, 4),
    ("restricted",            UINT32, 1),
    ("decrypt",               UINT32, 1),
    ("sign",                  UINT32, 1),
    ("reserved19_31",         UINT32, 13)
  ]

class TPMA_SESSION (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("continueSession", UINT8, 1),
    ("auditExclusive",  UINT8, 1),
    ("auditReset",      UINT8, 1),
    ("reserved3_4",     UINT8, 2),
    ("decrypt",         UINT8, 1),
    ("encrypt",         UINT8, 1),
    ("audit",           UINT8, 1)
  ]

class TPMA_LOCALITY (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("locZero",   UINT8, 1),
    ("locOne",    UINT8, 1),
    ("locTwo",    UINT8, 1),
    ("locThree",  UINT8, 1),
    ("locFour",   UINT8, 1),
    ("Extended",  UINT8, 3)
  ]

class TPMA_PERMANENT (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("ownerAuthSet",        UINT32, 1),
    ("endorsementAuthSet",  UINT32, 1),
    ("lockoutAuthSet",      UINT32, 1),
    ("reserved3_7",         UINT32, 5),
    ("disableClear",        UINT32, 1),
    ("inLockout",           UINT32, 1),
    ("tpmGeneratedEPS",     UINT32, 1),
    ("reserved11_31",       UINT32, 21)
  ]

class TPMA_STARTUP_CLEAR (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("phEnable",      UINT32, 1),
    ("shEnable",      UINT32, 1),
    ("ehEnable",      UINT32, 1),
    ("reserved3_30",  UINT32, 28),
    ("orderly",       UINT32, 1)
  ]

class TPMA_MEMORY (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("sharedRAM",         UINT32, 1),
    ("sharedNV",          UINT32, 1),
    ("objectCopiedToRam", UINT32, 1),
    ("reserved3_31",      UINT32, 29)
  ]

class TPMA_CC (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("commandIndex",      UINT32, 16),
    ("reserved16_21",     UINT32, 6),
    ("nv",                UINT32, 1),
    ("extensive",         UINT32, 1),
    ("flushed",           UINT32, 1),
    ("cHandles",          UINT32, 3),
    ("rHandle",           UINT32, 1),
    ("V",                 UINT32, 1),
    ("Res",               UINT32, 2)
  ]

TPMI_YES_NO = BYTE
TPMI_DH_OBJECT = Tpm12.TPM_HANDLE
TPMI_DH_PERSISTENT = Tpm12.TPM_HANDLE
TPMI_DH_ENTITY = Tpm12.TPM_HANDLE
TPMI_DH_PCR = Tpm12.TPM_HANDLE
TPMI_SH_AUTH_SESSION = Tpm12.TPM_HANDLE
TPMI_SH_HMAC = Tpm12.TPM_HANDLE
TPMI_SH_POLICY = Tpm12.TPM_HANDLE
TPMI_DH_CONTEXT = Tpm12.TPM_HANDLE
TPMI_RH_HIERARCHY = Tpm12.TPM_HANDLE
TPMI_RH_HIERARCHY_AUTH = Tpm12.TPM_HANDLE
TPMI_RH_PLATFORM = Tpm12.TPM_HANDLE
TPMI_RH_OWNER = Tpm12.TPM_HANDLE
TPMI_RH_ENDORSEMENT = Tpm12.TPM_HANDLE
TPMI_RH_PROVISION = Tpm12.TPM_HANDLE
TPMI_RH_CLEAR = Tpm12.TPM_HANDLE
TPMI_RH_NV_AUTH = Tpm12.TPM_HANDLE
TPMI_RH_LOCKOUT = Tpm12.TPM_HANDLE
TPMI_RH_NV_INDEX = Tpm12.TPM_HANDLE
TPMI_ALG_HASH = TPM_ALG_ID
TPMI_ALG_ASYM = TPM_ALG_ID
TPMI_ALG_SYM = TPM_ALG_ID
TPMI_ALG_SYM_OBJECT = TPM_ALG_ID
TPMI_ALG_SYM_MODE = TPM_ALG_ID
TPMI_ALG_KDF = TPM_ALG_ID
TPMI_ALG_SIG_SCHEME = TPM_ALG_ID
TPMI_ECC_KEY_EXCHANGE = TPM_ALG_ID
TPMI_ST_COMMAND_TAG = TPM_ST

class TPMS_ALGORITHM_DESCRIPTION (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("alg",         TPM_ALG_ID),
    ("attributes",  TPMA_ALGORITHM)
  ]

class TPMU_HA (EFIPY_INDUSTRY_UNION):
  _fields_ = [
    ("sha1",    BYTE * SHA1_DIGEST_SIZE),
    ("sha256",  BYTE * SHA256_DIGEST_SIZE),
    ("sm3_256", BYTE * SM3_256_DIGEST_SIZE),
    ("sha384",  BYTE * SHA384_DIGEST_SIZE),
    ("sha512",  BYTE * SHA512_DIGEST_SIZE)
  ]

class TPMT_HA (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("hashAlg", TPMI_ALG_HASH),
    ("digest",  TPMU_HA)
  ]

class TPM2B_DIGEST (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("size",    UINT16),
    ("buffer",  BYTE * sizeof (TPMU_HA))
  ]

class TPM2B_DATA (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("size",    UINT16),
    ("buffer",  BYTE * sizeof (TPMT_HA))
  ]

TPM2B_NONCE = TPM2B_DIGEST
TPM2B_AUTH = TPM2B_DIGEST
TPM2B_OPERAND = TPM2B_DIGEST

class TPM2B_EVENT (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("size",    UINT16),
    ("buffer",  BYTE * 1024)
  ]

class TPM2B_MAX_BUFFER (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("size",    UINT16),
    ("buffer",  BYTE * MAX_DIGEST_BUFFER)
  ]

class TPM2B_MAX_NV_BUFFER (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("size",    UINT16),
    ("buffer",  BYTE * MAX_NV_INDEX_SIZE)
  ]

class TPM2B_MAX_NV_BUFFER (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("size",    UINT16),
    ("buffer",  BYTE * sizeof (UINT64))
  ]

class TPM2B_IV (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("size",    UINT16),
    ("buffer",  BYTE * MAX_SYM_BLOCK_SIZE)
  ]

class TPMU_NAME (EFIPY_INDUSTRY_UNION):
  _fields_ = [
    ("digest",  TPMT_HA),
    ("handle",  Tpm12.TPM_HANDLE)
  ]

class TPM2B_NAME (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("size",  UINT16),
    ("name",  BYTE * sizeof(TPMU_NAME))
  ]

class TPMS_PCR_SELECT (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("sizeofSelect",  UINT16),
    ("pcrSelect",     BYTE * PCR_SELECT_MAX)
  ]

class TPMS_PCR_SELECTION (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("hash",          TPMI_ALG_HASH),
    ("sizeofSelect",  UINT16),
    ("pcrSelect",     BYTE * PCR_SELECT_MAX)
  ]

class TPMT_TK_CREATION (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("tag",       UINT16),
    ("hierarchy", TPMI_RH_HIERARCHY),
    ("digest",    TPM2B_DIGEST)
  ]

class TPMT_TK_VERIFIED (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("tag",       TPM_ST),
    ("hierarchy", TPMI_RH_HIERARCHY),
    ("digest",    TPM2B_DIGEST)
  ]

TPMT_TK_AUTH = TPMT_TK_VERIFIED

TPMT_TK_HASHCHECK = TPMT_TK_VERIFIED

class TPMS_ALG_PROPERTY (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("alg",           TPM_ALG_ID),
    ("algProperties", TPMA_ALGORITHM)
  ]

MAX_CAP_ALGS       = (MAX_CAP_DATA / sizeof(TPMS_ALG_PROPERTY))

class TPMS_TAGGED_PROPERTY (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("property",  TPM_PT),
    ("value",     UINT32)
  ]

MAX_TPM_PROPERTIES = (MAX_CAP_DATA / sizeof(TPMS_TAGGED_PROPERTY))

class TPMS_TAGGED_PCR_SELECT (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("tag",           TPM_PT),
    ("sizeofSelect",  UINT8),
    ("pcrSelect",     BYTE * PCR_SELECT_MAX)
  ]

MAX_PCR_PROPERTIES = (MAX_CAP_DATA / sizeof(TPMS_TAGGED_PCR_SELECT))

class TPML_CC (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("count",         UINT32),
    ("commandCodes",  TPM_CC * MAX_CAP_CC)
  ]

class TPML_CCA (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("count",             UINT32),
    ("commandAttributes", TPMA_CC * MAX_CAP_CC)
  ]

class TPML_ALG (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("count",       UINT32),
    ("algorithms",  TPM_ALG_ID * MAX_ALG_LIST_SIZE)
  ]

class TPML_HANDLE (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("count",   UINT32),
    ("handle",  Tpm12.TPM_HANDLE * MAX_CAP_HANDLES)
  ]

class TPML_DIGEST (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("count",   UINT32),
    ("digests", TPM2B_DIGEST * 8)
  ]

class TPML_DIGEST_VALUES (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("count",   UINT32),
    ("digests", TPMT_HA * HASH_COUNT)
  ]

class TPM2B_DIGEST_VALUES (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("size",   UINT16),
    ("buffer", BYTE * sizeof (TPML_DIGEST_VALUES))
  ]

class TPML_PCR_SELECTION (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("count",         UINT32),
    ("pcrSelections", TPMS_PCR_SELECTION * HASH_COUNT)
  ]

class TPML_ALG_PROPERTY (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("count",         UINT32),
    ("algProperties", TPMS_ALG_PROPERTY * MAX_CAP_ALGS)
  ]

class TPML_TAGGED_TPM_PROPERTY (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("count",       UINT32),
    ("tpmProperty", TPMS_TAGGED_PROPERTY * MAX_TPM_PROPERTIES)
  ]

class TPML_TAGGED_PCR_PROPERTY (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("count",       UINT32),
    ("pcrProperty", TPMS_TAGGED_PCR_SELECT * MAX_PCR_PROPERTIES)
  ]

class TPML_ECC_CURVE (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("count",       UINT32),
    ("eccCurves", TPM_ECC_CURVE * MAX_ECC_CURVES)
  ]

class TPMU_CAPABILITIES (EFIPY_INDUSTRY_UNION):
  _fields_ = [
    ("algorithms",    TPML_ALG_PROPERTY),
    ("handles",       TPML_HANDLE),
    ("command",       TPML_CCA),
    ("ppCommands",    TPML_CC),
    ("auditCommands", TPML_CC),
    ("assignedPCR",   TPML_PCR_SELECTION),
    ("tpmProperties", TPML_TAGGED_TPM_PROPERTY),
    ("pcrProperties", TPML_TAGGED_PCR_PROPERTY),
    ("eccCurves",     TPML_ECC_CURVE)
  ]

class TPMS_CAPABILITY_DATA (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("capability",  TPM_CAP),
    ("data",        TPMU_CAPABILITIES)
  ]

class TPMS_CLOCK_INFO (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("clock",         UINT64),
    ("resetCount",    UINT32),
    ("restartCount",  UINT32),
    ("safe",          TPMI_YES_NO)
  ]

class TPMS_TIME_INFO (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("time",      UINT64),
    ("clockInfo", TPMS_CLOCK_INFO)
  ]

class TPMS_TIME_ATTEST_INFO (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("time",            TPMS_TIME_INFO),
    ("firmwareVersion", UINT64)
  ]

class TPMS_CERTIFY_INFO (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("name",          TPM2B_NAME),
    ("qualifiedName", TPM2B_NAME)
  ]

class TPMS_QUOTE_INFO (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("pcrSelect", TPML_PCR_SELECTION),
    ("pcrDigest", TPM2B_DIGEST)
  ]

class TPMS_COMMAND_AUDIT_INFO (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("auditCounter",  UINT64),
    ("digestAlg",     TPM_ALG_ID),
    ("auditDigest",   TPM2B_DIGEST),
    ("commandDigest", TPM2B_DIGEST)
  ]

class TPMS_SESSION_AUDIT_INFO (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("exclusiveSession",  TPMI_YES_NO),
    ("sessionDigest",     TPM2B_DIGEST)
  ]

class TPMS_CREATION_INFO (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("objectName",    TPM2B_NAME),
    ("creationHash",  TPM2B_DIGEST)
  ]

class TPMS_NV_CERTIFY_INFO (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("indexName",   TPM2B_NAME),
    ("offset",      UINT16),
    ("nvContents",  TPM2B_MAX_NV_BUFFER),
  ]

TPMI_ST_ATTEST = TPM_ST
class TPMU_ATTEST (EFIPY_INDUSTRY_UNION):
  _fields_ = [
    ("certify",       TPMS_CERTIFY_INFO),
    ("creation",      TPMS_CREATION_INFO),
    ("quote",         TPMS_QUOTE_INFO),
    ("commandAudit",  TPMS_COMMAND_AUDIT_INFO),
    ("sessionAudit",  TPMS_SESSION_AUDIT_INFO),
    ("time",          TPMS_TIME_ATTEST_INFO),
    ("nv",            TPMS_NV_CERTIFY_INFO)
  ]

class TPMS_ATTEST (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("magic",           TPM_GENERATED),
    ("type",            TPMI_ST_ATTEST),
    ("qualifiedSigner", TPM2B_NAME),
    ("extraData",       TPM2B_DATA),
    ("clockInfo",       TPMS_CLOCK_INFO),
    ("firmwareVersion", UINT64),
    ("attested",        TPMU_ATTEST)
  ]

class TPM2B_ATTEST (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("size",            UINT16),
    ("attestationData", BYTE * sizeof (TPMS_ATTEST))
  ]

class TPMS_AUTH_COMMAND (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("sessionHandle",     TPMI_SH_AUTH_SESSION),
    ("nonce",             TPM2B_NONCE),
    ("sessionAttributes", TPMA_SESSION),
    ("hmac",              TPM2B_AUTH)
  ]

class TPMS_AUTH_RESPONSE (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("nonce",             TPM2B_NONCE),
    ("sessionAttributes", TPMA_SESSION),
    ("hmac",              TPM2B_AUTH)
  ]

TPMI_AES_KEY_BITS = TPM_KEY_BITS
TPMI_SM4_KEY_BITS = TPM_KEY_BITS

class TPMU_SYM_KEY_BITS (EFIPY_INDUSTRY_UNION):
  _fields_ = [
    ("aes", TPMI_AES_KEY_BITS),
    ("SM4", TPMI_SM4_KEY_BITS),
    ("sym", TPM_KEY_BITS),
    ("xor", TPMI_ALG_HASH)
  ]

class TPMU_SYM_MODE (EFIPY_INDUSTRY_UNION):
  _fields_ = [
    ("aes", TPMI_ALG_SYM_MODE),
    ("SM4", TPMI_ALG_SYM_MODE),
    ("sym", TPMI_ALG_SYM_MODE)
  ]

class TPMT_SYM_DEF (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("algorithm", TPMI_ALG_SYM),
    ("keyBits",   TPMU_SYM_KEY_BITS),
    ("mode",      TPMU_SYM_MODE)
  ]

class TPMT_SYM_DEF_OBJECT (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("algorithm", TPMI_ALG_SYM_OBJECT),
    ("keyBits",   TPMU_SYM_KEY_BITS),
    ("mode",      TPMU_SYM_MODE)
  ]

class TPM2B_SYM_KEY (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("size",    UINT16),
    ("buffer",  BYTE * MAX_SYM_KEY_BYTES)
  ]

class TPMS_SYMCIPHER_PARMS (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("sym",    TPMT_SYM_DEF_OBJECT)
  ]

class TPM2B_SENSITIVE_DATA (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("size",    UINT16),
    ("buffer",  BYTE * MAX_SYM_DATA)
  ]

class TPMS_SENSITIVE_CREATE (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("data",      TPM2B_AUTH),
    ("userAuth",  TPM2B_SENSITIVE_DATA)
  ]

class TPMS_SENSITIVE_CREATE (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("size",      UINT16),
    ("sensitive", TPMS_SENSITIVE_CREATE)
  ]

class TPMS_SCHEME_SIGHASH (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("hashAlg", TPMI_ALG_HASH)
  ]

TPMI_ALG_KEYEDHASH_SCHEME = TPM_ALG_ID
TPMS_SCHEME_HMAC = TPMS_SCHEME_SIGHASH

class TPMS_SCHEME_XOR (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("hashAlg", TPMI_ALG_HASH),
    ("kdf",     TPMI_ALG_KDF)
  ]

class TPMU_SCHEME_KEYEDHASH (EFIPY_INDUSTRY_UNION):
  _fields_ = [
    ("hmac",  TPMS_SCHEME_HMAC),
    ("xor",   TPMS_SCHEME_XOR)
  ]

class TPMT_KEYEDHASH_SCHEME (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("scheme",  TPMI_ALG_KEYEDHASH_SCHEME),
    ("details", TPMU_SCHEME_KEYEDHASH)
  ]

TPMS_SCHEME_RSASSA = TPMS_SCHEME_SIGHASH
TPMS_SCHEME_RSAPSS = TPMS_SCHEME_SIGHASH
TPMS_SCHEME_ECDSA = TPMS_SCHEME_SIGHASH
TPMS_SCHEME_SM2 = TPMS_SCHEME_SIGHASH
TPMS_SCHEME_ECSCHNORR = TPMS_SCHEME_SIGHASH

class TPMS_SCHEME_ECDAA (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("hashAlg", TPMI_ALG_HASH),
    ("count",   UINT16)
  ]

class TPMU_SIG_SCHEME (EFIPY_INDUSTRY_UNION):
  _fields_ = [
    ("rsassa",    TPMS_SCHEME_RSASSA),
    ("rsapss",    TPMS_SCHEME_RSAPSS),
    ("ecdsa",     TPMS_SCHEME_ECDSA),
    ("ecdaa",     TPMS_SCHEME_ECDAA),
    ("ecSchnorr", TPMS_SCHEME_ECSCHNORR),
    ("hmac",      TPMS_SCHEME_HMAC),
    ("any",       TPMS_SCHEME_SIGHASH),
  ]

class TPMT_SIG_SCHEME (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("scheme",  TPMI_ALG_SIG_SCHEME),
    ("details", TPMU_SIG_SCHEME)
  ]

class TPMS_SCHEME_OAEP (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("hashAlg", TPMI_ALG_HASH)
  ]

TPMS_SCHEME_ECDH = TPMS_SCHEME_OAEP

TPMS_SCHEME_MGF1 = TPMS_SCHEME_OAEP
TPMS_SCHEME_KDF1_SP800_56a = TPMS_SCHEME_OAEP
TPMS_SCHEME_KDF2 = TPMS_SCHEME_OAEP
TPMS_SCHEME_KDF1_SP800_108 = TPMS_SCHEME_OAEP

class TPMU_KDF_SCHEME (EFIPY_INDUSTRY_UNION):
  _fields_ = [
    ("mgf1",            TPMS_SCHEME_MGF1),
    ("kdf1_SP800_56a",  TPMS_SCHEME_KDF1_SP800_56a),
    ("kdf2",            TPMS_SCHEME_KDF2),
    ("kdf1_sp800_108",  TPMS_SCHEME_KDF1_SP800_108),
  ]

class TPMT_KDF_SCHEME (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("scheme",  TPMI_ALG_KDF),
    ("details", TPMU_KDF_SCHEME)
  ]

TPMI_ALG_ASYM_SCHEME = TPM_ALG_ID
class TPMU_ASYM_SCHEME (EFIPY_INDUSTRY_UNION):
  _fields_ = [
    ("rsassa",    TPMS_SCHEME_RSASSA),
    ("rsapss",    TPMS_SCHEME_RSAPSS),
    ("oaep",      TPMS_SCHEME_OAEP),
    ("ecdsa",     TPMS_SCHEME_ECDSA),
    ("ecdaa",     TPMS_SCHEME_ECDAA),
    ("ecSchnorr", TPMS_SCHEME_ECSCHNORR),
    ("anySig",    TPMS_SCHEME_SIGHASH)
  ]

class TPMT_ASYM_SCHEME (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("scheme",  TPMI_ALG_ASYM_SCHEME),
    ("details", TPMU_ASYM_SCHEME)
  ]

TPMI_ALG_RSA_SCHEME = TPM_ALG_ID

class TPMT_RSA_SCHEME (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("scheme",  TPMI_ALG_RSA_SCHEME),
    ("details", TPMU_ASYM_SCHEME)
  ]

TPMI_ALG_RSA_DECRYPT = TPM_ALG_ID

class TPMT_RSA_DECRYPT (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("scheme",  TPMI_ALG_RSA_DECRYPT),
    ("details", TPMU_ASYM_SCHEME)
  ]

class TPM2B_PUBLIC_KEY_RSA (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("size",    UINT16),
    ("buffer",  BYTE * MAX_RSA_KEY_BYTES)
  ]

TPMI_RSA_KEY_BITS = TPM_KEY_BITS

class TPM2B_PRIVATE_KEY_RSA (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("size",    UINT16),
    ("buffer",  BYTE * (MAX_RSA_KEY_BYTES / 2))
  ]

class TPM2B_ECC_PARAMETER (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("size",    UINT16),
    ("buffer",  BYTE * MAX_ECC_KEY_BYTES)
  ]

class TPMS_ECC_POINT (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("x", TPM2B_ECC_PARAMETER),
    ("y", TPM2B_ECC_PARAMETER)
  ]

class TPM2B_ECC_POINT (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("size",  UINT16),
    ("point", TPMS_ECC_POINT)
  ]

TPMI_ALG_ECC_SCHEME = TPM_ALG_ID
TPMI_ECC_CURVE = TPM_ECC_CURVE
class TPMT_ECC_SCHEME (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("scheme",  TPMI_ALG_ECC_SCHEME),
    ("details", TPMU_SIG_SCHEME)
  ]

class TPMS_ALGORITHM_DETAIL_ECC (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("curveID", TPM_ECC_CURVE),
    ("keySize", UINT16),
    ("kdf",     TPMT_KDF_SCHEME),
    ("sign",    TPMT_ECC_SCHEME),
    ("p",       TPM2B_ECC_PARAMETER),
    ("a",       TPM2B_ECC_PARAMETER),
    ("b",       TPM2B_ECC_PARAMETER),
    ("gX",      TPM2B_ECC_PARAMETER),
    ("gY",      TPM2B_ECC_PARAMETER),
    ("n",       TPM2B_ECC_PARAMETER),
    ("h",       TPM2B_ECC_PARAMETER)
  ]

class TPMS_SIGNATURE_RSASSA (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("sig",  TPMI_ALG_HASH),
    ("hash", TPM2B_PUBLIC_KEY_RSA)
  ]

class TPMS_SIGNATURE_RSAPSS (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("hash",  TPMI_ALG_HASH),
    ("sig",   TPM2B_PUBLIC_KEY_RSA)
  ]

class TPMS_SIGNATURE_ECDSA (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("hash",        TPMI_ALG_HASH),
    ("signatureR",  TPM2B_ECC_PARAMETER),
    ("signatureS",  TPM2B_ECC_PARAMETER)
  ]

class TPMU_SIGNATURE (EFIPY_INDUSTRY_UNION):
  _fields_ = [
    ("rsassa",    TPMS_SIGNATURE_RSASSA),
    ("rsapss",    TPMS_SIGNATURE_RSAPSS),
    ("ecdsa",     TPMS_SIGNATURE_ECDSA),
    ("sm2",       TPMS_SIGNATURE_ECDSA),
    ("ecdaa",     TPMS_SIGNATURE_ECDSA),
    ("ecschnorr", TPMS_SIGNATURE_ECDSA),
    ("hmac",      TPMT_HA),
    ("any",       TPMS_SCHEME_SIGHASH)
  ]

class TPMT_SIGNATURE (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("sigAlg",    TPMI_ALG_SIG_SCHEME),
    ("signature", TPMU_SIGNATURE)
  ]

class TPMU_ENCRYPTED_SECRET (EFIPY_INDUSTRY_UNION):
  _fields_ = [
    ("ecc",       BYTE * sizeof (TPMS_ECC_POINT)),
    ("rsa",       BYTE * MAX_RSA_KEY_BYTES),
    ("symmetric", BYTE * sizeof (TPM2B_DIGEST)),
    ("keyedHash", BYTE * sizeof (TPM2B_DIGEST))
  ]

class TPM2B_ENCRYPTED_SECRET (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("size",    UINT16),
    ("secret",  BYTE * sizeof (TPMU_ENCRYPTED_SECRET))
  ]

TPMI_ALG_PUBLIC = TPM_ALG_ID
class TPMU_PUBLIC_ID (EFIPY_INDUSTRY_UNION):
  _fields_ = [
    ("keyedHash", TPM2B_DIGEST),
    ("sym",       TPM2B_DIGEST),
    ("rsa",       TPM2B_PUBLIC_KEY_RSA),
    ("ecc",       TPMS_ECC_POINT)
  ]

class TPMS_KEYEDHASH_PARMS (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("scheme",  TPMT_KEYEDHASH_SCHEME)
  ]

class TPMS_ASYM_PARMS (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("symmetric", TPMT_SYM_DEF_OBJECT),
    ("scheme",    TPMT_ASYM_SCHEME)
  ]

class TPMS_RSA_PARMS (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("symmetric", TPMT_SYM_DEF_OBJECT),
    ("scheme",    TPMT_RSA_SCHEME),
    ("keyBits",   TPMI_RSA_KEY_BITS),
    ("exponent",  UINT32)
  ]

class TPMS_ECC_PARMS (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("symmetric", TPMT_SYM_DEF_OBJECT),
    ("scheme",    TPMT_ECC_SCHEME),
    ("curveID",   TPMI_ECC_CURVE),
    ("kdf",       TPMT_KDF_SCHEME)
  ]

class TPMU_PUBLIC_PARMS (EFIPY_INDUSTRY_UNION):
  _fields_ = [
    ("keyedHashDetail", TPMS_KEYEDHASH_PARMS),
    ("symDetail",       TPMT_SYM_DEF_OBJECT),
    ("rsaDetail",       TPMS_RSA_PARMS),
    ("eccDetail",       TPMS_ECC_PARMS),
    ("asymDetail",      TPMS_ASYM_PARMS)
  ]

class TPMT_PUBLIC_PARMS (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("type",        TPMI_ALG_PUBLIC),
    ("parameters",  TPMU_PUBLIC_PARMS)
  ]

class TPMT_PUBLIC (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("type",              TPMI_ALG_PUBLIC),
    ("nameAlg",           TPMI_ALG_HASH),
    ("objectAttributes",  TPMA_OBJECT),
    ("authPolicy",        TPM2B_DIGEST),
    ("parameters",        TPMU_PUBLIC_PARMS),
    ("unique",            TPMU_PUBLIC_ID)
  ]

class TPM2B_PUBLIC (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("size",        UINT16),
    ("publicArea",  TPMT_PUBLIC)
  ]

class TPM2B_PRIVATE_VENDOR_SPECIFIC (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("size",    UINT16),
    ("buffer",  BYTE * PRIVATE_VENDOR_SPECIFIC_BYTES)
  ]

class TPMU_SENSITIVE_COMPOSITE (EFIPY_INDUSTRY_UNION):
  _fields_ = [
    ("rsa",   TPM2B_PRIVATE_KEY_RSA),
    ("ecc",   TPM2B_ECC_PARAMETER),
    ("bits",  TPM2B_SENSITIVE_DATA),
    ("sym",   TPM2B_SYM_KEY),
    ("any",   TPM2B_PRIVATE_VENDOR_SPECIFIC)
  ]

class TPMT_SENSITIVE (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("sensitiveType", TPMI_ALG_PUBLIC),
    ("authValue",     TPM2B_AUTH),
    ("seedValue",     TPM2B_DIGEST),
    ("sensitive",     TPMU_SENSITIVE_COMPOSITE)
  ]

class TPM2B_SENSITIVE (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("size",          UINT16),
    ("sensitiveArea", TPMT_SENSITIVE)
  ]

class _PRIVATE (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("integrityOuter",  TPM2B_DIGEST),
    ("integrityInner",  TPM2B_DIGEST),
    ("sensitive",       TPMT_SENSITIVE)
  ]

class TPM2B_PRIVATE (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("size",    UINT16),
    ("buffer",  BYTE * sizeof (_PRIVATE))
  ]

class _ID_OBJECT (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("integrityHMAC", TPM2B_DIGEST),
    ("encIdentity",   TPM2B_DIGEST)
  ]

class TPM2B_ID_OBJECT (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("size",        UINT16),
    ("credential",  BYTE * sizeof (_ID_OBJECT))
  ]

class TPMA_NV (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("TPMA_NV_PPWRITE",         UINT32, 1),
    ("TPMA_NV_OWNERWRITE ",     UINT32, 1),
    ("TPMA_NV_AUTHWRITE",       UINT32, 1),
    ("TPMA_NV_POLICYWRITE",     UINT32, 1),
    ("TPMA_NV_COUNTER",         UINT32, 1),
    ("TPMA_NV_BITS",            UINT32, 1),
    ("TPMA_NV_EXTEND",          UINT32, 1),
    ("reserved7_9",             UINT32, 3),
    ("TPMA_NV_POLICY_DELETE ",  UINT32, 1),
    ("TPMA_NV_WRITELOCKED",     UINT32, 1),
    ("TPMA_NV_WRITEALL",        UINT32, 1),
    ("TPMA_NV_WRITEDEFINE",     UINT32, 1),
    ("TPMA_NV_WRITE_STCLEAR ",  UINT32, 1),
    ("TPMA_NV_GLOBALLOCK",      UINT32, 1),
    ("TPMA_NV_PPREAD",          UINT32, 1),
    ("TPMA_NV_OWNERREAD",       UINT32, 1),
    ("TPMA_NV_AUTHREAD",        UINT32, 1),
    ("TPMA_NV_POLICYREAD",      UINT32, 1),
    ("reserved20_24",           UINT32, 5),
    ("TPMA_NV_NO_DA",           UINT32, 1),
    ("TPMA_NV_ORDERLY",         UINT32, 1),
    ("TPMA_NV_CLEAR_STCLEAR",   UINT32, 1),
    ("TPMA_NV_READLOCKED",      UINT32, 1),
    ("TPMA_NV_WRITTEN",         UINT32, 1),
    ("TPMA_NV_PLATFORMCREATE",  UINT32, 1),
    ("TPMA_NV_READ_STCLEAR",    UINT32, 1)
  ]

class TPMS_NV_PUBLIC (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("nvIndex",     TPMI_RH_NV_INDEX),
    ("nameAlg",     TPMI_ALG_HASH),
    ("attributes",  TPMA_NV),
    ("authPolicy",  TPM2B_DIGEST),
    ("dataSize",    UINT16)
  ]

class TPM2B_NV_PUBLIC (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("size",      UINT16),
    ("nvPublic",  TPMS_NV_PUBLIC)
  ]

class TPM2B_CONTEXT_SENSITIVE (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("size",    UINT16),
    ("buffer",  BYTE * MAX_CONTEXT_SIZE)
  ]

class TPMS_CONTEXT_DATA (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("integrity", TPM2B_DIGEST),
    ("encrypted", TPM2B_CONTEXT_SENSITIVE)
  ]

class TPM2B_CONTEXT_DATA (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("size",    UINT16),
    ("buffer",  BYTE * sizeof(TPMS_CONTEXT_DATA))
  ]

class TPMS_CONTEXT (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("sequence",    UINT64),
    ("savedHandle", TPMI_DH_CONTEXT),
    ("hierarchy",   TPMI_RH_HIERARCHY),
    ("contextBlob", TPM2B_CONTEXT_DATA)
  ]

class TPMS_CREATION_DATA (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("pcrSelect",           TPML_PCR_SELECTION),
    ("pcrDigest",           TPM2B_DIGEST),
    ("locality",            TPMA_LOCALITY),
    ("parentNameAlg",       TPM_ALG_ID),
    ("parentName",          TPM2B_NAME),
    ("parentQualifiedName", TPM2B_NAME),
    ("outsideInfo",         TPM2B_DATA)
  ]

class TPM2B_CREATION_DATA (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("size",          UINT16),
    ("creationData", TPMS_CREATION_DATA)
  ]

class TPM2_COMMAND_HEADER (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("tag",         TPM_ST),
    ("paramSize",   UINT32),
    ("commandCode", TPM_CC)
  ]

class TPM2_RESPONSE_HEADER (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("tag",           TPM_ST),
    ("paramSize",     UINT32),
    ("responseCode",  TPM_RC)
  ]

