import socket

s = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)

ip_port = ('0.0.0.0',12345)

while True:
    msg_input = raw_input('input: ')

    if msg_input == 'exit':
       break

    s.sendto(msg_input,ip_port)

s.close()

