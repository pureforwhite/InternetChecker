import socket
import sys
from time import sleep
o = print
l = Exception
y = socket.AF_INET
a = socket.socket
m = sys.exit
b = socket.SOCK_STREAM
def c():
    try:
        o("\n\n checking your internet \n\n")
        s = a(y,b)
        s.connect(("www.google.com",80))
        s.close()
        o("You are online")
    except l:
        o("You're offline")
        o("Exiting")
        sleep(1)
        m(0)
c()

#Everything is working fine
#Even I am building this in this damn way
#XDDDDDDD
#Thanks for watching this video
#Please subscribe and turn on the bell You will get every notification every time I upload a new video
#Thanks for every support from you guys! See ya in next video!