#!/usr/bin/python3.8
# -*- coding: utf-8 -*-
import requests
import zipfile
import binascii
import string

def title():
    print('+-----------------------------------------------------+')
    print('+              渊龙Sec安全团队CTF工具包               +')
    print('+              团队公开QQ群：877317946                +')
    print('+             Title: CRC-Tools,so easy!!!             +')
    print('+     python3 ReadZip.py --> ReadZip >>> Demo.zip     +')
    print('+                作者：曾哥（AabyssZG）               +')
    print('+                  版本：V1.1优化版                   +')
    print('+-----------------------------------------------------+')

def ReadCRC(zipname):
    zip_url = "./" + zipname
    file_zip = zipfile.ZipFile(zip_url)    #用zipfile读取指定的压缩包文件
    name_list = file_zip.namelist()        #使用一个列表，获取并存储压缩包内所有的文件名
    crc_list = []
    crc32_list = []
    print('+--------------遍历指定压缩包的CRC值----------------+')
    for name in name_list:
    	name_message = file_zip.getinfo(name)
    	crc_list.append(name_message.CRC)
    	crc32_list.append(hex(name_message.CRC))
    	print('[OK] {0}: {1}'.format(name,hex(name_message.CRC)))
    print('+-------------对输出的CRC值进行碰撞-----------------+')
    comment = ''
    chars = string.printable
    for crc_value in crc_list:
        for char1 in chars:
            thicken_crc = binascii.crc32(char1.encode()) #获取任意1Byte字符串的CRC32值
            calc_crc = thicken_crc & 0xffffffff          #将任意1Byte字符串的CRC32值与0xffffffff进行与运算
            if calc_crc == crc_value:                    #匹配两个CRC32值
                print('[+] {}: {}'.format(hex(crc_value),char1))
                comment += char1
    print('+-----------------CRC碰撞结束！！！-----------------+')
    crc32_list = str(crc32_list)
    crc32_list = crc32_list.replace('\'' , '')
    print("读取成功，导出CRC列表为：" + crc32_list)                     #导出CRC列表
    print('CRC碰撞成功，结果为: {}'.format(comment))                    #输出CRC碰撞结果

if __name__ == '__main__':
    title()
    zipname = str(input("请输入压缩包名字：\nReadZip >>> "))
    ReadCRC(zipname)