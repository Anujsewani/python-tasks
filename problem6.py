#!/usr/bin/python
from googlesearch import search
#import speech_recognition

options = '''
Press 1 to type topic
Press 2 to for mic
'''
print(options)
choice = input("Enter your choice:")
url =[]
if choice == '1' :
	web=input("Please enter topic:")
	for i in search(web,tld="co.in",pause=2,num=5,stop=10):
        	url.append(i)
        	f=open('urls.txt','a+')
	for i in url:
		f.write(i+'\n')
	f.seek(0)
	print(f.read())
	f.close()
elif choice == '2' :
	print("program still in process")
else :
	print("Enter correct choice!!!!")
