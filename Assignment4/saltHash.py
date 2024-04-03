import hashlib
import os

print(os.getcwd())

# List of given password hashes
password_hashes = [
    "2834da08d58330d8dafbb2ac1c0f85f6b3b135ef",
    "92e54f10103a3c511853c7098c04141f114719c1",
    "437fbc6892b38db6ac5bdbe2eab3f7bc924527d9",
    "fafa4483874ec051989d53e1e432ba3a6c6b9143",
    "06f6fe0f73c6e197ee43eff4e5f7d10fb9e438b2",
    "f44f3b09df53c1c11273def13cacd8922a86d48c"
]

with open('rockyou.txt', 'r') as f:
    for line in f:
        # Remove trailing newline character
        password = line.strip()
        salt = "www.exploringsecurity.com"

        # Compute the hash: sha1($pass.$salt)
        salted_password1 = password + salt
        hash1 = hashlib.sha1(salted_password1.encode()).hexdigest()

        # Compute the hash: sha1($salt.$pass)
        salted_password2 = salt + password
        hash2 = hashlib.sha1(salted_password2.encode()).hexdigest()

        # Compute the hash: sha1(sha1($pass).$salt)
        inner_hash3 = hashlib.sha1(password.encode()).hexdigest()
        salted_password3 = inner_hash3 + salt
        outer_hash3 = hashlib.sha1(salted_password3.encode()).hexdigest()

        # Compute the hash: sha1($salt.sha1($pass))
        salted_password4 = salt + inner_hash3
        hash4 = hashlib.sha1(salted_password4.encode()).hexdigest()

        # Compute the hash: sha1($salt.$pass.$salt)
        salted_password5 = salt + password + salt
        outer_hash5 = hashlib.sha1(salted_password5.encode()).hexdigest()

        # Compute the hash: sha1(sha1($salt.$pass.$salt))
        inner_hash6 = hashlib.sha1(salted_password5.encode()).hexdigest()
        salted_password6 = salt + inner_hash6
        outer_hash6 = hashlib.sha1(salted_password6.encode()).hexdigest()

        # Compute the hash: sha1($pass.$salt.$pass)
        salted_password7 = password + salt + password
        hash7 = hashlib.sha1(salted_password7.encode()).hexdigest()

        # Compute the hash: sha1($pass.$salt.$pass.$salt)
        salted_password8 = password + salt + password + salt
        hash8 = hashlib.sha1(salted_password8.encode()).hexdigest()

        # Compute the hash: sha1(sha1($pass.$salt.$pass))
        inner_hash9 = hashlib.sha1(salted_password7.encode()).hexdigest()
        salted_password9 = inner_hash9 + salt
        hash9 = hashlib.sha1(salted_password9.encode()).hexdigest()

        
        # If the hash is in the list of password hashes, print the full salted password and the hash
        if hash1 in password_hashes:
            print(f"Found password: {salted_password1}, Hash1: {hash1}")
        # if hash2 in password_hashes:
        #     print(f"Found password: {salted_password2}, Hash2: {hash2}")
        if outer_hash3 in password_hashes:
            print(f"Found password: {salted_password3}, Hash3: {outer_hash3}")
        if hash4 in password_hashes:
            print(f"Found password: {salted_password4}, Hash4: {hash4}")
        if outer_hash5 in password_hashes:
            print(f"Found password: {salted_password5}, Hash5: {outer_hash5}")
        if outer_hash6 in password_hashes:
            print(f"Found password: {salted_password6}, Hash6: {outer_hash6}")
        if hash7 in password_hashes:
            print(f"Found password: {salted_password7}, Hash7: {hash7}")
        if hash8 in password_hashes:
            print(f"Found password: {salted_password8}, Hash8: {hash8}")
        if hash9 in password_hashes:
            print(f"Found password: {salted_password9}, Hash9: {hash9}")
        
