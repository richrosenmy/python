# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

chi=int(input("國文:"))
eng=int(input("英文:"))
math=int(input("微積分:"))
phc=int(input("體育:"))
inc=int(input("程式設計:"))
nuc=list()
n1=nuc.append(chi)
n2=nuc.append(eng)
n3=nuc.append(math)
n4=nuc.append(phc)
n5=nuc.append(inc)
ang=sum(nuc)/5
anc=int(ang)
print("平均分數:",str(round(anc,2)))
hig=max(nuc)
losr=min(nuc)
print("最高分科目:",str(hig))
print("最低分科目:",str(losr))
