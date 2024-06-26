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
        # Hash Format : sha1($salt.$pass)
        salt_password = salt + password
        hash = hashlib.sha1(salt_password.encode()).hexdigest()

        if hash in password_hashes:
            print(f"Found password: {password}, hash: {hash}")