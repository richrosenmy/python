# -*- coding: utf-8 -*-
"""
Created on Sun Apr  4 12:12:13 2021

@author: Asus
"""

nus=int(input("輸入查詢學號為:"))
ncs=[["123","Tom","DTGD"],["456","Cat","CSIE"],["789","Nana","ASIE"],
["321","Lim","DBA"],["654","Won","FOD"]]
if nus==123:
 a1=ncs[0][0:3]
 a2=" ".join(a1)
 print("學生資料為:",str(a2))
if nus==456:
 a3=ncs[1][0:3]
 a4=" ".join(a3)
 print("學生資料為:",str(a4))
if nus==789:
 a5=ncs[2][0:3]
 a6=" ".join(a5)
 print("學生資料為:",str(a6))
if nus==321:
 a7=ncs[3][0:3]
 a8=" ".join(a7)
 print("學生資料為:",str(a8))
if nus==654:
 a9=ncs[4][0:3]
 a10=" ".join(a9)
 print("學生資料為:",str(a10))

