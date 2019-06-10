#!/bin/python3
x=[]
y=[]
adhoc=[1,2,3,1,4,5,66,22,2,6,0,9]
for i in adhoc :
	if i>5 :
		x.append(i)
	elif i<=2 :
		y.append(i)
print(x,"numbers which are greater than 5")
print(y,"numbers which are less than or equal to 2")
	

