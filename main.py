import socket
import sys
from time import sleep

def c():
    try:
        print("\n\n checking your internet \n\n")
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect(("www.google.com", 80))
        s.close()
        print("You're online")
    except Exception:
        print("You are offline")
        print("Exiting")
        sleep(1)
        sys.exit(0)
c()

#Lets see
#I am going to try to build this is different way