import socket
from threading import Thread
from server.utility import hexdump
from server.control import ctrlHandle
from server.modes.buffer import Buffer
from server.modes.trackpad import Trackpad
from server.modes.trackpadTest import TrackpadTest


class UDPHandler:
    enableMouse = True
    enableDebug = True

    buffHandler = Buffer
    isModeSelected = False
    controlHandler = ctrlHandle()
    sensitivity = 0.5
    isMouseDown = False



    def __init__(self, ip="127.0.0.1", port=8008) -> None:
        self.ip = ip
        self.port = port
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    def listen(self, callback=None):
        thread1 = Thread(target=self._receiver, args=[callback])
        self.controlHandler.setFailSafe(False)
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

        if(self.enableDebug):
            print(f"[+] {addr[0]}:{addr[1]} => server")
            print("data raw:")
            print("==================================================================")
            print("\n".join([line for line in hexdump(data).split("\n") if line != ""]))
            # print("\n".join(list(map(lambda lines: f"={lines}=", [line for line in hexdump(data).split("\n") if line != ""]))))
            print("==================================================================")
            print(f"{unpackedData}")
            print("==================================================================")
            print("")
        
        if(mode == 2):
            newX = unpackedData["velX"]*self.sensitivity
            newY = unpackedData["velY"]*self.sensitivity

            if(abs(newX) > 0.002 and abs(newY) > 0.002 ):
                self.controlHandler.relativeMoveCustom(newX,newY)

            if(self.enableMouse):
                if(not self.isMouseDown and unpackedData["m1"] == 1):
                    self.isMouseDown = True
                    self.controlHandler.m1Down()
                elif(self.isMouseDown and unpackedData["m1"] == 0):
                    self.isMouseDown = False
                    self.controlHandler.m1Up()

