import json
from hashlib import md5
from Crypto.Util.number import *
from pwn import *

## Unintended solution: consider a known MD5 collision with 1-block messages,
## e.g., https://eprint.iacr.org/2010/643.pdf
m0 = bytes.fromhex("0e306561559aa787d00bc6f70bbdfe3404cf03659e704f8534c00ffb659c4c8740cc942feb2da115a3f4155cbb8607497386656d7d1f34a42059d78f5a8dd1ef")
m1 = bytes.fromhex("0e306561559aa787d00bc6f70bbdfe3404cf03659e744f8534c00ffb659c4c8740cc942feb2da115a3f415dcbb8607497386656d7d1f34a42059d78f5a8dd1ef")
assert md5(m0).hexdigest() == md5(m1).hexdigest()

## Now, observe that these messages are 64-byte long, 
## which allows to extend them by whatever 64-byte common suffix to match the challenge dimensions.
## We do so by iterating over a small space to get a prime p0
cnt = 0
while True:
	s = long_to_bytes(cnt, 4)
	if isPrime(bytes_to_long(m0 + s)):
		break
	cnt += 1

p0 = m0 + s
p1 = m1 + s

assert md5(p0).hexdigest() == md5(p1).hexdigest()
assert isPrime(bytes_to_long(p0))
assert not isPrime(bytes_to_long(p1))
assert bytes_to_long(p1) % 42487 == 0 ## Obtained from PollardRho on p1

c = remote("socket.cryptohack.org", 13392)
c.recvline()

sign = {
	"option": "sign",
	"prime": str(bytes_to_long(p0))
}
c.sendline(json.dumps(sign))
r = c.recvline()
sig = json.loads(r)["signature"]


check = {
	"option": "check",
	"prime": str(bytes_to_long(p1)),
	"a": 42487,
	"signature": sig
}
c.sendline(json.dumps(check))
flag = c.recvline()
print(flag.decode())

c.close()