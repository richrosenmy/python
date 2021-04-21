sas=int(input('x軸座標:'))
wes=int(input('\ny軸座標:'))
a1=(sas-0)**2+(wes-0)**2
if sas==0 and wes==0:
 print('該點位於原點')
if sas>0 and wes>0:
 print('該點位於第一象限，','離原點距離為根號',str(a1))
if sas==0 and wes>0:
  print('該點位於上半平面y軸上，','離原點距離為根號',str(a1))
if sas<0 and wes==0:
  print('該點位於左半平面x軸上，','離原點距離為根號',str(a1))

