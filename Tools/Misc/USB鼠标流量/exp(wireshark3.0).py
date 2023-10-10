#sniffer.py
import os
#os.system("tshark -r test2.pcapng -T fields -e usb.capdata > usbdata.txt")
os.system("tshark -r test2.pcapng -T fields -e usbhid.data > usbdata.txt")
#sniffer.py
nums = []
keys = open('usbdata.txt','r')
result=open('result.txt','w')
posx = 0
posy = 0
for line in keys:
    if len(line) != 13 :#????
         continue
    x = int(line[4:6],16)
    y = int(line[6:8],16)
    if x > 127 :
        x -= 256
    if y >120 :#??????????????????????????????
        y -=264#??????????????????????????????????
    posx += x
    posy += y
    btn_flag = int(line[2:4],16)  # 1 for left , 2 for right , 0 for nothing
    if btn_flag == 1 :
        result.write(str(posx)+' '+str(-posy)+'\n')
print(result)
keys.close()
result.close()
