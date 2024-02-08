def hexdump(data):
        dump = ""
        for chunk in [data[i:i+16] for i in range(0, len(data), 16)]:
            #print(chunk)
            hexes = " ".join(["{:02X}".format(n) for n in chunk]).ljust(49)
            asciirep = "".join([chr(n) if chr(n).isprintable() else "." for n in chunk])
            dump += hexes + asciirep + "\n"
        return dump