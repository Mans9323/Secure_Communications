from math import gcd
from Crypto.Util.number import long_to_bytes
from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP

def egcd(a, b):
    if a == 0:
        return (b, 0, 1)
    else:
        gcd, x, y = egcd(b % a, a)
        return (gcd, y - (b//a) * x, x)
    pass

def decrypt(info, debug=False):
    phi = (info['q'] - 1) * (info['p'] - 1)
    _,a,b = egcd(phi, info['e'])
    d = b % phi
    assert (info['e'] * d) % phi == 1

    if debug:
        print("[-] id:", info['id'])
        print("[-] n:", info['n'])
        print("[-] e:", info['e'])
        print("[-] c:", info['c'])
        print("[-] p:", info['p'])
        print("[-] q:", info['q'])
        print("[-] d:", d)

    key = RSA.construct((info['n'], info['e'], d))
    cipher = PKCS1_OAEP.new(key)

    c = bytes.fromhex(info['c'].decode())

    print("[+] flag:", cipher.decrypt(c))
    pass

ns = []
for i in range(1, 51):
    key = RSA.importKey(open("keys_and_messages/%d.pem" % i, "rb").read())

    n = key.n
    e = key.e

    with open("keys_and_messages/%d.ciphertext" % i, "rb") as f:
        c = f.read()

    ns.append({'id':i, 'n':n, 'e':e, 'c':c})

for i1 in range(len(ns)):
    n1 = ns[i1]
    if 'p' in n1 or 'q' in n1:
        continue
    for n2 in ns:
        if n1['n'] == n2['n']:
            continue
        if 'p' in n2 and not n1['n'] % n2['p']:
            p = n2['p']
        else:
            # if n1['n'] and n2['n'] have a prime factor in common, gcd will find it 
            p = gcd(n1['n'], n2['n'])
        if p != 1:
            print("[+] factor found")

            q1 = n1['n'] // p
            assert n1['n'] == q1 * p
            n1['q'] = q1
            n1['p'] = p

            q2 = n2['n'] // p
            assert n2['n'] == q2 * p
            n2['q'] = q2
            n2['p'] = p

            decrypt(n1)
            decrypt(n2)

            break