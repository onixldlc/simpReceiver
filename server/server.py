from server.udp import UDPHandler

# temp = print
# def tem(*objs, **kwargs):
#     temp("[+] ", *objs, **kwargs)
# __builtins__.print = tem

def main():
    udp_handle = UDPHandler("0.0.0.0")
    udp_handle.listen()



if __name__ == "__main__":
    main()

# def test():
#     print("test")

# test()
# print(type(test).__name__)