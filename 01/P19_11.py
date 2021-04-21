# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
nus=int(input("組數為:"))
for isc in range(1,nus+1):
    cas=input(f"第{isc}組:").split()
    cal=(int(cas[0])*250)+(int(cas[1])*175)
    print(f"第{isc}組應收費用:",str(cal))