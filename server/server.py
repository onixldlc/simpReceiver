from server.udp import UDPHandler
import pyautogui
import struct

# temp = print
# def tem(*objs, **kwargs):
#     temp("[+] ", *objs, **kwargs)
# __builtins__.print = tem



def moveMouse(data, addr):
    mode, velX, velY, m1, m2 =  struct.unpack(">BffBB", data)
    pyautogui.move(velX, velY, _pause = False)


def main():
    udp_handle = UDPHandler("0.0.0.0")
    # udp_handle.listen(moveMouse)
    udp_handle.listen()



if __name__ == "__main__":
    main()

# def test():
#     print("test")

# test()
# print(type(test).__name__)