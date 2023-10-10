# -*- coding: utf-8 -*-
import subprocess

rar_name="11.rar"
#载入字典
with open('10000.txt',"r") as f:
    for p in f.readlines():
        cmd = "rar.exe e {0} -y -p{1}".format(rar_name,p.strip())
        r = subprocess.getstatusoutput(cmd)
        # print(r)
        # print(r[0])
        if r[0] == 0:
            print("pass = %s" % p)
             break
#纯数字爆破
for p in range(0,999999):
    cmd = "rar.exe e {0} -y -p{1}".format(rar_name,str(p))
    r = subprocess.getstatusoutput(cmd)
    if r[0] == 0:
        print("pass = %s" % p)
        breakrar5.0爆破