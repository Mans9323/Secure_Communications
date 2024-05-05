from Crypto.Util.number import *
from pwn import remote
import json

x = 0x372f0e88f6f7189da7c06ed49e87e0664b988ecbee583586dfd1c6af99bf20345ae7442012c6807b3493d8936f5b48e553f614754deb3da6230fa1e16a8d5953a94c886699fc2bf409556264d5dced76a1780a90fd22f3701fdbcb183ddab4046affdc4dc6379090f79f4cd50673b24d0b08458cdbe509d60a4ad88a7b4e2921

with open('output_d8d7a60bdc52b56d3be6f24a000f40cd.txt') as f:
    f.readline(); f.readline()
    N = e = c = 0
    exec(f.read())

p = None
for i in range(16):
    num = pow(x, 2 ** i, N) - 1
    if GCD(num, N) not in [1, N]:
        p = GCD(num, N)
        break
num = pow(x, 2 ** 15, N) + 1
if GCD(num, N) not in [1, N]:
    p = GCD(num, N)
if p:
    q = N // p
    flag = pow(c, inverse(e, (p - 1) * (q - 1)), N)
    print(long_to_bytes(flag).decode())
else:
    print('Nope')