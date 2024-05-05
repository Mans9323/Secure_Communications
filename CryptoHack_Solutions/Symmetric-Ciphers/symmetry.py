import requests

url_base = 'http://aes.cryptohack.org/symmetry'

BLOCK_SIZE = 16

def hack():
  response = requests.get(url="%s/encrypt_flag/" % url_base).json()
  ciphertext = bytes.fromhex(response['ciphertext'])

  # Split the ciphertext into the IV and the actual ciphertext
  iv, ciphertext = ciphertext[:BLOCK_SIZE], ciphertext[BLOCK_SIZE:]

  # Encrypt the ciphertext (E_K(IV) ^ FLAG) which just will encrypt the supplied
  # IV as E_K(IV) and XOR it with the ciphertext and recover the flag. Abuses
  # the fact that encryption and decryption perform the same operation in OFB mode.
  response = requests.get(url="%s/encrypt/%s/%s" % (url_base, ciphertext.hex(), iv.hex())).json()
  plaintext = bytes.fromhex(response['ciphertext'])
  return plaintext.decode()

if __name__ == '__main__':
  flag = hack()
  print(flag)