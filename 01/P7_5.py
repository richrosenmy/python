# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
nus=input('輸入月租費形式及通話時間為:').split(',')

a1=int(nus[1])*0.09
if a1<=186 and int(nus[0])==186:
       print('通話費為:186')
if a1<=186*2 and int(a1[0])==186:
      a2=int(nus[1])*0.09*0.9
      print('通話費為:',int(round(a2,1)))
if a1>186*2   and int(nus[0])==186:
      a3=int(nus[1])*0.09*0.8
      print('通話費為:',int(round(a3,1)))
 

a4=int(nus[1])*0.08
      
if a4<=386 and int(nus[0])==386:
       print('通話費為:386')
if a4<=386*2 and int(nus[0])==386:
        a5=int(nus[1])*0.08*0.8
        print('通話費為:',int(round(a5,1)))
if a4>386*2 and int(nus[0])==386:
          a6=int(nus[1])*0.08*0.7
          print('通話費為:',int(round(a6,1)))

a7=int(nus[1])*0.07
if a7<=586 and int(nus[0])==586:
          print('通話費為:586')
if a7<=586*2 and int(a1[0])==586:
       a8=int(nus[1])*0.07*0.7
       print('通話費為:',int(round(a8,1)))
if a7>586*2 and int(nus[0])==586:
      a9=int(nus[1])*0.07*0.6
      print('通話費為:',int(round(a9,1)))
   
e1=int(nus[1])*0.06
if e1<=986 and int(nus[0])==986:
     print('通話費為:986')
if e1<=986*2 and int(nus[0])==986:
       e2=int(nus[1])*0.06*0.6
       print('通話費為:',int(round(e2,1)))
if e1>986*2 and int(nus[0])==986:
         e3=int(nus[1])*0.06*0.5
         print('通話費為:',int(round(e3,1)))
         

    