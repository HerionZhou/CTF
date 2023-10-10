import re
#GET /index.php?act=news&id=1%20and%20ascii(substr(((select%20concat_ws(char(94),%20flag)%20%20from%20db_flag.tb_flag%20%20limit%200,1)),%2038,%201))>125

a=[]
with open("sqltest.pcapng","rb") as f: # rb：以二进制读取
    for i in f.readlines():
        if b"id=1%20and%20ascii(substr(((select%20concat_ws(char(94),%20flag)%20%20from%20db_flag.tb_flag%20%20limit%200,1))," in i:
            a.append(i.strip())

a1={}
for i in a:
    b=re.search(br"%200,1\)\),%20(\d+),%201\)\)>",i).group(1).decode() # (\d+) 匹配多个数字
    c=re.search(br"%201\)\)>(\d+) HTTP/1.1",i).group(1).decode()
    a1[int(b)]=int(c) # 使用字典不可重复性，获取最后一行的ascii码
print(a1)

flag=''
for i in range(1,39):
    flag+=(chr(a1[i])) # ascii转字符
print(flag)
