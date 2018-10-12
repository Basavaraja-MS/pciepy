cimport pcipy_h
from libc.stdint cimport *

"""
import sys
def _displayhook(o):
    if type(o).__name__ in ('int', 'long'):
        print(hex(o))
        __builtins__._ = o
    else:
        sys.__displayhook__(o)

def hexon():
    sys.displayhook = _displayhook
def hexoff():
    sys.displayhook=sys.__displayhook__
"""
"""
def display_as_hex(item):
    if isinstance(item, int):
        print(hex(item))
    else:
        print(repr(item))
import sys
sys.displayhook = display_as_hex
"""
cdef class pci:
    cdef pcipy_h.pci_access *pacc
    cdef pcipy_h.pci_dev *dev

    def __cinit__(self):
        self.pacc = pcipy_h.pci_alloc()
        pcipy_h.pci_init(self.pacc)
        pcipy_h.pci_scan_bus(self.pacc)
        #self.dev = self.pacc.devices
        #TODO: Traverse to purticular vendor id and 
        #deivce id instead of first one
        #pcipy_h.pci_fill_info(self.dev, 0xFF)
    def dev_info(self):
        self.dev = self.pacc.devices
        pcipy_h.pci_fill_info(self.dev, 0xFF)

    def dev_info_next(self):
        print("Problem here")
        self.dev = self.dev.next
        print("Problem here2")
        pcipy_h.pci_fill_info(self.dev, 0xFF)
    def __dealloc__(self):
        pcipy_h.pci_cleanup(self.pacc)
    """
	cdef pcipy_h.pci_dev *fill_info(self):
		self.dev = self.pacc.devices
		pcipy_h.pci_fill_info(self.dev, 0xFF)
		return self.dev
	"""
    #TODO Need to truncate reg value to respective numbers 
    def read_byte(self, reg):
        c = pcipy_h.pci_read_byte(self.dev, reg)
        return c

    def read_word(self, reg):
        c = pcipy_h.pci_read_word(self.dev, reg)
        return c

    def read_long(self, reg):
        c = pcipy_h.pci_read_long(self.dev, reg)
        return c

    def read_block(self, pos, buf, len):
        c = pcipy_h.pci_read_block(self.dev, pos, buf, len)
        return c

    def read_vpd(self, pos, buf, len):
        c = pcipy_h.pci_read_vpd(self.dev, pos, buf, len)
        return c

    def write_byte(self, pos, data):
        c = pcipy_h.pci_write_byte(self.dev, pos, data)
        return c

    def write_word(self, pos, data):
        c = pcipy_h.pci_write_word(self.dev, pos, data)
        return c

    def write_long(self, pos, data):
        c = pcipy_h.pci_write_long(self.dev, pos, data)
        return c

    def write_block(self, pos, buf, len):
        c = pcipy_h.pci_write_block(self.dev, pos, buf, len)
        return c
"""
print ("Itshould print`:wq!")
var = pci()
var.dev_info()
print ("Its not comming here")
i = 20
while i:
    if i == 0:
        break
    var.dev_info_next()
    print ("0x%x" %var.read_word(0x0))
    i = i - 1

print ("Done with this :)")
#var.write_byte(0xc, 16)
ar = pci()
print ar.read_byte(0x0)

print "Its not printing here"
#var = pci()
ar.dev_info_next()
print ar.read_byte(0x18)
#var.write_byte(0xc, 16)
print ar.read_byte(0xc)
#print configuration info 
"""
