# encoding:utf-8
import os
import os.path
import sys
import subprocess

#打印可打印字符串
def str_re(str1):
    str2=""
    for i in str1.decode('utf8','ignore'):
        try:
            #print(ord(i))
            if ord(i) <= 126 and ord(i) >= 33:
                str2 += i
        except:
                str2 += ""
    #print(str2)
    return str2


#写入文本函数
def txt_wt(name,txt1):
    with open("output.txt","a") as f:
        f.write('filename:'+name)
        f.write("\n")
        f.write('flag:'+txt1)
        f.write("\n")

#第一次运行，清空output文件
def clear_txt():
    with open("output.txt","w") as f:
        print("clear output.txt！！！")

# 递归遍历的所有文件
def file_bianli():
    # 路径设置为当前目录
    path = os.getcwd()
    # 返回文件下的所有文件列表
    file_list = []
    for i, j, k in os.walk(path):
        for dd in k:
            if ".py" not in dd  and "output.txt" not in dd:
                file_list.append(os.path.join(i, dd))
    return file_list

#查找文件中可能为flag的字符串

def flag(file_list,flag):
    for i in file_list:
        try:
            with open(i,"rb") as f:
                for j in f.readlines():
                    j1=str_re(j)#可打印字符串
                    #print j1
                    for k in flag:
                        if k in j1:
                            txt_wt(i, j1)
                            print('filename:',i)
                            print('flag:',j1)
        except:
            print('err')

flag_txt = ['flag{', '666c6167','flag','Zmxh','&#102', '666C6167', 'FLAG{', 'FLAG', 'RkxB', '464c4147']

#清空输出的文本文件
clear_txt()
#遍历文件名
file_lt=file_bianli()
#查找flag关键字
flag(file_lt,flag_txt)
