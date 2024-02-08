import socket
from utility import hexdump
from threading import Thread
from modes.buffer import Buffer
from modes.trackpad import Trackpad
from modes.trackpadTest import TrackpadTest


class UDPHandler:
    buffHandler = Buffer
    isModeSelected = False


    def __init__(self, ip="127.0.0.1", port=8008) -> None:
        self.ip = ip
        self.port = port
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    def listen(self, callback=None):
        thread1 = Thread(target=self._receiver, args=[callback])
        thread1.run()

    def _receiver(self, callback=None):
        print(f"udp server listening on: {self.ip}:{self.port}")

        func = callback if type(callback).__name__ == "function" else self._callback

        self.socket.bind((self.ip, self.port))
        self.socket.settimeout(0.1)

        while True:
            try:
                data, addr = self.socket.recvfrom(1024)
                func(data, addr)
            except socket.timeout:
                pass
        
    def _callback(self, data, addr):        
        dataBuff = self.buffHandler(data)
        mode = dataBuff.unpackMode()
        #  breakpoint()

        result = ""

        # print(self.isModeSelected, mode)
        if not self.isModeSelected:
            match(mode):
                case 1:
                    self.buffHandler = TrackpadTest
                case 2:
                    self.buffHandler = Trackpad
                case _:
                    self.buffHandler = Buffer
                
        
        try:
            dataBuff = self.buffHandler(dataBuff)
            # print(dataBuff)
            unpackedData = dataBuff.unpackData()
        except Exception as error :
            self.isModeSelected = False
            print("ERROR! unexpected change of mode!")
            print(error.args)
            return

        
        print(f"[+] {addr[0]}:{addr[1]} => server")
        print("data raw:")
        print("==================================================================")
        print("\n".join([line for line in hexdump(data).split("\n") if line != ""]))
        # print("\n".join(list(map(lambda lines: f"={lines}=", [line for line in hexdump(data).split("\n") if line != ""]))))
        print("==================================================================")
        print(f"{unpackedData}")
        print("==================================================================")
        print("")
