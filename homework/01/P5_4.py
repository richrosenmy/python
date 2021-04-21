tus=int(input('請輸入階乘值M:'))
wa=1
ws=1
while wa<tus:
 ws=ws+1
 wa=wa*ws
print('超過M為',str(tus),'的最小階乘N值為:',str(ws))