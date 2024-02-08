# current mouse implementation:
# packet structure:
#       |--mode--|--velx--|--vely--|---m1---|---m2---|

# data structure:
#       |--char--|--flot--|--flot--|--char--|--char--|


from modes.trackpad import Trackpad

class TrackpadTest(Trackpad):
    def unpackData(self):
        velX, velY, m1, m2 = self.unpack("IIBB")
        return {
            "velX":velX,
            "velY":velY,
            "m1":m1,
            "m2":m2,
        }
