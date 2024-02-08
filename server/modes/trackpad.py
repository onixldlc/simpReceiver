# current mouse implementation:
# packet structure:
#       |--mode--|--velx--|--vely--|---m1---|---m2---|

# data structure:
#       |--char--|--flot--|--flot--|--char--|--char--|


from server.modes.buffer import Buffer

class Trackpad(Buffer):
    def unpackData(self):
        velX, velY, m1, m2 = self.unpack("ffBB")
        return {
            "velX":velX,
            "velY":velY,
            "m1":m1,
            "m2":m2,
        }
