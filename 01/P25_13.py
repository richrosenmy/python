# -*- coding: utf-8 -*-
"""
Created on Sun Apr  4 13:40:33 2021

@author: Asus
"""
import sys
wsc=input("檢測的字串(end 結束):")
if wsc=="end":
  print("檢測結束")
  sys.exit()
wss=input("檢測的單一字元:")
cal=wsc.count(wss)
print("字元",str(wss),"出現次數為:",str(cal))

