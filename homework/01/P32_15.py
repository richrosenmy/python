# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""


nus=int(input("請輸入一正整數:"))
if nus%2==0 and nus%11==0  and nus%5!=0 and nus%7!=0:
    print(str(nus),"為新公倍數?:","Yes")
else:
    print(str(nus),"為新公倍數?:","No")