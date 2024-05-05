from pwn import *  
from Crypto.Cipher import AES  
from Crypto.Util.Padding import pad  
import json  
def bxor(a, b):  
    return bytes(x ^ y for x, y in zip(a, b))  
starter = b"a" * 16  
p = remote('socket.cryptohack.org',13388)  
payload = {"option": "sign", "message": starter.hex()} # Get the signature of our dummy text  
p.recvline()  
p.sendline(json.dumps(payload)) 
response = json.loads(p.recvline().decode())
signature = bytes.fromhex(response['signature'])
wanted = pad(b"admin=True",16) 
# Compute our new signature by completing the final step
newhash = bxor(AES.new(wanted,AES.MODE_ECB).encrypt(signature),signature) 
# Pad the starter(as that is what the server will have done) then append admin=True
# This gets the message for which we have generated the signature
newmessage = pad(starter,16) + b"admin=True"
payload = {"option": "get_flag", "message": newmessage.hex(), "signature": newhash.hex()}  
p.sendline(json.dumps(payload))  
print(p.recvline())