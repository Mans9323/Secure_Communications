# We convert the ssh public key to PEM format and store it in a file called "bruce_rsa.pem"
# ssh-keygen -f bruce_rsa.pub -e -m pem > bruce_rsa.pem

# Finally, retrieve the modulo with the following code:

from Crypto.PublicKey import RSA

f = open('bruce_rsa_6e7ecd53b443a97013397b1a1ea30e14.pub', 'r')
pubkey = RSA.import_key(f.read())

print(pubkey.n)