# CTF
---
CTF工具合集

##目录
1.[Crypto](#Crypto)
2.[Forensics](#Forensics)
3.[Misc](#Misc)
4.[Reverse](#Reverse)
5.[Web](#Web)

---
##<span id="Crypto">1.Crypto
####1.CaptfEncoder
综合密码加解密工具
####2.CyberChef
网页版综合密码加解密工具
####3.Passware Kit
密码破解工具，可破解excel、zip等密码，也可破解镜像、内存等登录密码
####4.Ziperello
zip压缩包密码破解工具
####5.AsteriskPassword
星星密码查看器，光标移动到*号位置，可显示明文
####6.CTFcrackTools
CTF密码解密工具，支持栅栏 凯撒 摩斯 Base64 Url编码 Unicode等多种解码方式
####7.ZipCenOp
zip伪加密压缩包修复工具
`java -jar ZipCenOp.jar r yourzip.zip`
####8.yafu
RSA N分解工具
```
yafu-x64.exe factor(N)
N太长会报错，需要保存在文件中，txt文件结尾需要添加一个换行符
yafu-x64.exe factor(@) -batchfile n.txt
```
####9.RSA2/RSA4
RSA求解脚本
####10.rsatool
RSA解密工具
生成私钥：
`python rsatool.py -p **** -q **** -e **** -o pri.pem -f PEM`
通过私钥解密：
`openssl rsautl -decrypt -in flag.enc -inkey pri.pem -out flag.txt`
####11.URL编码解码
URL编码解码工具
####12.morsecoder.py
摩斯密码加密解密脚本
##<span id="Forensics">2.Forensics
####1.volatility

##<span id="Misc">3.Misc
##<span id="Reverse">4.Reverse
##<span id="Web">5.Web

