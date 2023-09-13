from gmpy2 import *
from Crypto.Util.number import getPrime, long_to_bytes, bytes_to_long

c = 
n = 
p = 
q =

phi = (p - 1) * (q - 1)

e = 0x10001 #65537

d = gmpy2.invert(e, phi)

m = pow(c, d, n)
flag = long_to_bytes(m)
print(flag)