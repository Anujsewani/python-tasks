#!/usr/bin/python3
import datetime
time=datetime.datetime.now()
name=input("enter your name ")
if time.hour<12 and time.hour>4:
	print('good morning ',name)
elif time.hour>=12 and time.hour<16:
	print('good afternoon ',name)
elif time.hour>=16 and time.hour<22:
	print('good evening ',name)
elif time.hour>=22 and time.hour<=4:
	print('good night ',name)

