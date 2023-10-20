import base64
import struct

with open("exp3.dat", "rb") as f:
    r = f.read()

# lst = list(base64.b64decode(r))
# lst.reverse()
#
# with open("flag.zip", "wb") as f:
#     for i in lst:
#         s = struct.pack('B', i)     # struct的pack函数把任意数据类型变成bytes
#         f.write(s)

with open('test.zip', 'wb') as f:
    f.write(base64.b64decode(r)[::-1])      # 直接转倒序