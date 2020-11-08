# -*- coding: utf-8 -*-
"""
Created on Mon Oct  7 12:42:04 2019

@author: morei
"""
num = int(input())
sum = 0
num1 = num
while num1!=0:
    i = num1%10
    sum += i**3
    num1 = num1//10
if sum==num:
    print(True)
else:
    print(False)
    
