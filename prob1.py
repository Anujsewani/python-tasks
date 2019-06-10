#!/bin/python3
import datetime
name=input('please enter your name? \n')
age=int(input('please enter your age \n'))
date=datetime.datetime.now()
print(name, "will turn 95 years old in",(95-age)+date.year)

