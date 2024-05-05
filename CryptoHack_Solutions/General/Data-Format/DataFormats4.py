# verben, solution to the Transparency challenge from cryptohack.org
# this solution uses only crt.sh certificate transparency database
# this python script will print the flag without any user's manual intervention
"""
steps: 
  1) get sha256 digest of DER subject public key
  2) search by this value in crt.sh, this will provides us with the certificate that has this SPKI
  3) get the PEM certificate and parse it's content in order to get the commonName attribute
  4) query the commonName and get the flag
"""
from Crypto.PublicKey import RSA
import OpenSSL
import hashlib
import json
import requests
from OpenSSL.crypto import load_certificate
## 1) get the sha256 digest of the DER public key
pem = open("transparency_afff0345c6f99bf80eab5895458d8eab.pem", "r").read() # open the PEM provided file
rsa_key = RSA.importKey(pem).public_key()
der = rsa_key.exportKey(format='DER') # make DER format of our provided PEM in order to make searchable digest
digest = hashlib.sha256(der).hexdigest() # get the sha256 digest of the DER public key, we will search by this value in crt.sh
## 2) search for certificate that has this specific SPKI 
ua = 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:40.0) Gecko/20100101 Firefox/40.1' # a user agent for my requests
spki_url = "https://crt.sh/?spkisha256={hash}&output=json" # this is the crt.sh subject public key info attribute search URL
# the output=json attribute is an option from crt.sh to output json data instead of HTML 
req = requests.get(spki_url.format(hash=digest), headers={'User-Agent': ua})
content = req.content.decode('utf-8')
data = json.loads(content)
id = data[0]["id"] # get the certificate id of that specific subject public key
download_url = "https://crt.sh/?d={id}" # this is the crt.sh certificate donwload url, it download the PEM certificate
req = requests.get(download_url.format(id=id), headers={'User-Agent': ua})
PEMcert = req.content.decode('utf-8') # this is the PEM certificate that contains that particular SPKI
## 3) grab the common Name field:
cert = load_certificate(OpenSSL.crypto.FILETYPE_PEM, PEMcert) # returns an X.509 object 
CN = cert.get_subject().commonName # get the commonName of that certificat's subject
print("The certificate subject's commonName is:", CN) # print CN of the subject
## 4) get the flag:
flag_url = "https://" + CN
req = requests.get(flag_url, headers={'User-Agent': ua})
flag = req.content.decode('utf-8')
print("Flag:", flag) # will print the flag crypto{thx_redpwn_for_inspiration}