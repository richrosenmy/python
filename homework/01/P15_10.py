# -*- coding: utf-8 -*-
"""
Created on Sun Mar 28 12:34:09 2021

@author: Asus
"""

nus=input("輸入一組四位數字為:")
cal=[str((int(i)+7)%10) for i in nus]
cas=cal[0],cal[2],cal[1],cal[3]
ws=sorted(cas)
ans="".join(ws)
print("輸出加密後的數字為:",str(ans))