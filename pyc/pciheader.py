#
#Its really intresting how i get this file :)
# its lib/header.h file
# Replace /# #/ by # #
# Replace = by awk '{$2="=" OFS $2} 1' file > file
### comment macro functions by sed -e '/(x)/s/^/#/g' -i file
#


PCI_VENDOR_ID = 0x00 # 16 bits #
PCI_DEVICE_ID = 0x02 # 16 bits #
PCI_COMMAND = 0x04 # 16 bits #
PCI_COMMAND_IO = 0x1 # Enable response in I/O space #
PCI_COMMAND_MEMORY = 0x2 # Enable response in Memory space #
PCI_COMMAND_MASTER = 0x4 # Enable bus mastering #
PCI_COMMAND_SPECIAL = 0x8 # Enable response to special cycles #
PCI_COMMAND_INVALIDATE = 0x10 # Use memory write and invalidate #
PCI_COMMAND_VGA_PALETTE = 0x20 # Enable palette snooping #
PCI_COMMAND_PARITY = 0x40 # Enable parity checking #
PCI_COMMAND_WAIT = 0x80 # Enable address/data stepping #
PCI_COMMAND_SERR = 0x100 # Enable SERR #
PCI_COMMAND_FAST_BACK = 0x200 # Enable back-to-back writes #
PCI_COMMAND_DISABLE_INTx = 0x400 # PCIE: Disable INTx interrupts #

PCI_STATUS = 0x06 # 16 bits #
PCI_STATUS_INTx = 0x08 # PCIE: INTx interrupt pending #
PCI_STATUS_CAP_LIST = 0x10 # Support Capability List #
PCI_STATUS_66MHZ = 0x20 # Support 66 Mhz PCI 2.1 bus #
PCI_STATUS_UDF = 0x40 # Support User Definable Features [obsolete] #
PCI_STATUS_FAST_BACK = 0x80 # Accept fast-back to back #
PCI_STATUS_PARITY = 0x100 # Detected parity error #
PCI_STATUS_DEVSEL_MASK = 0x600 # DEVSEL timing #
PCI_STATUS_DEVSEL_FAST = 0x000
PCI_STATUS_DEVSEL_MEDIUM = 0x200
PCI_STATUS_DEVSEL_SLOW = 0x400
PCI_STATUS_SIG_TARGET_ABORT = 0x800 # Set on target abort #
PCI_STATUS_REC_TARGET_ABORT = 0x1000 # Master ack of " #
PCI_STATUS_REC_MASTER_ABORT = 0x2000 # Set on master abort #
PCI_STATUS_SIG_SYSTEM_ERROR = 0x4000 # Set when we drive SERR #
PCI_STATUS_DETECTED_PARITY = 0x8000 # Set on parity error #

PCI_CLASS_REVISION = 0x08 # High 24 bits are class, low 8
#revision = #
PCI_REVISION_ID = 0x08 # Revision ID #
PCI_CLASS_PROG = 0x09 # Reg. Level Programming Interface #
PCI_CLASS_DEVICE = 0x0a # Device class #

PCI_CACHE_LINE_SIZE = 0x0c # 8 bits #
PCI_LATENCY_TIMER = 0x0d # 8 bits #
PCI_HEADER_TYPE = 0x0e # 8 bits #
PCI_HEADER_TYPE_NORMAL = 0
PCI_HEADER_TYPE_BRIDGE = 1
PCI_HEADER_TYPE_CARDBUS = 2

PCI_BIST = 0x0f # 8 bits #
PCI_BIST_CODE_MASK = 0x0f # Return result #
PCI_BIST_START = 0x40 # 1 to start BIST, 2 secs or less #
PCI_BIST_CAPABLE = 0x80 # 1 if BIST capable #

#
# = Base addresses specify locations in memory or I/O space.
# = Decoded size can be determined by writing a value of
# = 0xffffffff to the register, and reading it back. Only
# = 1 bits are decoded.
#
PCI_BASE_ADDRESS_0 = 0x10 # 32 bits #
PCI_BASE_ADDRESS_1 = 0x14 # 32 bits [htype 0,1 only] #
PCI_BASE_ADDRESS_2 = 0x18 # 32 bits [htype 0 only] #
PCI_BASE_ADDRESS_3 = 0x1c # 32 bits #
PCI_BASE_ADDRESS_4 = 0x20 # 32 bits #
PCI_BASE_ADDRESS_5 = 0x24 # 32 bits #
PCI_BASE_ADDRESS_SPACE = 0x01 # 0 = memory, 1 = I/O #
PCI_BASE_ADDRESS_SPACE_IO = 0x01
PCI_BASE_ADDRESS_SPACE_MEMORY = 0x00
PCI_BASE_ADDRESS_MEM_TYPE_MASK = 0x06
PCI_BASE_ADDRESS_MEM_TYPE_32 = 0x00 # 32 bit address #
PCI_BASE_ADDRESS_MEM_TYPE_1M = 0x02 # Below 1M [obsolete] #
PCI_BASE_ADDRESS_MEM_TYPE_64 = 0x04 # 64 bit address #
PCI_BASE_ADDRESS_MEM_PREFETCH = 0x08 # prefetchable? #
#PCI_BASE_ADDRESS_MEM_MASK = (~(pciaddr_t)0x0f)
#PCI_BASE_ADDRESS_IO_MASK = (~(pciaddr_t)0x03)
# = bit 1 is reserved if address_space = 1 #

# = Header type 0 (normal devices) #
PCI_CARDBUS_CIS = 0x28
PCI_SUBSYSTEM_VENDOR_ID = 0x2c
PCI_SUBSYSTEM_ID = 0x2e
PCI_ROM_ADDRESS = 0x30 # Bits 31..11 are address, 10..1 reserved #
PCI_ROM_ADDRESS_ENABLE = 0x01
#PCI_ROM_ADDRESS_MASK = (~(pciaddr_t)0x7ff)

PCI_CAPABILITY_LIST = 0x34 # Offset of first capability list entry #

# = 0x35-0x3b are reserved #
PCI_INTERRUPT_LINE = 0x3c # 8 bits #
PCI_INTERRUPT_PIN = 0x3d # 8 bits #
PCI_MIN_GNT = 0x3e # 8 bits #
PCI_MAX_LAT = 0x3f # 8 bits #

# = Header type 1 (PCI-to-PCI bridges) #
PCI_PRIMARY_BUS = 0x18 # Primary bus number #
PCI_SECONDARY_BUS = 0x19 # Secondary bus number #
PCI_SUBORDINATE_BUS = 0x1a # Highest bus number behind the bridge #
PCI_SEC_LATENCY_TIMER = 0x1b # Latency timer for secondary interface #
PCI_IO_BASE = 0x1c # I/O range behind the bridge #
PCI_IO_LIMIT = 0x1d
PCI_IO_RANGE_TYPE_MASK = 0x0f # I/O bridging type #
PCI_IO_RANGE_TYPE_16 = 0x00
PCI_IO_RANGE_TYPE_32 = 0x01
PCI_IO_RANGE_MASK = ~0x0f
PCI_SEC_STATUS = 0x1e # Secondary status register #
PCI_MEMORY_BASE = 0x20 # Memory range behind #
PCI_MEMORY_LIMIT = 0x22
PCI_MEMORY_RANGE_TYPE_MASK = 0x0f
PCI_MEMORY_RANGE_MASK = ~0x0f
PCI_PREF_MEMORY_BASE = 0x24 # Prefetchable memory range behind #
PCI_PREF_MEMORY_LIMIT = 0x26
PCI_PREF_RANGE_TYPE_MASK = 0x0f
PCI_PREF_RANGE_TYPE_32 = 0x00
PCI_PREF_RANGE_TYPE_64 = 0x01
PCI_PREF_RANGE_MASK = ~0x0f
PCI_PREF_BASE_UPPER32 = 0x28 # Upper half of prefetchable memory range #
PCI_PREF_LIMIT_UPPER32 = 0x2c
PCI_IO_BASE_UPPER16 = 0x30 # Upper half of I/O addresses #
PCI_IO_LIMIT_UPPER16 = 0x32
# = 0x34 same as for htype 0 #
# = 0x35-0x3b is reserved #
PCI_ROM_ADDRESS1 = 0x38 # Same as PCI_ROM_ADDRESS, but for htype 1 #
# = 0x3c-0x3d are same as for htype 0 #
PCI_BRIDGE_CONTROL = 0x3e
PCI_BRIDGE_CTL_PARITY = 0x01 # Enable parity detection on secondary interface #
PCI_BRIDGE_CTL_SERR = 0x02 # The same for SERR forwarding #
PCI_BRIDGE_CTL_NO_ISA = 0x04 # Disable bridging of ISA ports #
PCI_BRIDGE_CTL_VGA = 0x08 # Forward VGA addresses #
PCI_BRIDGE_CTL_MASTER_ABORT = 0x20 # Report master aborts #
PCI_BRIDGE_CTL_BUS_RESET = 0x40 # Secondary bus reset #
PCI_BRIDGE_CTL_FAST_BACK = 0x80 # Fast Back2Back enabled on secondary interface #
PCI_BRIDGE_CTL_PRI_DISCARD_TIMER = 0x100 # PCI-X? #
PCI_BRIDGE_CTL_SEC_DISCARD_TIMER = 0x200 # PCI-X? #
PCI_BRIDGE_CTL_DISCARD_TIMER_STATUS = 0x400 # PCI-X? #
PCI_BRIDGE_CTL_DISCARD_TIMER_SERR_EN = 0x800 # PCI-X? #

# = Header type 2 (CardBus bridges) #
# = 0x14-0x15 reserved #
PCI_CB_SEC_STATUS = 0x16 # Secondary status #
PCI_CB_PRIMARY_BUS = 0x18 # PCI bus number #
PCI_CB_CARD_BUS = 0x19 # CardBus bus number #
PCI_CB_SUBORDINATE_BUS = 0x1a # Subordinate bus number #
PCI_CB_LATENCY_TIMER = 0x1b # CardBus latency timer #
PCI_CB_MEMORY_BASE_0 = 0x1c
PCI_CB_MEMORY_LIMIT_0 = 0x20
PCI_CB_MEMORY_BASE_1 = 0x24
PCI_CB_MEMORY_LIMIT_1 = 0x28
PCI_CB_IO_BASE_0 = 0x2c
PCI_CB_IO_BASE_0_HI = 0x2e
PCI_CB_IO_LIMIT_0 = 0x30
PCI_CB_IO_LIMIT_0_HI = 0x32
PCI_CB_IO_BASE_1 = 0x34
PCI_CB_IO_BASE_1_HI = 0x36
PCI_CB_IO_LIMIT_1 = 0x38
PCI_CB_IO_LIMIT_1_HI = 0x3a
PCI_CB_IO_RANGE_MASK = ~0x03
# = 0x3c-0x3d are same as for htype 0 #
PCI_CB_BRIDGE_CONTROL = 0x3e
PCI_CB_BRIDGE_CTL_PARITY = 0x01 # Similar to standard bridge control register #
PCI_CB_BRIDGE_CTL_SERR = 0x02
PCI_CB_BRIDGE_CTL_ISA = 0x04
PCI_CB_BRIDGE_CTL_VGA = 0x08
PCI_CB_BRIDGE_CTL_MASTER_ABORT = 0x20
PCI_CB_BRIDGE_CTL_CB_RESET = 0x40 # CardBus reset #
PCI_CB_BRIDGE_CTL_16BIT_INT = 0x80 # Enable interrupt for 16-bit cards #
PCI_CB_BRIDGE_CTL_PREFETCH_MEM0 = 0x100 # Prefetch enable for both memory regions #
PCI_CB_BRIDGE_CTL_PREFETCH_MEM1 = 0x200
PCI_CB_BRIDGE_CTL_POST_WRITES = 0x400
PCI_CB_SUBSYSTEM_VENDOR_ID = 0x40
PCI_CB_SUBSYSTEM_ID = 0x42
PCI_CB_LEGACY_MODE_BASE = 0x44 # 16-bit PC Card legacy mode base address (ExCa) #
# = 0x48-0x7f reserved #

# = Capability lists #

PCI_CAP_LIST_ID = 0 # Capability ID #
PCI_CAP_ID_PM = 0x01 # Power Management #
PCI_CAP_ID_AGP = 0x02 # Accelerated Graphics Port #
PCI_CAP_ID_VPD = 0x03 # Vital Product Data #
PCI_CAP_ID_SLOTID = 0x04 # Slot Identification #
PCI_CAP_ID_MSI = 0x05 # Message Signaled Interrupts #
PCI_CAP_ID_CHSWP = 0x06 # CompactPCI HotSwap #
PCI_CAP_ID_PCIX = 0x07 # PCI-X #
PCI_CAP_ID_HT = 0x08 # HyperTransport #
PCI_CAP_ID_VNDR = 0x09 # Vendor specific #
PCI_CAP_ID_DBG = 0x0A # Debug port #
PCI_CAP_ID_CCRC = 0x0B # CompactPCI Central Resource Control #
PCI_CAP_ID_HOTPLUG = 0x0C # PCI hot-plug #
PCI_CAP_ID_SSVID = 0x0D # Bridge subsystem vendor/device ID #
PCI_CAP_ID_AGP3 = 0x0E # AGP 8x #
PCI_CAP_ID_SECURE = 0x0F # Secure device (?) #
PCI_CAP_ID_EXP = 0x10 # PCI Express #
PCI_CAP_ID_MSIX = 0x11 # MSI-X #
PCI_CAP_ID_SATA = 0x12 # Serial-ATA HBA #
PCI_CAP_ID_AF = 0x13 # Advanced features of PCI devices integrated in PCIe root cplx #
PCI_CAP_LIST_NEXT = 1 # Next capability in the list #
PCI_CAP_FLAGS = 2 # Capability defined flags (16 bits) #
PCI_CAP_SIZEOF = 4

# = Capabilities residing in the PCI Express extended configuration space #

PCI_EXT_CAP_ID_AER = 0x01 # Advanced Error Reporting #
PCI_EXT_CAP_ID_VC = 0x02 # Virtual Channel #
PCI_EXT_CAP_ID_DSN = 0x03 # Device Serial Number #
PCI_EXT_CAP_ID_PB = 0x04 # Power Budgeting #
PCI_EXT_CAP_ID_RCLINK = 0x05 # Root Complex Link Declaration #
PCI_EXT_CAP_ID_RCILINK = 0x06 # Root Complex Internal Link Declaration #
PCI_EXT_CAP_ID_RCECOLL = 0x07 # Root Complex Event Collector #
PCI_EXT_CAP_ID_MFVC = 0x08 # Multi-Function Virtual Channel #
PCI_EXT_CAP_ID_RBCB = 0x0a # Root Bridge Control Block #
PCI_EXT_CAP_ID_VNDR = 0x0b # Vendor specific #
PCI_EXT_CAP_ID_ACS = 0x0d # Access Controls #
PCI_EXT_CAP_ID_ARI = 0x0e # Alternative Routing-ID Interpretation #
PCI_EXT_CAP_ID_ATS = 0x0f # Address Translation Service #
PCI_EXT_CAP_ID_SRIOV = 0x10 # Single Root I/O Virtualization #

# = Power Management Registers #

PCI_PM_CAP_VER_MASK = 0x0007 # Version (2=PM1.1) #
PCI_PM_CAP_PME_CLOCK = 0x0008 # Clock required for PME generation #
PCI_PM_CAP_DSI = 0x0020 # Device specific initialization required #
PCI_PM_CAP_AUX_C_MASK = 0x01c0 # Maximum aux current required in D3cold #
PCI_PM_CAP_D1 = 0x0200 # D1 power state support #
PCI_PM_CAP_D2 = 0x0400 # D2 power state support #
PCI_PM_CAP_PME_D0 = 0x0800 # PME can be asserted from D0 #
PCI_PM_CAP_PME_D1 = 0x1000 # PME can be asserted from D1 #
PCI_PM_CAP_PME_D2 = 0x2000 # PME can be asserted from D2 #
PCI_PM_CAP_PME_D3_HOT = 0x4000 # PME can be asserted from D3hot #
PCI_PM_CAP_PME_D3_COLD = 0x8000 # PME can be asserted from D3cold #
PCI_PM_CTRL = 4 # PM control and status register #
PCI_PM_CTRL_STATE_MASK = 0x0003 # Current power state (D0 to D3) #
PCI_PM_CTRL_NO_SOFT_RST = 0x0008 # No Soft Reset from D3hot to D0 #
PCI_PM_CTRL_PME_ENABLE = 0x0100 # PME pin enable #
PCI_PM_CTRL_DATA_SEL_MASK = 0x1e00 # PM table data index #
PCI_PM_CTRL_DATA_SCALE_MASK = 0x6000 # PM table data scaling factor #
PCI_PM_CTRL_PME_STATUS = 0x8000 # PME pin status #
PCI_PM_PPB_EXTENSIONS = 6 # PPB support extensions #
PCI_PM_PPB_B2_B3 = 0x40 # If bridge enters D3hot, bus enters: 0=B3, 1=B2 #
PCI_PM_BPCC_ENABLE = 0x80 # Secondary bus is power managed #
PCI_PM_DATA_REGISTER = 7 # PM table contents read here #
PCI_PM_SIZEOF = 8

# = AGP registers #

PCI_AGP_VERSION = 2 # BCD version number #
PCI_AGP_RFU = 3 # Rest of capability flags #
PCI_AGP_STATUS = 4 # Status register #
PCI_AGP_STATUS_RQ_MASK = 0xff000000 # Maximum number of requests - 1 #
PCI_AGP_STATUS_ISOCH = 0x10000 # Isochronous transactions supported #
PCI_AGP_STATUS_ARQSZ_MASK = 0xe000 # log2(optimum async req size in bytes) - 4 #
PCI_AGP_STATUS_CAL_MASK = 0x1c00 # Calibration cycle timing #
PCI_AGP_STATUS_SBA = 0x0200 # Sideband addressing supported #
PCI_AGP_STATUS_ITA_COH = 0x0100 # In-aperture accesses always coherent #
PCI_AGP_STATUS_GART64 = 0x0080 # 64-bit GART entries supported #
PCI_AGP_STATUS_HTRANS = 0x0040 # If 0, core logic can xlate host CPU accesses thru aperture #
PCI_AGP_STATUS_64BIT = 0x0020 # 64-bit addressing cycles supported #
PCI_AGP_STATUS_FW = 0x0010 # Fast write transfers supported #
PCI_AGP_STATUS_AGP3 = 0x0008 # AGP3 mode supported #
PCI_AGP_STATUS_RATE4 = 0x0004 # 4x transfer rate supported (RFU in AGP3 mode) #
PCI_AGP_STATUS_RATE2 = 0x0002 # 2x transfer rate supported (8x in AGP3 mode) #
PCI_AGP_STATUS_RATE1 = 0x0001 # 1x transfer rate supported (4x in AGP3 mode) #
PCI_AGP_COMMAND = 8 # Control register #
PCI_AGP_COMMAND_RQ_MASK = 0xff000000 # Master: Maximum number of requests #
PCI_AGP_COMMAND_ARQSZ_MASK = 0xe000 # log2(optimum async req size in bytes) - 4 #
PCI_AGP_COMMAND_CAL_MASK = 0x1c00 # Calibration cycle timing #
PCI_AGP_COMMAND_SBA = 0x0200 # Sideband addressing enabled #
PCI_AGP_COMMAND_AGP = 0x0100 # Allow processing of AGP transactions #
PCI_AGP_COMMAND_GART64 = 0x0080 # 64-bit GART entries enabled #
PCI_AGP_COMMAND_64BIT = 0x0020 # Allow generation of 64-bit addr cycles #
PCI_AGP_COMMAND_FW = 0x0010 # Enable FW transfers #
PCI_AGP_COMMAND_RATE4 = 0x0004 # Use 4x rate (RFU in AGP3 mode) #
PCI_AGP_COMMAND_RATE2 = 0x0002 # Use 2x rate (8x in AGP3 mode) #
PCI_AGP_COMMAND_RATE1 = 0x0001 # Use 1x rate (4x in AGP3 mode) #
PCI_AGP_SIZEOF = 12

# = Vital Product Data #

PCI_VPD_ADDR = 2 # Address to access (15 bits!) #
PCI_VPD_ADDR_MASK = 0x7fff # Address mask #
PCI_VPD_ADDR_F = 0x8000 # Write 0, 1 indicates completion #
PCI_VPD_DATA = 4 # 32-bits of data returned here #

# = Slot Identification #

PCI_SID_ESR = 2 # Expansion Slot Register #
PCI_SID_ESR_NSLOTS = 0x1f # Number of expansion slots available #
PCI_SID_ESR_FIC = 0x20 # First In Chassis Flag #
PCI_SID_CHASSIS_NR = 3 # Chassis Number #

# = Message Signaled Interrupts registers #

PCI_MSI_FLAGS = 2 # Various flags #
PCI_MSI_FLAGS_MASK_BIT = 0x100 # interrupt masking & reporting supported #
PCI_MSI_FLAGS_64BIT = 0x080 # 64-bit addresses allowed #
PCI_MSI_FLAGS_QSIZE = 0x070 # Message queue size configured #
PCI_MSI_FLAGS_QMASK = 0x00e # Maximum queue size available #
PCI_MSI_FLAGS_ENABLE = 0x001 # MSI feature enabled #
PCI_MSI_RFU = 3 # Rest of capability flags #
PCI_MSI_ADDRESS_LO = 4 # Lower 32 bits #
PCI_MSI_ADDRESS_HI = 8 # Upper 32 bits (if PCI_MSI_FLAGS_64BIT set) #
PCI_MSI_DATA_32 = 8 # 16 bits of data for 32-bit devices #
PCI_MSI_DATA_64 = 12 # 16 bits of data for 64-bit devices #
PCI_MSI_MASK_BIT_32 = 12 # per-vector masking for 32-bit devices #
PCI_MSI_MASK_BIT_64 = 16 # per-vector masking for 64-bit devices #
PCI_MSI_PENDING_32 = 16 # per-vector interrupt pending for 32-bit devices #
PCI_MSI_PENDING_64 = 20 # per-vector interrupt pending for 64-bit devices #

# = PCI-X #
PCI_PCIX_COMMAND = 2 # Command register offset #
PCI_PCIX_COMMAND_DPERE = 0x0001 # Data Parity Error Recover Enable #
PCI_PCIX_COMMAND_ERO = 0x0002 # Enable Relaxed Ordering #
PCI_PCIX_COMMAND_MAX_MEM_READ_BYTE_COUNT = 0x000c # Maximum Memory Read Byte Count #
PCI_PCIX_COMMAND_MAX_OUTSTANDING_SPLIT_TRANS = 0x0070
PCI_PCIX_COMMAND_RESERVED = 0xf80
PCI_PCIX_STATUS = 4 # Status register offset #
PCI_PCIX_STATUS_FUNCTION = 0x00000007
PCI_PCIX_STATUS_DEVICE = 0x000000f8
PCI_PCIX_STATUS_BUS = 0x0000ff00
PCI_PCIX_STATUS_64BIT = 0x00010000
PCI_PCIX_STATUS_133MHZ = 0x00020000
PCI_PCIX_STATUS_SC_DISCARDED = 0x00040000 # Split Completion Discarded #
PCI_PCIX_STATUS_UNEXPECTED_SC = 0x00080000 # Unexpected Split Completion #
PCI_PCIX_STATUS_DEVICE_COMPLEXITY = 0x00100000 # 0 = simple device, 1 = bridge device #
PCI_PCIX_STATUS_DESIGNED_MAX_MEM_READ_BYTE_COUNT = 0x00600000 # 0 = 512 bytes, 1 = 1024, 2 = 2048, 3 = 4096 #
PCI_PCIX_STATUS_DESIGNED_MAX_OUTSTANDING_SPLIT_TRANS = 0x03800000
PCI_PCIX_STATUS_DESIGNED_MAX_CUMULATIVE_READ_SIZE = 0x1c000000
PCI_PCIX_STATUS_RCVD_SC_ERR_MESS = 0x20000000 # Received Split Completion Error Message #
PCI_PCIX_STATUS_266MHZ = 0x40000000 # 266 MHz capable #
PCI_PCIX_STATUS_533MHZ = 0x80000000 # 533 MHz capable #
PCI_PCIX_SIZEOF = 4

# = PCI-X Bridges #
PCI_PCIX_BRIDGE_SEC_STATUS = 2 # Secondary bus status register offset #
PCI_PCIX_BRIDGE_SEC_STATUS_64BIT = 0x0001
PCI_PCIX_BRIDGE_SEC_STATUS_133MHZ = 0x0002
PCI_PCIX_BRIDGE_SEC_STATUS_SC_DISCARDED = 0x0004 # Split Completion Discarded on secondary bus #
PCI_PCIX_BRIDGE_SEC_STATUS_UNEXPECTED_SC = 0x0008 # Unexpected Split Completion on secondary bus #
PCI_PCIX_BRIDGE_SEC_STATUS_SC_OVERRUN = 0x0010 # Split Completion Overrun on secondary bus #
PCI_PCIX_BRIDGE_SEC_STATUS_SPLIT_REQUEST_DELAYED = 0x0020
PCI_PCIX_BRIDGE_SEC_STATUS_CLOCK_FREQ = 0x01c0
PCI_PCIX_BRIDGE_SEC_STATUS_RESERVED = 0xfe00
PCI_PCIX_BRIDGE_STATUS = 4 # Primary bus status register offset #
PCI_PCIX_BRIDGE_STATUS_FUNCTION = 0x00000007
PCI_PCIX_BRIDGE_STATUS_DEVICE = 0x000000f8
PCI_PCIX_BRIDGE_STATUS_BUS = 0x0000ff00
PCI_PCIX_BRIDGE_STATUS_64BIT = 0x00010000
PCI_PCIX_BRIDGE_STATUS_133MHZ = 0x00020000
PCI_PCIX_BRIDGE_STATUS_SC_DISCARDED = 0x00040000 # Split Completion Discarded #
PCI_PCIX_BRIDGE_STATUS_UNEXPECTED_SC = 0x00080000 # Unexpected Split Completion #
PCI_PCIX_BRIDGE_STATUS_SC_OVERRUN = 0x00100000 # Split Completion Overrun #
PCI_PCIX_BRIDGE_STATUS_SPLIT_REQUEST_DELAYED = 0x00200000
PCI_PCIX_BRIDGE_STATUS_RESERVED = 0xffc00000
PCI_PCIX_BRIDGE_UPSTREAM_SPLIT_TRANS_CTRL = 8 # Upstream Split Transaction Register offset #
PCI_PCIX_BRIDGE_DOWNSTREAM_SPLIT_TRANS_CTRL = 12 # Downstream Split Transaction Register offset #
PCI_PCIX_BRIDGE_STR_CAPACITY = 0x0000ffff
PCI_PCIX_BRIDGE_STR_COMMITMENT_LIMIT = 0xffff0000
PCI_PCIX_BRIDGE_SIZEOF = 12

# = HyperTransport (as of spec rev. 2.00) #
PCI_HT_CMD = 2 # Command Register #
PCI_HT_CMD_TYP_HI = 0xe000 # Capability Type high part #
PCI_HT_CMD_TYP_HI_PRI = 0x0000 # Slave or Primary Interface #
PCI_HT_CMD_TYP_HI_SEC = 0x2000 # Host or Secondary Interface #
PCI_HT_CMD_TYP = 0xf800 # Capability Type #
PCI_HT_CMD_TYP_SW = 0x4000 # Switch #
PCI_HT_CMD_TYP_IDC = 0x8000 # Interrupt Discovery and Configuration #
PCI_HT_CMD_TYP_RID = 0x8800 # Revision ID #
PCI_HT_CMD_TYP_UIDC = 0x9000 # UnitID Clumping #
PCI_HT_CMD_TYP_ECSA = 0x9800 # Extended Configuration Space Access #
PCI_HT_CMD_TYP_AM = 0xa000 # Address Mapping #
PCI_HT_CMD_TYP_MSIM = 0xa800 # MSI Mapping #
PCI_HT_CMD_TYP_DR = 0xb000 # DirectRoute #
PCI_HT_CMD_TYP_VCS = 0xb800 # VCSet #
PCI_HT_CMD_TYP_RM = 0xc000 # Retry Mode #
PCI_HT_CMD_TYP_X86 = 0xc800 # X86 (reserved) #

# = Link Control Register #
PCI_HT_LCTR_CFLE = 0x0002 # CRC Flood Enable #
PCI_HT_LCTR_CST = 0x0004 # CRC Start Test #
PCI_HT_LCTR_CFE = 0x0008 # CRC Force Error #
PCI_HT_LCTR_LKFAIL = 0x0010 # Link Failure #
PCI_HT_LCTR_INIT = 0x0020 # Initialization Complete #
PCI_HT_LCTR_EOC = 0x0040 # End of Chain #
PCI_HT_LCTR_TXO = 0x0080 # Transmitter Off #
PCI_HT_LCTR_CRCERR = 0x0f00 # CRC Error #
PCI_HT_LCTR_ISOCEN = 0x1000 # Isochronous Flow Control Enable #
PCI_HT_LCTR_LSEN = 0x2000 # LDTSTOP# Tristate Enable #
PCI_HT_LCTR_EXTCTL = 0x4000 # Extended CTL Time #
PCI_HT_LCTR_64B = 0x8000 # 64-bit Addressing Enable #

# = Link Configuration Register #
PCI_HT_LCNF_MLWI = 0x0007 # Max Link Width In #
PCI_HT_LCNF_LW_8B = 0x0 # Link Width 8 bits #
PCI_HT_LCNF_LW_16B = 0x1 # Link Width 16 bits #
PCI_HT_LCNF_LW_32B = 0x3 # Link Width 32 bits #
PCI_HT_LCNF_LW_2B = 0x4 # Link Width 2 bits #
PCI_HT_LCNF_LW_4B = 0x5 # Link Width 4 bits #
PCI_HT_LCNF_LW_NC = 0x7 # Link physically not connected #
PCI_HT_LCNF_DFI = 0x0008 # Doubleword Flow Control In #
PCI_HT_LCNF_MLWO = 0x0070 # Max Link Width Out #
PCI_HT_LCNF_DFO = 0x0080 # Doubleword Flow Control Out #
PCI_HT_LCNF_LWI = 0x0700 # Link Width In #
PCI_HT_LCNF_DFIE = 0x0800 # Doubleword Flow Control In Enable #
PCI_HT_LCNF_LWO = 0x7000 # Link Width Out #
PCI_HT_LCNF_DFOE = 0x8000 # Doubleword Flow Control Out Enable #

# = Revision ID Register #
PCI_HT_RID_MIN = 0x1f # Minor Revision #
PCI_HT_RID_MAJ = 0xe0 # Major Revision #

# = Link Frequency/Error Register #
PCI_HT_LFRER_FREQ = 0x0f # Transmitter Clock Frequency #
PCI_HT_LFRER_200 = 0x00 # 200MHz #
PCI_HT_LFRER_300 = 0x01 # 300MHz #
PCI_HT_LFRER_400 = 0x02 # 400MHz #
PCI_HT_LFRER_500 = 0x03 # 500MHz #
PCI_HT_LFRER_600 = 0x04 # 600MHz #
PCI_HT_LFRER_800 = 0x05 # 800MHz #
PCI_HT_LFRER_1000 = 0x06 # 1.0GHz #
PCI_HT_LFRER_1200 = 0x07 # 1.2GHz #
PCI_HT_LFRER_1400 = 0x08 # 1.4GHz #
PCI_HT_LFRER_1600 = 0x09 # 1.6GHz #
PCI_HT_LFRER_VEND = 0x0f # Vendor-Specific #
PCI_HT_LFRER_ERR = 0xf0 # Link Error #
PCI_HT_LFRER_PROT = 0x10 # Protocol Error #
PCI_HT_LFRER_OV = 0x20 # Overflow Error #
PCI_HT_LFRER_EOC = 0x40 # End of Chain Error #
PCI_HT_LFRER_CTLT = 0x80 # CTL Timeout #

# = Link Frequency Capability Register #
PCI_HT_LFCAP_200 = 0x0001 # 200MHz #
PCI_HT_LFCAP_300 = 0x0002 # 300MHz #
PCI_HT_LFCAP_400 = 0x0004 # 400MHz #
PCI_HT_LFCAP_500 = 0x0008 # 500MHz #
PCI_HT_LFCAP_600 = 0x0010 # 600MHz #
PCI_HT_LFCAP_800 = 0x0020 # 800MHz #
PCI_HT_LFCAP_1000 = 0x0040 # 1.0GHz #
PCI_HT_LFCAP_1200 = 0x0080 # 1.2GHz #
PCI_HT_LFCAP_1400 = 0x0100 # 1.4GHz #
PCI_HT_LFCAP_1600 = 0x0200 # 1.6GHz #
PCI_HT_LFCAP_VEND = 0x8000 # Vendor-Specific #

# = Feature Register #
PCI_HT_FTR_ISOCFC = 0x0001 # Isochronous Flow Control Mode #
PCI_HT_FTR_LDTSTOP = 0x0002 # LDTSTOP# Supported #
PCI_HT_FTR_CRCTM = 0x0004 # CRC Test Mode #
PCI_HT_FTR_ECTLT = 0x0008 # Extended CTL Time Required #
PCI_HT_FTR_64BA = 0x0010 # 64-bit Addressing #
PCI_HT_FTR_UIDRD = 0x0020 # UnitID Reorder Disable #

# = Error Handling Register #
PCI_HT_EH_PFLE = 0x0001 # Protocol Error Flood Enable #
PCI_HT_EH_OFLE = 0x0002 # Overflow Error Flood Enable #
PCI_HT_EH_PFE = 0x0004 # Protocol Error Fatal Enable #
PCI_HT_EH_OFE = 0x0008 # Overflow Error Fatal Enable #
PCI_HT_EH_EOCFE = 0x0010 # End of Chain Error Fatal Enable #
PCI_HT_EH_RFE = 0x0020 # Response Error Fatal Enable #
PCI_HT_EH_CRCFE = 0x0040 # CRC Error Fatal Enable #
PCI_HT_EH_SERRFE = 0x0080 # System Error Fatal Enable (B #
PCI_HT_EH_CF = 0x0100 # Chain Fail #
PCI_HT_EH_RE = 0x0200 # Response Error #
PCI_HT_EH_PNFE = 0x0400 # Protocol Error Nonfatal Enable #
PCI_HT_EH_ONFE = 0x0800 # Overflow Error Nonfatal Enable #
PCI_HT_EH_EOCNFE = 0x1000 # End of Chain Error Nonfatal Enable #
PCI_HT_EH_RNFE = 0x2000 # Response Error Nonfatal Enable #
PCI_HT_EH_CRCNFE = 0x4000 # CRC Error Nonfatal Enable #
PCI_HT_EH_SERRNFE = 0x8000 # System Error Nonfatal Enable #

# = HyperTransport: Slave or Primary Interface #
PCI_HT_PRI_CMD = 2 # Command Register #
PCI_HT_PRI_CMD_BUID = 0x001f # Base UnitID #
PCI_HT_PRI_CMD_UC = 0x03e0 # Unit Count #
PCI_HT_PRI_CMD_MH = 0x0400 # Master Host #
PCI_HT_PRI_CMD_DD = 0x0800 # Default Direction #
PCI_HT_PRI_CMD_DUL = 0x1000 # Drop on Uninitialized Link #

PCI_HT_PRI_LCTR0 = 4 # Link Control 0 Register #
PCI_HT_PRI_LCNF0 = 6 # Link Config 0 Register #
PCI_HT_PRI_LCTR1 = 8 # Link Control 1 Register #
PCI_HT_PRI_LCNF1 = 10 # Link Config 1 Register #
PCI_HT_PRI_RID = 12 # Revision ID Register #
PCI_HT_PRI_LFRER0 = 13 # Link Frequency/Error 0 Register #
PCI_HT_PRI_LFCAP0 = 14 # Link Frequency Capability 0 Register #
PCI_HT_PRI_FTR = 16 # Feature Register #
PCI_HT_PRI_LFRER1 = 17 # Link Frequency/Error 1 Register #
PCI_HT_PRI_LFCAP1 = 18 # Link Frequency Capability 1 Register #
PCI_HT_PRI_ES = 20 # Enumeration Scratchpad Register #
PCI_HT_PRI_EH = 22 # Error Handling Register #
PCI_HT_PRI_MBU = 24 # Memory Base Upper Register #
PCI_HT_PRI_MLU = 25 # Memory Limit Upper Register #
PCI_HT_PRI_BN = 26 # Bus Number Register #
PCI_HT_PRI_SIZEOF = 28

# = HyperTransport: Host or Secondary Interface #
PCI_HT_SEC_CMD = 2 # Command Register #
PCI_HT_SEC_CMD_WR = 0x0001 # Warm Reset #
PCI_HT_SEC_CMD_DE = 0x0002 # Double-Ended #
PCI_HT_SEC_CMD_DN = 0x0076 # Device Number #
PCI_HT_SEC_CMD_CS = 0x0080 # Chain Side #
PCI_HT_SEC_CMD_HH = 0x0100 # Host Hide #
PCI_HT_SEC_CMD_AS = 0x0400 # Act as Slave #
PCI_HT_SEC_CMD_HIECE = 0x0800 # Host Inbound End of Chain Error #
PCI_HT_SEC_CMD_DUL = 0x1000 # Drop on Uninitialized Link #

PCI_HT_SEC_LCTR = 4 # Link Control Register #
PCI_HT_SEC_LCNF = 6 # Link Config Register #
PCI_HT_SEC_RID = 8 # Revision ID Register #
PCI_HT_SEC_LFRER = 9 # Link Frequency/Error Register #
PCI_HT_SEC_LFCAP = 10 # Link Frequency Capability Register #
PCI_HT_SEC_FTR = 12 # Feature Register #
PCI_HT_SEC_FTR_EXTRS = 0x0100 # Extended Register Set #
PCI_HT_SEC_FTR_UCNFE = 0x0200 # Upstream Configuration Enable #
PCI_HT_SEC_ES = 16 # Enumeration Scratchpad Register #
PCI_HT_SEC_EH = 18 # Error Handling Register #
PCI_HT_SEC_MBU = 20 # Memory Base Upper Register #
PCI_HT_SEC_MLU = 21 # Memory Limit Upper Register #
PCI_HT_SEC_SIZEOF = 24

# = HyperTransport: Switch #
PCI_HT_SW_CMD = 2 # Switch Command Register #
PCI_HT_SW_CMD_VIBERR = 0x0080 # VIB Error #
PCI_HT_SW_CMD_VIBFL = 0x0100 # VIB Flood #
PCI_HT_SW_CMD_VIBFT = 0x0200 # VIB Fatal #
PCI_HT_SW_CMD_VIBNFT = 0x0400 # VIB Nonfatal #
PCI_HT_SW_PMASK = 4 # Partition Mask Register #
PCI_HT_SW_SWINF = 8 # Switch Info Register #
PCI_HT_SW_SWINF_DP = 0x0000001f # Default Port #
PCI_HT_SW_SWINF_EN = 0x00000020 # Enable Decode #
PCI_HT_SW_SWINF_CR = 0x00000040 # Cold Reset #
PCI_HT_SW_SWINF_PCIDX = 0x00000f00 # Performance Counter Index #
PCI_HT_SW_SWINF_BLRIDX = 0x0003f000 # Base/Limit Range Index #
PCI_HT_SW_SWINF_SBIDX = 0x00002000 # Secondary Base Range Index #
PCI_HT_SW_SWINF_HP = 0x00040000 # Hot Plug #
PCI_HT_SW_SWINF_HIDE = 0x00080000 # Hide Port #
PCI_HT_SW_PCD = 12 # Performance Counter Data Register #
PCI_HT_SW_BLRD = 16 # Base/Limit Range Data Register #
PCI_HT_SW_SBD = 20 # Secondary Base Data Register #
PCI_HT_SW_SIZEOF = 24

# = Counter indices #
PCI_HT_SW_PC_PCR = 0x0 # Posted Command Receive #
PCI_HT_SW_PC_NPCR = 0x1 # Nonposted Command Receive #
PCI_HT_SW_PC_RCR = 0x2 # Response Command Receive #
PCI_HT_SW_PC_PDWR = 0x3 # Posted DW Receive #
PCI_HT_SW_PC_NPDWR = 0x4 # Nonposted DW Receive #
PCI_HT_SW_PC_RDWR = 0x5 # Response DW Receive #
PCI_HT_SW_PC_PCT = 0x6 # Posted Command Transmit #
PCI_HT_SW_PC_NPCT = 0x7 # Nonposted Command Transmit #
PCI_HT_SW_PC_RCT = 0x8 # Response Command Transmit #
PCI_HT_SW_PC_PDWT = 0x9 # Posted DW Transmit #
PCI_HT_SW_PC_NPDWT = 0xa # Nonposted DW Transmit #
PCI_HT_SW_PC_RDWT = 0xb # Response DW Transmit #

# = Base/Limit Range indices #
PCI_HT_SW_BLR_BASE0_LO = 0x0 # Base 0[31:1], Enable #
PCI_HT_SW_BLR_BASE0_HI = 0x1 # Base 0 Upper #
PCI_HT_SW_BLR_LIM0_LO = 0x2 # Limit 0 Lower #
PCI_HT_SW_BLR_LIM0_HI = 0x3 # Limit 0 Upper #

# = Secondary Base indices #
PCI_HT_SW_SB_LO = 0x0 # Secondary Base[31:1], Enable #
PCI_HT_SW_S0_HI = 0x1 # Secondary Base Upper #

# = HyperTransport: Interrupt Discovery and Configuration #
PCI_HT_IDC_IDX = 2 # Index Register #
PCI_HT_IDC_DATA = 4 # Data Register #
PCI_HT_IDC_SIZEOF = 8

# = Register indices #
PCI_HT_IDC_IDX_LINT = 0x01 # Last Interrupt Register #
PCI_HT_IDC_LINT = 0x00ff0000 # Last interrupt definition #
PCI_HT_IDC_IDX_IDR = 0x10 # Interrupt Definition Registers #
# = Low part (at index) #
PCI_HT_IDC_IDR_MASK = 0x10000001 # Mask #
PCI_HT_IDC_IDR_POL = 0x10000002 # Polarity #
PCI_HT_IDC_IDR_II_2 = 0x1000001c # IntrInfo[4:2]: Message Type #
PCI_HT_IDC_IDR_II_5 = 0x10000020 # IntrInfo[5]: Request EOI #
PCI_HT_IDC_IDR_II_6 = 0x00ffffc0 # IntrInfo[23:6] #
PCI_HT_IDC_IDR_II_24 = 0xff000000 # IntrInfo[31:24] #
# = High part (at index + 1) #
PCI_HT_IDC_IDR_II_32 = 0x00ffffff # IntrInfo[55:32] #
PCI_HT_IDC_IDR_PASSPW = 0x40000000 # PassPW setting for messages #
PCI_HT_IDC_IDR_WEOI = 0x80000000 # Waiting for EOI #

# = HyperTransport: Revision ID #
PCI_HT_RID_RID = 2 # Revision Register #
PCI_HT_RID_SIZEOF = 4

# = HyperTransport: UnitID Clumping #
PCI_HT_UIDC_CS = 4 # Clumping Support Register #
PCI_HT_UIDC_CE = 8 # Clumping Enable Register #
PCI_HT_UIDC_SIZEOF = 12

# = HyperTransport: Extended Configuration Space Access #
PCI_HT_ECSA_ADDR = 4 # Configuration Address Register #
PCI_HT_ECSA_ADDR_REG = 0x00000ffc # Register #
PCI_HT_ECSA_ADDR_FUN = 0x00007000 # Function #
PCI_HT_ECSA_ADDR_DEV = 0x000f1000 # Device #
PCI_HT_ECSA_ADDR_BUS = 0x0ff00000 # Bus Number #
PCI_HT_ECSA_ADDR_TYPE = 0x10000000 # Access Type #
PCI_HT_ECSA_DATA = 8 # Configuration Data Register #
PCI_HT_ECSA_SIZEOF = 12

# = HyperTransport: Address Mapping #
PCI_HT_AM_CMD = 2 # Command Register #
PCI_HT_AM_CMD_NDMA = 0x000f # Number of DMA Mappings #
PCI_HT_AM_CMD_IOSIZ = 0x01f0 # I/O Size #
PCI_HT_AM_CMD_MT = 0x0600 # Map Type #
PCI_HT_AM_CMD_MT_40B = 0x0000 # 40-bit #
PCI_HT_AM_CMD_MT_64B = 0x0200 # 64-bit #

# = Window Control Register bits #
PCI_HT_AM_SBW_CTR_COMP = 0x1 # Compat #
PCI_HT_AM_SBW_CTR_NCOH = 0x2 # NonCoherent #
PCI_HT_AM_SBW_CTR_ISOC = 0x4 # Isochronous #
PCI_HT_AM_SBW_CTR_EN = 0x8 # Enable #

# = HyperTransport: 40-bit Address Mapping #
PCI_HT_AM40_SBNPW = 4 # Secondary Bus Non-Prefetchable Window Register #
PCI_HT_AM40_SBW_BASE = 0x000fffff # Window Base #
PCI_HT_AM40_SBW_CTR = 0xf0000000 # Window Control #
PCI_HT_AM40_SBPW = 8 # Secondary Bus Prefetchable Window Register #
PCI_HT_AM40_DMA_PBASE0 = 12 # DMA Window Primary Base 0 Register #
PCI_HT_AM40_DMA_CTR0 = 15 # DMA Window Control 0 Register #
PCI_HT_AM40_DMA_CTR_CTR = 0xf0 # Window Control #
PCI_HT_AM40_DMA_SLIM0 = 16 # DMA Window Secondary Limit 0 Register #
PCI_HT_AM40_DMA_SBASE0 = 18 # DMA Window Secondary Base 0 Register #
PCI_HT_AM40_SIZEOF = 12 # size is variable: 12 + 8 # NDMA #

# = HyperTransport: 64-bit Address Mapping #
PCI_HT_AM64_IDX = 4 # Index Register #
PCI_HT_AM64_DATA_LO = 8 # Data Lower Register #
PCI_HT_AM64_DATA_HI = 12 # Data Upper Register #
PCI_HT_AM64_SIZEOF = 16

# = Register indices #
PCI_HT_AM64_IDX_SBNPW = 0x00 # Secondary Bus Non-Prefetchable Window Register #
PCI_HT_AM64_W_BASE_LO = 0xfff00000 # Window Base Lower #
PCI_HT_AM64_W_CTR = 0x0000000f # Window Control #
PCI_HT_AM64_IDX_SBPW = 0x01 # Secondary Bus Prefetchable Window Register #
PCI_HT_AM64_IDX_PBNPW = 0x02 # Primary Bus Non-Prefetchable Window Register #
PCI_HT_AM64_IDX_DMAPB0 = 0x04 # DMA Window Primary Base 0 Register #
PCI_HT_AM64_IDX_DMASB0 = 0x05 # DMA Window Secondary Base 0 Register #
PCI_HT_AM64_IDX_DMASL0 = 0x06 # DMA Window Secondary Limit 0 Register #

# = HyperTransport: MSI Mapping #
PCI_HT_MSIM_CMD = 2 # Command Register #
PCI_HT_MSIM_CMD_EN = 0x0001 # Mapping Active #
PCI_HT_MSIM_CMD_FIXD = 0x0002 # MSI Mapping Address Fixed #
PCI_HT_MSIM_ADDR_LO = 4 # MSI Mapping Address Lower Register #
PCI_HT_MSIM_ADDR_HI = 8 # MSI Mapping Address Upper Register #
PCI_HT_MSIM_SIZEOF = 12

# = HyperTransport: DirectRoute #
PCI_HT_DR_CMD = 2 # Command Register #
PCI_HT_DR_CMD_NDRS = 0x000f # Number of DirectRoute Spaces #
PCI_HT_DR_CMD_IDX = 0x01f0 # Index #
PCI_HT_DR_EN = 4 # Enable Vector Register #
PCI_HT_DR_DATA = 8 # Data Register #
PCI_HT_DR_SIZEOF = 12

# = Register indices #
PCI_HT_DR_IDX_BASE_LO = 0x00 # DirectRoute Base Lower Register #
PCI_HT_DR_OTNRD = 0x00000001 # Opposite to Normal Request Direction #
PCI_HT_DR_BL_LO = 0xffffff00 # Base/Limit Lower #
PCI_HT_DR_IDX_BASE_HI = 0x01 # DirectRoute Base Upper Register #
PCI_HT_DR_IDX_LIMIT_LO = 0x02 # DirectRoute Limit Lower Register #
PCI_HT_DR_IDX_LIMIT_HI = 0x03 # DirectRoute Limit Upper Register #

# = HyperTransport: VCSet #
PCI_HT_VCS_SUP = 4 # VCSets Supported Register #
PCI_HT_VCS_L1EN = 5 # Link 1 VCSets Enabled Register #
PCI_HT_VCS_L0EN = 6 # Link 0 VCSets Enabled Register #
PCI_HT_VCS_SBD = 8 # Stream Bucket Depth Register #
PCI_HT_VCS_SINT = 9 # Stream Interval Register #
PCI_HT_VCS_SSUP = 10 # Number of Streaming VCs Supported Register #
PCI_HT_VCS_SSUP_0 = 0x00 # Streaming VC 0 #
PCI_HT_VCS_SSUP_3 = 0x01 # Streaming VCs 0-3 #
PCI_HT_VCS_SSUP_15 = 0x02 # Streaming VCs 0-15 #
PCI_HT_VCS_NFCBD = 12 # Non-FC Bucket Depth Register #
PCI_HT_VCS_NFCINT = 13 # Non-FC Bucket Interval Register #
PCI_HT_VCS_SIZEOF = 16

# = HyperTransport: Retry Mode #
PCI_HT_RM_CTR0 = 4 # Control 0 Register #
PCI_HT_RM_CTR_LRETEN = 0x01 # Link Retry Enable #
PCI_HT_RM_CTR_FSER = 0x02 # Force Single Error #
PCI_HT_RM_CTR_ROLNEN = 0x04 # Rollover Nonfatal Enable #
PCI_HT_RM_CTR_FSS = 0x08 # Force Single Stomp #
PCI_HT_RM_CTR_RETNEN = 0x10 # Retry Nonfatal Enable #
PCI_HT_RM_CTR_RETFEN = 0x20 # Retry Fatal Enable #
PCI_HT_RM_CTR_AA = 0xc0 # Allowed Attempts #
PCI_HT_RM_STS0 = 5 # Status 0 Register #
PCI_HT_RM_STS_RETSNT = 0x01 # Retry Sent #
PCI_HT_RM_STS_CNTROL = 0x02 # Count Rollover #
PCI_HT_RM_STS_SRCV = 0x04 # Stomp Received #
PCI_HT_RM_CTR1 = 6 # Control 1 Register #
PCI_HT_RM_STS1 = 7 # Status 1 Register #
PCI_HT_RM_CNT0 = 8 # Retry Count 0 Register #
PCI_HT_RM_CNT1 = 10 # Retry Count 1 Register #
PCI_HT_RM_SIZEOF = 12

# = PCI Express #
PCI_EXP_FLAGS = 0x2 # Capabilities register #
PCI_EXP_FLAGS_VERS = 0x000f # Capability version #
PCI_EXP_FLAGS_TYPE = 0x00f0 # Device/Port type #
PCI_EXP_TYPE_ENDPOINT = 0x0 # Express Endpoint #
PCI_EXP_TYPE_LEG_END = 0x1 # Legacy Endpoint #
PCI_EXP_TYPE_ROOT_PORT = 0x4 # Root Port #
PCI_EXP_TYPE_UPSTREAM = 0x5 # Upstream Port #
PCI_EXP_TYPE_DOWNSTREAM = 0x6 # Downstream Port #
PCI_EXP_TYPE_PCI_BRIDGE = 0x7 # PCI/PCI-X Bridge #
PCI_EXP_TYPE_PCIE_BRIDGE = 0x8 # PCI/PCI-X to PCIE Bridge #
PCI_EXP_TYPE_ROOT_INT_EP = 0x9 # Root Complex Integrated Endpoint #
PCI_EXP_TYPE_ROOT_EC = 0xa # Root Complex Event Collector #
PCI_EXP_FLAGS_SLOT = 0x0100 # Slot implemented #
PCI_EXP_FLAGS_IRQ = 0x3e00 # Interrupt message number #
PCI_EXP_DEVCAP = 0x4 # Device capabilities #
PCI_EXP_DEVCAP_PAYLOAD = 0x07 # Max_Payload_Size #
PCI_EXP_DEVCAP_PHANTOM = 0x18 # Phantom functions #
PCI_EXP_DEVCAP_EXT_TAG = 0x20 # Extended tags #
PCI_EXP_DEVCAP_L0S = 0x1c0 # L0s Acceptable Latency #
PCI_EXP_DEVCAP_L1 = 0xe00 # L1 Acceptable Latency #
PCI_EXP_DEVCAP_ATN_BUT = 0x1000 # Attention Button Present #
PCI_EXP_DEVCAP_ATN_IND = 0x2000 # Attention Indicator Present #
PCI_EXP_DEVCAP_PWR_IND = 0x4000 # Power Indicator Present #
PCI_EXP_DEVCAP_RBE = 0x8000 # Role-Based Error Reporting #
PCI_EXP_DEVCAP_PWR_VAL = 0x3fc0000 # Slot Power Limit Value #
PCI_EXP_DEVCAP_PWR_SCL = 0xc000000 # Slot Power Limit Scale #
PCI_EXP_DEVCAP_FLRESET = 0x10000000 # Function-Level Reset #
PCI_EXP_DEVCTL = 0x8 # Device Control #
PCI_EXP_DEVCTL_CERE = 0x0001 # Correctable Error Reporting En. #
PCI_EXP_DEVCTL_NFERE = 0x0002 # Non-Fatal Error Reporting Enable #
PCI_EXP_DEVCTL_FERE = 0x0004 # Fatal Error Reporting Enable #
PCI_EXP_DEVCTL_URRE = 0x0008 # Unsupported Request Reporting En. #
PCI_EXP_DEVCTL_RELAXED = 0x0010 # Enable Relaxed Ordering #
PCI_EXP_DEVCTL_PAYLOAD = 0x00e0 # Max_Payload_Size #
PCI_EXP_DEVCTL_EXT_TAG = 0x0100 # Extended Tag Field Enable #
PCI_EXP_DEVCTL_PHANTOM = 0x0200 # Phantom Functions Enable #
PCI_EXP_DEVCTL_AUX_PME = 0x0400 # Auxiliary Power PM Enable #
PCI_EXP_DEVCTL_NOSNOOP = 0x0800 # Enable No Snoop #
PCI_EXP_DEVCTL_READRQ = 0x7000 # Max_Read_Request_Size #
PCI_EXP_DEVCTL_BCRE = 0x8000 # Bridge Configuration Retry Enable #
PCI_EXP_DEVCTL_FLRESET = 0x8000 # Function-Level Reset [bit shared with BCRE] #
PCI_EXP_DEVSTA = 0xa # Device Status #
PCI_EXP_DEVSTA_CED = 0x01 # Correctable Error Detected #
PCI_EXP_DEVSTA_NFED = 0x02 # Non-Fatal Error Detected #
PCI_EXP_DEVSTA_FED = 0x04 # Fatal Error Detected #
PCI_EXP_DEVSTA_URD = 0x08 # Unsupported Request Detected #
PCI_EXP_DEVSTA_AUXPD = 0x10 # AUX Power Detected #
PCI_EXP_DEVSTA_TRPND = 0x20 # Transactions Pending #
PCI_EXP_LNKCAP = 0xc # Link Capabilities #
PCI_EXP_LNKCAP_SPEED = 0x0000f # Maximum Link Speed #
PCI_EXP_LNKCAP_WIDTH = 0x003f0 # Maximum Link Width #
PCI_EXP_LNKCAP_ASPM = 0x00c00 # Active State Power Management #
PCI_EXP_LNKCAP_L0S = 0x07000 # L0s Acceptable Latency #
PCI_EXP_LNKCAP_L1 = 0x38000 # L1 Acceptable Latency #
PCI_EXP_LNKCAP_CLOCKPM = 0x40000 # Clock Power Management #
PCI_EXP_LNKCAP_SURPRISE = 0x80000 # Surprise Down Error Reporting #
PCI_EXP_LNKCAP_DLLA = 0x100000 # Data Link Layer Active Reporting #
PCI_EXP_LNKCAP_LBNC = 0x200000 # Link Bandwidth Notification Capability #
PCI_EXP_LNKCAP_PORT = 0xff000000 # Port Number #
PCI_EXP_LNKCTL = 0x10 # Link Control #
PCI_EXP_LNKCTL_ASPM = 0x0003 # ASPM Control #
PCI_EXP_LNKCTL_RCB = 0x0008 # Read Completion Boundary #
PCI_EXP_LNKCTL_DISABLE = 0x0010 # Link Disable #
PCI_EXP_LNKCTL_RETRAIN = 0x0020 # Retrain Link #
PCI_EXP_LNKCTL_CLOCK = 0x0040 # Common Clock Configuration #
PCI_EXP_LNKCTL_XSYNCH = 0x0080 # Extended Synch #
PCI_EXP_LNKCTL_CLOCKPM = 0x0100 # Clock Power Management #
PCI_EXP_LNKCTL_HWAUTWD = 0x0200 # Hardware Autonomous Width Disable #
PCI_EXP_LNKCTL_BWMIE = 0x0400 # Bandwidth Mgmt Interrupt Enable #
PCI_EXP_LNKCTL_AUTBWIE = 0x0800 # Autonomous Bandwidth Mgmt Interrupt Enable #
PCI_EXP_LNKSTA = 0x12 # Link Status #
PCI_EXP_LNKSTA_SPEED = 0x000f # Negotiated Link Speed #
PCI_EXP_LNKSTA_WIDTH = 0x03f0 # Negotiated Link Width #
PCI_EXP_LNKSTA_TR_ERR = 0x0400 # Training Error (obsolete) #
PCI_EXP_LNKSTA_TRAIN = 0x0800 # Link Training #
PCI_EXP_LNKSTA_SL_CLK = 0x1000 # Slot Clock Configuration #
PCI_EXP_LNKSTA_DL_ACT = 0x2000 # Data Link Layer in DL_Active State #
PCI_EXP_LNKSTA_BWMGMT = 0x4000 # Bandwidth Mgmt Status #
PCI_EXP_LNKSTA_AUTBW = 0x8000 # Autonomous Bandwidth Mgmt Status #
PCI_EXP_SLTCAP = 0x14 # Slot Capabilities #
PCI_EXP_SLTCAP_ATNB = 0x0001 # Attention Button Present #
PCI_EXP_SLTCAP_PWRC = 0x0002 # Power Controller Present #
PCI_EXP_SLTCAP_MRL = 0x0004 # MRL Sensor Present #
PCI_EXP_SLTCAP_ATNI = 0x0008 # Attention Indicator Present #
PCI_EXP_SLTCAP_PWRI = 0x0010 # Power Indicator Present #
PCI_EXP_SLTCAP_HPS = 0x0020 # Hot-Plug Surprise #
PCI_EXP_SLTCAP_HPC = 0x0040 # Hot-Plug Capable #
PCI_EXP_SLTCAP_PWR_VAL = 0x00007f80 # Slot Power Limit Value #
PCI_EXP_SLTCAP_PWR_SCL = 0x00018000 # Slot Power Limit Scale #
PCI_EXP_SLTCAP_INTERLOCK = 0x020000 # Electromechanical Interlock Present #
PCI_EXP_SLTCAP_NOCMDCOMP = 0x040000 # No Command Completed Support #
PCI_EXP_SLTCAP_PSN = 0xfff80000 # Physical Slot Number #
PCI_EXP_SLTCTL = 0x18 # Slot Control #
PCI_EXP_SLTCTL_ATNB = 0x0001 # Attention Button Pressed Enable #
PCI_EXP_SLTCTL_PWRF = 0x0002 # Power Fault Detected Enable #
PCI_EXP_SLTCTL_MRLS = 0x0004 # MRL Sensor Changed Enable #
PCI_EXP_SLTCTL_PRSD = 0x0008 # Presence Detect Changed Enable #
PCI_EXP_SLTCTL_CMDC = 0x0010 # Command Completed Interrupt Enable #
PCI_EXP_SLTCTL_HPIE = 0x0020 # Hot-Plug Interrupt Enable #
PCI_EXP_SLTCTL_ATNI = 0x00c0 # Attention Indicator Control #
PCI_EXP_SLTCTL_PWRI = 0x0300 # Power Indicator Control #
PCI_EXP_SLTCTL_PWRC = 0x0400 # Power Controller Control #
PCI_EXP_SLTCTL_INTERLOCK = 0x0800 # Electromechanical Interlock Control #
PCI_EXP_SLTCTL_LLCHG = 0x1000 # Data Link Layer State Changed Enable #
PCI_EXP_SLTSTA = 0x1a # Slot Status #
PCI_EXP_SLTSTA_ATNB = 0x0001 # Attention Button Pressed #
PCI_EXP_SLTSTA_PWRF = 0x0002 # Power Fault Detected #
PCI_EXP_SLTSTA_MRLS = 0x0004 # MRL Sensor Changed #
PCI_EXP_SLTSTA_PRSD = 0x0008 # Presence Detect Changed #
PCI_EXP_SLTSTA_CMDC = 0x0010 # Command Completed #
PCI_EXP_SLTSTA_MRL_ST = 0x0020 # MRL Sensor State #
PCI_EXP_SLTSTA_PRES = 0x0040 # Presence Detect State #
PCI_EXP_SLTSTA_INTERLOCK = 0x0080 # Electromechanical Interlock Status #
PCI_EXP_SLTSTA_LLCHG = 0x0100 # Data Link Layer State Changed #
PCI_EXP_RTCTL = 0x1c # Root Control #
PCI_EXP_RTCTL_SECEE = 0x0001 # System Error on Correctable Error #
PCI_EXP_RTCTL_SENFEE = 0x0002 # System Error on Non-Fatal Error #
PCI_EXP_RTCTL_SEFEE = 0x0004 # System Error on Fatal Error #
PCI_EXP_RTCTL_PMEIE = 0x0008 # PME Interrupt Enable #
PCI_EXP_RTCTL_CRSVIS = 0x0010 # Configuration Request Retry Status Visible to SW #
PCI_EXP_RTCAP = 0x1e # Root Capabilities #
PCI_EXP_RTCAP_CRSVIS = 0x0010 # Configuration Request Retry Status Visible to SW #
PCI_EXP_RTSTA = 0x20 # Root Status #
PCI_EXP_RTSTA_PME_REQID = 0x0000ffff # PME Requester ID #
PCI_EXP_RTSTA_PME_STATUS = 0x00010000 # PME Status #
PCI_EXP_RTSTA_PME_PENDING = 0x00020000 # PME is Pending #
PCI_EXP_DEVCAP2 = 0x24 # Device capabilities 2 #
PCI_EXP_DEVCTL2 = 0x28 # Device Control #
###def PCI_EXP_DEV2_TIMEOUT_RANGE(x):
###    return ((x) & 0xf) # Completion Timeout Ranges Supported #
###def PCI_EXP_DEV2_TIMEOUT_VALUE(x):
###    return ((x) & 0xf) # Completion Timeout Value #
PCI_EXP_DEV2_TIMEOUT_DIS = 0x0010 # Completion Timeout Disable Supported #
PCI_EXP_DEV2_ARI = 0x0020 # ARI Forwarding #
PCI_EXP_DEVSTA2 = 0x2a # Device Status #
PCI_EXP_LNKCAP2 = 0x2c # Link Capabilities #
PCI_EXP_LNKCTL2 = 0x30 # Link Control #
###PCI_EXP_LNKCTL2_SPEED(x) = ((x) & 0xf) # Target Link Speed #
PCI_EXP_LNKCTL2_CMPLNC = 0x0010 # Enter Compliance #
PCI_EXP_LNKCTL2_SPEED_DIS = 0x0020 # Hardware Autonomous Speed Disable #
###PCI_EXP_LNKCTL2_DEEMPHASIS(x) = (((x) >> 6) & 1) # Selectable De-emphasis #
###PCI_EXP_LNKCTL2_MARGIN(x) = (((x) >> 7) & 7) # Transmit Margin #
PCI_EXP_LNKCTL2_MOD_CMPLNC = 0x0400 # Enter Modified Compliance #
PCI_EXP_LNKCTL2_CMPLNC_SOS = 0x0800 # Compliance SOS #
###PCI_EXP_LNKCTL2_COM_DEEMPHASIS(x) = (((x) >> 12) & 1) # Compliance De-emphasis #
PCI_EXP_LNKSTA2 = 0x32 # Link Status #
###PCI_EXP_LINKSTA2_DEEMPHASIS(x) = ((x) & 1) # Current De-emphasis Level #
PCI_EXP_SLTCAP2 = 0x34 # Slot Capabilities #
PCI_EXP_SLTCTL2 = 0x38 # Slot Control #
PCI_EXP_SLTSTA2 = 0x3a # Slot Status #

# = MSI-X #
PCI_MSIX_ENABLE = 0x8000
PCI_MSIX_MASK = 0x4000
PCI_MSIX_TABSIZE = 0x07ff
PCI_MSIX_TABLE = 4
PCI_MSIX_PBA = 8
PCI_MSIX_BIR = 0x7

# = Subsystem vendor/device ID for PCI bridges #
PCI_SSVID_VENDOR = 4
PCI_SSVID_DEVICE = 6

# = PCI Advanced Features #
PCI_AF_CAP = 3
PCI_AF_CAP_TP = 0x01
PCI_AF_CAP_FLR = 0x02
PCI_AF_CTRL = 4
PCI_AF_CTRL_FLR = 0x01
PCI_AF_STATUS = 5
PCI_AF_STATUS_TP = 0x01

PCI_EXT_CAPS_OFFSET = 0x100

# = Advanced Error Reporting #
PCI_ERR_UNCOR_STATUS = 4 # Uncorrectable Error Status #
PCI_ERR_UNC_TRAIN = 0x00000001 # Undefined in PCIe rev1.1 & 2.0 spec #
PCI_ERR_UNC_DLP = 0x00000010 # Data Link Protocol #
PCI_ERR_UNC_SDES = 0x00000020 # Surprise Down Error #
PCI_ERR_UNC_POISON_TLP = 0x00001000 # Poisoned TLP #
PCI_ERR_UNC_FCP = 0x00002000 # Flow Control Protocol #
PCI_ERR_UNC_COMP_TIME = 0x00004000 # Completion Timeout #
PCI_ERR_UNC_COMP_ABORT = 0x00008000 # Completer Abort #
PCI_ERR_UNC_UNX_COMP = 0x00010000 # Unexpected Completion #
PCI_ERR_UNC_RX_OVER = 0x00020000 # Receiver Overflow #
PCI_ERR_UNC_MALF_TLP = 0x00040000 # Malformed TLP #
PCI_ERR_UNC_ECRC = 0x00080000 # ECRC Error Status #
PCI_ERR_UNC_UNSUP = 0x00100000 # Unsupported Request #
PCI_ERR_UNC_ACS_VIOL = 0x00200000 # ACS Violation #
PCI_ERR_UNCOR_MASK = 8 # Uncorrectable Error Mask #
# = Same bits as above #
PCI_ERR_UNCOR_SEVER = 12 # Uncorrectable Error Severity #
# = Same bits as above #
PCI_ERR_COR_STATUS = 16 # Correctable Error Status #
PCI_ERR_COR_RCVR = 0x00000001 # Receiver Error Status #
PCI_ERR_COR_BAD_TLP = 0x00000040 # Bad TLP Status #
PCI_ERR_COR_BAD_DLLP = 0x00000080 # Bad DLLP Status #
PCI_ERR_COR_REP_ROLL = 0x00000100 # REPLAY_NUM Rollover #
PCI_ERR_COR_REP_TIMER = 0x00001000 # Replay Timer Timeout #
PCI_ERR_COR_REP_ANFE = 0x00002000 # Advisory Non-Fatal Error #
PCI_ERR_COR_MASK = 20 # Correctable Error Mask #
# = Same bits as above #
PCI_ERR_CAP = 24 # Advanced Error Capabilities #
###PCI_ERR_CAP_FEP(x) = ((x) & 31) # First Error Pointer #
PCI_ERR_CAP_ECRC_GENC = 0x00000020 # ECRC Generation Capable #
PCI_ERR_CAP_ECRC_GENE = 0x00000040 # ECRC Generation Enable #
PCI_ERR_CAP_ECRC_CHKC = 0x00000080 # ECRC Check Capable #
PCI_ERR_CAP_ECRC_CHKE = 0x00000100 # ECRC Check Enable #
PCI_ERR_HEADER_LOG = 28 # Header Log Register (16 bytes) #
PCI_ERR_ROOT_COMMAND = 44 # Root Error Command #
PCI_ERR_ROOT_STATUS = 48
PCI_ERR_ROOT_COR_SRC = 52
PCI_ERR_ROOT_SRC = 54

# = Virtual Channel #
PCI_VC_PORT_REG1 = 4
PCI_VC_PORT_REG2 = 8
PCI_VC_PORT_CTRL = 12
PCI_VC_PORT_STATUS = 14
PCI_VC_RES_CAP = 16
PCI_VC_RES_CTRL = 20
PCI_VC_RES_STATUS = 26

# = Power Budgeting #
PCI_PWR_DSR = 4 # Data Select Register #
PCI_PWR_DATA = 8 # Data Register #
###PCI_PWR_DATA_BASE(x) = ((x) & 0xff) # Base Power #
###PCI_PWR_DATA_SCALE(x) = (((x) >> 8) & 3) # Data Scale #
###PCI_PWR_DATA_PM_SUB(x) = (((x) >> 10) & 7) # PM Sub State #
###PCI_PWR_DATA_PM_STATE(x) = (((x) >> 13) & 3) # PM State #
###PCI_PWR_DATA_TYPE(x) = (((x) >> 15) & 7) # Type #
###PCI_PWR_DATA_RAIL(x) = (((x) >> 18) & 7) # Power Rail #
PCI_PWR_CAP = 12 # Capability #
###PCI_PWR_CAP_BUDGET(x) = ((x) & 1) # Included in system budget #

# = Access Control Services #
PCI_ACS_CAP = 0x04 # ACS Capability Register #
PCI_ACS_CAP_VALID = 0x0001 # ACS Source Validation #
PCI_ACS_CAP_BLOCK = 0x0002 # ACS Translation Blocking #
PCI_ACS_CAP_REQ_RED = 0x0004 # ACS P2P Request Redirect #
PCI_ACS_CAP_CMPLT_RED = 0x0008 # ACS P2P Completion Redirect #
PCI_ACS_CAP_FORWARD = 0x0010 # ACS Upstream Forwarding #
PCI_ACS_CAP_EGRESS = 0x0020 # ACS P2P Egress Control #
PCI_ACS_CAP_TRANS = 0x0040 # ACS Direct Translated P2P #
###PCI_ACS_CAP_VECTOR(x) = (((x) >> 8) & 0xff) # Egress Control Vector Size #
PCI_ACS_CTRL = 0x06 # ACS Control Register #
PCI_ACS_CTRL_VALID = 0x0001 # ACS Source Validation Enable #
PCI_ACS_CTRL_BLOCK = 0x0002 # ACS Translation Blocking Enable #
PCI_ACS_CTRL_REQ_RED = 0x0004 # ACS P2P Request Redirect Enable #
PCI_ACS_CTRL_CMPLT_RED = 0x0008 # ACS P2P Completion Redirect Enable #
PCI_ACS_CTRL_FORWARD = 0x0010 # ACS Upstream Forwarding Enable #
PCI_ACS_CTRL_EGRESS = 0x0020 # ACS P2P Egress Control Enable #
PCI_ACS_CTRL_TRANS = 0x0040 # ACS Direct Translated P2P Enable #
PCI_ACS_EGRESS_CTRL = 0x08 # Egress Control Vector #

# = Alternative Routing-ID Interpretation #
PCI_ARI_CAP = 0x04 # ARI Capability Register #
PCI_ARI_CAP_MFVC = 0x0001 # MFVC Function Groups Capability #
PCI_ARI_CAP_ACS = 0x0002 # ACS Function Groups Capability #
###PCI_ARI_CAP_NFN(x) = (((x) >> 8) & 0xff) # Next Function Number #
PCI_ARI_CTRL = 0x06 # ARI Control Register #
PCI_ARI_CTRL_MFVC = 0x0001 # MFVC Function Groups Enable #
PCI_ARI_CTRL_ACS = 0x0002 # ACS Function Groups Enable #
###PCI_ARI_CTRL_FG(x) = (((x) >> 4) & 7) # Function Group #

# = Address Translation Service #
PCI_ATS_CAP = 0x04 # ATS Capability Register #
###PCI_ATS_CAP_IQD(x) = ((x) & 0x1f) # Invalidate Queue Depth #
PCI_ATS_CTRL = 0x06 # ATS Control Register #
###PCI_ATS_CTRL_STU(x) = ((x) & 0x1f) # Smallest Translation Unit #
PCI_ATS_CTRL_ENABLE = 0x8000 # ATS Enable #

# = Single Root I/O Virtualization #
PCI_IOV_CAP = 0x04 # SR-IOV Capability Register #
PCI_IOV_CAP_VFM = 0x00000001 # VF Migration Capable #
###PCI_IOV_CAP_IMN(x) = ((x) >> 21) # VF Migration Interrupt Message Number #
PCI_IOV_CTRL = 0x08 # SR-IOV Control Register #
PCI_IOV_CTRL_VFE = 0x0001 # VF Enable #
PCI_IOV_CTRL_VFME = 0x0002 # VF Migration Enable #
PCI_IOV_CTRL_VFMIE = 0x0004 # VF Migration Interrupt Enable #
PCI_IOV_CTRL_MSE = 0x0008 # VF MSE #
PCI_IOV_CTRL_ARI = 0x0010 # ARI Capable Hierarchy #
PCI_IOV_STATUS = 0x0a # SR-IOV Status Register #
PCI_IOV_STATUS_MS = 0x0001 # VF Migration Status #
PCI_IOV_INITIALVF = 0x0c # Number of VFs that are initially associated #
PCI_IOV_TOTALVF = 0x0e # Maximum number of VFs that could be associated #
PCI_IOV_NUMVF = 0x10 # Number of VFs that are available #
PCI_IOV_FDL = 0x12 # Function Dependency Link #
PCI_IOV_OFFSET = 0x14 # First VF Offset #
PCI_IOV_STRIDE = 0x16 # Routing ID offset from one VF to the next one #
PCI_IOV_DID = 0x1a # VF Device ID #
PCI_IOV_SUPPS = 0x1c # Supported Page Sizes #
PCI_IOV_SYSPS = 0x20 # System Page Size #
PCI_IOV_BAR_BASE = 0x24 # VF BAR0, VF BAR1, ... VF BAR5 #
PCI_IOV_NUM_BAR = 6 # Number of VF BARs #
PCI_IOV_MSAO = 0x3c # VF Migration State Array Offset #
###def PCI_IOV_MSA_BIR(x):
###    return ((x) & 7) # VF Migration State BIR #
###def PCI_IOV_MSA_OFFSET(x):
###    return ((x) & 0xfffffff8) # VF Migration State Offset #

#
# = The PCI interface treats multi-function devices as independent
# = devices. The slot/function address of each device is encoded
# = in a single byte as follows:
#
# = 7:3 = slot
# = 2:0 = function
#

#PCI_DEVFN(slot,func) = ((((slot) & 0x1f) << 3) | ((func) & 0x07))
#PCI_SLOT(devfn) = (((devfn) >> 3) & 0x1f)
#PCI_FUNC(devfn) = ((devfn) & 0x07)

# = Device classes and subclasses #

PCI_CLASS_NOT_DEFINED = 0x0000
PCI_CLASS_NOT_DEFINED_VGA = 0x0001

PCI_BASE_CLASS_STORAGE = 0x01
PCI_CLASS_STORAGE_SCSI = 0x0100
PCI_CLASS_STORAGE_IDE = 0x0101
PCI_CLASS_STORAGE_FLOPPY = 0x0102
PCI_CLASS_STORAGE_IPI = 0x0103
PCI_CLASS_STORAGE_RAID = 0x0104
PCI_CLASS_STORAGE_ATA = 0x0105
PCI_CLASS_STORAGE_SATA = 0x0106
PCI_CLASS_STORAGE_SAS = 0x0107
PCI_CLASS_STORAGE_OTHER = 0x0180

PCI_BASE_CLASS_NETWORK = 0x02
PCI_CLASS_NETWORK_ETHERNET = 0x0200
PCI_CLASS_NETWORK_TOKEN_RING = 0x0201
PCI_CLASS_NETWORK_FDDI = 0x0202
PCI_CLASS_NETWORK_ATM = 0x0203
PCI_CLASS_NETWORK_ISDN = 0x0204
PCI_CLASS_NETWORK_OTHER = 0x0280

PCI_BASE_CLASS_DISPLAY = 0x03
PCI_CLASS_DISPLAY_VGA = 0x0300
PCI_CLASS_DISPLAY_XGA = 0x0301
PCI_CLASS_DISPLAY_3D = 0x0302
PCI_CLASS_DISPLAY_OTHER = 0x0380

PCI_BASE_CLASS_MULTIMEDIA = 0x04
PCI_CLASS_MULTIMEDIA_VIDEO = 0x0400
PCI_CLASS_MULTIMEDIA_AUDIO = 0x0401
PCI_CLASS_MULTIMEDIA_PHONE = 0x0402
PCI_CLASS_MULTIMEDIA_AUDIO_DEV = 0x0403
PCI_CLASS_MULTIMEDIA_OTHER = 0x0480

PCI_BASE_CLASS_MEMORY = 0x05
PCI_CLASS_MEMORY_RAM = 0x0500
PCI_CLASS_MEMORY_FLASH = 0x0501
PCI_CLASS_MEMORY_OTHER = 0x0580

PCI_BASE_CLASS_BRIDGE = 0x06
PCI_CLASS_BRIDGE_HOST = 0x0600
PCI_CLASS_BRIDGE_ISA = 0x0601
PCI_CLASS_BRIDGE_EISA = 0x0602
PCI_CLASS_BRIDGE_MC = 0x0603
PCI_CLASS_BRIDGE_PCI = 0x0604
PCI_CLASS_BRIDGE_PCMCIA = 0x0605
PCI_CLASS_BRIDGE_NUBUS = 0x0606
PCI_CLASS_BRIDGE_CARDBUS = 0x0607
PCI_CLASS_BRIDGE_RACEWAY = 0x0608
PCI_CLASS_BRIDGE_PCI_SEMI = 0x0609
PCI_CLASS_BRIDGE_IB_TO_PCI = 0x060a
PCI_CLASS_BRIDGE_OTHER = 0x0680

PCI_BASE_CLASS_COMMUNICATION = 0x07
PCI_CLASS_COMMUNICATION_SERIAL = 0x0700
PCI_CLASS_COMMUNICATION_PARALLEL = 0x0701
PCI_CLASS_COMMUNICATION_MSERIAL = 0x0702
PCI_CLASS_COMMUNICATION_MODEM = 0x0703
PCI_CLASS_COMMUNICATION_OTHER = 0x0780

PCI_BASE_CLASS_SYSTEM = 0x08
PCI_CLASS_SYSTEM_PIC = 0x0800
PCI_CLASS_SYSTEM_DMA = 0x0801
PCI_CLASS_SYSTEM_TIMER = 0x0802
PCI_CLASS_SYSTEM_RTC = 0x0803
PCI_CLASS_SYSTEM_PCI_HOTPLUG = 0x0804
PCI_CLASS_SYSTEM_OTHER = 0x0880

PCI_BASE_CLASS_INPUT = 0x09
PCI_CLASS_INPUT_KEYBOARD = 0x0900
PCI_CLASS_INPUT_PEN = 0x0901
PCI_CLASS_INPUT_MOUSE = 0x0902
PCI_CLASS_INPUT_SCANNER = 0x0903
PCI_CLASS_INPUT_GAMEPORT = 0x0904
PCI_CLASS_INPUT_OTHER = 0x0980

PCI_BASE_CLASS_DOCKING = 0x0a
PCI_CLASS_DOCKING_GENERIC = 0x0a00
PCI_CLASS_DOCKING_OTHER = 0x0a80

PCI_BASE_CLASS_PROCESSOR = 0x0b
PCI_CLASS_PROCESSOR_386 = 0x0b00
PCI_CLASS_PROCESSOR_486 = 0x0b01
PCI_CLASS_PROCESSOR_PENTIUM = 0x0b02
PCI_CLASS_PROCESSOR_ALPHA = 0x0b10
PCI_CLASS_PROCESSOR_POWERPC = 0x0b20
PCI_CLASS_PROCESSOR_MIPS = 0x0b30
PCI_CLASS_PROCESSOR_CO = 0x0b40

PCI_BASE_CLASS_SERIAL = 0x0c
PCI_CLASS_SERIAL_FIREWIRE = 0x0c00
PCI_CLASS_SERIAL_ACCESS = 0x0c01
PCI_CLASS_SERIAL_SSA = 0x0c02
PCI_CLASS_SERIAL_USB = 0x0c03
PCI_CLASS_SERIAL_FIBER = 0x0c04
PCI_CLASS_SERIAL_SMBUS = 0x0c05
PCI_CLASS_SERIAL_INFINIBAND = 0x0c06

PCI_BASE_CLASS_WIRELESS = 0x0d
PCI_CLASS_WIRELESS_IRDA = 0x0d00
PCI_CLASS_WIRELESS_CONSUMER_IR = 0x0d01
PCI_CLASS_WIRELESS_RF = 0x0d10
PCI_CLASS_WIRELESS_OTHER = 0x0d80

PCI_BASE_CLASS_INTELLIGENT = 0x0e
PCI_CLASS_INTELLIGENT_I2O = 0x0e00

PCI_BASE_CLASS_SATELLITE = 0x0f
PCI_CLASS_SATELLITE_TV = 0x0f00
PCI_CLASS_SATELLITE_AUDIO = 0x0f01
PCI_CLASS_SATELLITE_VOICE = 0x0f03
PCI_CLASS_SATELLITE_DATA = 0x0f04

PCI_BASE_CLASS_CRYPT = 0x10
PCI_CLASS_CRYPT_NETWORK = 0x1000
PCI_CLASS_CRYPT_ENTERTAINMENT = 0x1010
PCI_CLASS_CRYPT_OTHER = 0x1080

PCI_BASE_CLASS_SIGNAL = 0x11
PCI_CLASS_SIGNAL_DPIO = 0x1100
PCI_CLASS_SIGNAL_PERF_CTR = 0x1101
PCI_CLASS_SIGNAL_SYNCHRONIZER = 0x1110
PCI_CLASS_SIGNAL_OTHER = 0x1180

PCI_CLASS_OTHERS = 0xff

# = Several ID's we need in the library #

PCI_VENDOR_ID_INTEL = 0x8086
PCI_VENDOR_ID_COMPAQ = 0x0e11

PCIE_EXP_EXT_CAPS_ID=0x19

PCI_EXP_LNKCTL3=0x4

PCI_EXP_CURR_DEMPHASIS_LEVEL = 1
PCI_EXP_EQU_COMPLETE = 2
PCI_EXP_EQU_PHASE_1_SUCC = 4
PCI_EXP_EQU_PHASE_2_SUCC = 8
PCI_EXP_EQU_PHASE_3_SUCC = 16
PCI_EXP_EQU_REQUEST = 32
PCI_EXP_PERFORM_EQU = 1

#  Advanced Error Reporting  #
PCI_ERR_UNCOR_STATUS	= 4	#  Uncorrectable Error Status  #
PCI_ERR_UNC_UND	= 0x00000001	#  Undefined  #
PCI_ERR_UNC_DLP	= 0x00000010	#  Data Link Protocol  #
PCI_ERR_UNC_SURPDN	= 0x00000020	#  Surprise Down  #
PCI_ERR_UNC_POISON_TLP	= 0x00001000	#  Poisoned TLP  #
PCI_ERR_UNC_FCP	= 0x00002000	#  Flow Control Protocol  #
PCI_ERR_UNC_COMP_TIME	= 0x00004000	#  Completion Timeout  #
PCI_ERR_UNC_COMP_ABORT	= 0x00008000	#  Completer Abort  #
PCI_ERR_UNC_UNX_COMP	= 0x00010000	#  Unexpected Completion  #
PCI_ERR_UNC_RX_OVER	= 0x00020000	#  Receiver Overflow  #
PCI_ERR_UNC_MALF_TLP	= 0x00040000	#  Malformed TLP  #
PCI_ERR_UNC_ECRC	= 0x00080000	#  ECRC Error Status  #
PCI_ERR_UNC_UNSUP	= 0x00100000	#  Unsupported Request  #
PCI_ERR_UNC_ACSV	= 0x00200000	#  ACS Violation  #
PCI_ERR_UNC_INTN	= 0x00400000	#  internal error  #
PCI_ERR_UNC_MCBTLP	= 0x00800000	#  MC blocked TLP  #
PCI_ERR_UNC_ATOMEG	= 0x01000000	#  Atomic egress blocked  #
PCI_ERR_UNC_TLPPRE	= 0x02000000	#  TLP prefix blocked  #
PCI_ERR_UNCOR_MASK	= 8	#  Uncorrectable Error Mask  #
	#  Same bits as above  #
PCI_ERR_UNCOR_SEVER	= 12	#  Uncorrectable Error Severity  #
	#  Same bits as above  #
PCI_ERR_COR_STATUS	= 16	#  Correctable Error Status  #
PCI_ERR_COR_RCVR	= 0x00000001	#  Receiver Error Status  #
PCI_ERR_COR_BAD_TLP	= 0x00000040	#  Bad TLP Status  #
PCI_ERR_COR_BAD_DLLP	= 0x00000080	#  Bad DLLP Status  #
PCI_ERR_COR_REP_ROLL	= 0x00000100	#  REPLAY_NUM Rollover  #
PCI_ERR_COR_REP_TIMER	= 0x00001000	#  Replay Timer Timeout  #
PCI_ERR_COR_ADV_NFAT	= 0x00002000	#  Advisory Non-Fatal  #
PCI_ERR_COR_INTERNAL	= 0x00004000	#  Corrected Internal  #
PCI_ERR_COR_LOG_OVER	= 0x00008000	#  Header Log Overflow  #
PCI_ERR_COR_MASK	= 20	#  Correctable Error Mask  #
	#  Same bits as above  #
PCI_ERR_CAP	=	24	#  Advanced Error Capabilities  #
##PCI_ERR_CAP_FEP(x)	((x) & 31)	#  First Error Pointer  #
PCI_ERR_CAP_ECRC_GENC	= 0x00000020	#  ECRC Generation Capable  #
PCI_ERR_CAP_ECRC_GENE	 = 0x00000040	#  ECRC Generation Enable  #
PCI_ERR_CAP_ECRC_CHKC	 = 0x00000080	#  ECRC Check Capable  #
PCI_ERR_CAP_ECRC_CHKE	 = 0x00000100	#  ECRC Check Enable  #
PCI_ERR_HEADER_LOG	= 28	#  Header Log Register (16 bytes)  #
PCI_ERR_ROOT_COMMAND	= 44	#  Root Error Command  #
PCI_ERR_ROOT_CMD_COR_EN		 = 0x00000001 #  Correctable Err Reporting Enable  #
PCI_ERR_ROOT_CMD_NONFATAL_EN	 = 0x00000002 #  Non-Fatal Err Reporting Enable  #
PCI_ERR_ROOT_CMD_FATAL_EN	 = 0x00000004 #  Fatal Err Reporting Enable  #
PCI_ERR_ROOT_STATUS	= 48
PCI_ERR_ROOT_COR_RCV		 = 0x00000001 #  ERR_COR Received  #
PCI_ERR_ROOT_MULTI_COR_RCV	 = 0x00000002 #  Multiple ERR_COR  #
PCI_ERR_ROOT_UNCOR_RCV		 = 0x00000004 #  ERR_FATAL#NONFATAL  #
PCI_ERR_ROOT_MULTI_UNCOR_RCV	 = 0x00000008 #  Multiple FATAL#NONFATAL  #
PCI_ERR_ROOT_FIRST_FATAL	 = 0x00000010 #  First UNC is Fatal  #
PCI_ERR_ROOT_NONFATAL_RCV	 = 0x00000020 #  Non-Fatal Received  #
PCI_ERR_ROOT_FATAL_RCV		 = 0x00000040 #  Fatal Received  #
PCI_ERR_ROOT_AER_IRQ		 = 0xf8000000 #  Advanced Error Interrupt Message Number  #
PCI_ERR_ROOT_ERR_SRC	= 52	#  Error Source Identification  #
