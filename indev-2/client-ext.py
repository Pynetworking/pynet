#filename: client-ext.py
import socket
import time
import os

hostname1 = input()
hostname = hostname1.casefold()
if hostname == 'pynet.org':
	PORT = 1
	IP = "26.78.225.20"
if hostname == 'pynet.org/news':
	PORT = 2
	IP = "26.78.225.20"
# Mobile Supported Sites
if hostname == 'm.pynet.org':
	PORT = 3
	IP = "26.78.225.20"
# End Of Mobile-Supported sites
if hostname == 'asciiguys.tv':
	PORT = 4
	IP = "26.78.225.20"
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((IP, PORT))

msg = s.recv(1024)
os.system('cls')
print("Current connected site: " + hostname)
print()
print(msg.decode("utf-8"))
exec(open("client-ext.py").read())
