# -*- coding: utf-8 -*-
"""
Created on Sun Mar 28 11:38:20 2021

@author: Asus
"""

nus=input("輸入值為:").split(",")
nus.sort()
ans="".join(nus)
nus.sort(reverse=True)
ans1="".join(nus)
cal=int(ans1)-int(ans)
print("最大值數列與最小值數列差值為:",str(cal))
