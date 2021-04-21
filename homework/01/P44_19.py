# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""


ms=int(input())
da=int(input())
cal=(ms*2+da)%3
if cal==0:
   print("普通")
if cal==1:
    print("吉")
if cal==2:
    print("大吉")