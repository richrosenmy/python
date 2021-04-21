# -*- coding: utf-8 -*-
"""
Created on Mon Apr  5 11:46:09 2021

@author: Asus
"""


nos=int(input(""))
for ia in range(1,nos+1,2):
    ias="*"*ia
    print(ias.center(nos))
for ib in range(nos,0,-2):
    ibs="*"*ib
    print(ibs.center(nos))