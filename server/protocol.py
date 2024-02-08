# dream mouse structure
# packet structure:
#       |--mode--|---m1---|---m2---|---m3---|--velx--|--vely--|--sclx--|--scly--|

# data structure:
#       |--byte--|--byte--|--byte--|--byte--|--long--|--long--|--long--|--long--|



# dream gyro mouse structure
# packet structure:
#       |--mode--|---m1---|---m2---|---m3---|--angx--|--angy--|

# data structure:
#       |--byte--|--byte--|--byte--|--byte--|--long--|--long--|




# dream keyboard structure
# packet structure:
#       |--mode--|--key1--|--key2--|--key3--|--key4--|--key5--|--key6--|
# data structure:
#       |--char--|--char--|--char--|--char--|--char--|--char--|--char--|






# current mouse implementation:
# packet structure:
#       |--mode--|--velx--|--vely--|---m1---|---m2---|

# data structure:
#       |--byte--|--flot--|--flot--|--byte--|--byte--|



# explanation:
# - there are only 5 mode, char is more than enough
# - velocitys are hopefully in double, so long is probably enough
# - i would use long double, but i have no clue how to use it in python or if its implemented in python...
#   ok.. well its probably is since python uses big number but give me a break ok d:



class protocol:
    def __init__(self) -> None:
        self.type
        self.velX
        self.velY
        pass
        