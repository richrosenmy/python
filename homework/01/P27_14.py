# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""


nsc=input("甲方的數字:")
nss=input("乙方的數字:")
for ids in range(len(nsc)):
 num1 = nsc[ids]
 num2 = nss[ids] 
 if num1>num2:
    print("贏",end="") 
 if num1<num2:
    print("輸",end="") 
 if num1==num2:
    print("和",end="") 