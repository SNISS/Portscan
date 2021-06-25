import socket

ip = input("Enter target ip: ")

for doors in range(1, 65535):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    if s.connect_ex((ip, doors)) == 0:
        print(doors, "Open")
        s.close()
