#!/usr/bin/python
import pyqrcode
from googlesearch import search
from pyqrcode import QRCode
browser=input("enter anything that u wanna search: ")
ulist=[]
z=0
for i in search(browser,stop=3):
	ulist.append(i)
	print(i)
	url=pyqrcode.create(ulist[z])
	url.svg("qr"+str(z) + ".svg",scale=10 )
	z=z+1
	print(url.terminal())
