from ctypes import *
import struct

class Buffer(object):
    buffer = b""
    index = 0

    def __init__(self, data) -> None:
        # print(type(data))
        if type(data) != bytes:
            self.buffer = data.dump()
        elif data:
            self.buffer = data
        
    def __len__(self):
        return len(self.buffer) - self.index
    
    def dump(self):
        return self.buffer
    
    def save(self):
        self.buffer = self.buffer[self.index:]
        self.index = 0

    def create(self, buffer):
        self.buffer = buffer

    def unpackMode(self):
        return self.unpack("B")
    
    def unpackData(self):            
        return self.unpack("B"*len(self))

    
    def unpack(self, format, mode=">"):
        if(format[0] in ["@", "=", "<", ">", "!"]):
            mode = format.pop()
        unpacked = struct.unpack_from(mode+format, self.buffer)
        self.index += struct.calcsize(format)

        # print(f"[+]  buffer: '{self.buffer}'")
        # print(f"[+]  unpacked data: '{unpacked}'")
        # print(f"[+]  unpacked data format: '{mode+format}'" )

        self.save()
        if(len(format)<2):
            return unpacked[0]
        return unpacked
        


    # def unpackChar(self):
    #     if(self.size - self.index < c_char):
    #         raise("Error! buffer is not enough for char type!")
    #     self.index+=2
    #     return struct.unpack_from(">c", self.buffer, self.index)
    
    # def unpackInt(self):
    #     if(self.size - self.index < c_int32):
    #         raise("Error! buffer is not enough for char type!")
    #     self.index+=4
    #     return struct.unpack_from(">i", self.buffer, self.index)
    
    # def unpackFloat(self):
    #     if(self.size - self.index < c_float):
    #         raise("Error! buffer is not enough for char type!")
    #     self.index+=4
    #     return struct.unpack_from(">f", self.buffer, self.index)

