# import required module
# requires cryptography
from cryptography.fernet import Fernet

# opening the key
with open('filekey.key', 'rb') as filekey:
    key = filekey.read()
 
# using the generated key
fernet = Fernet(key)
 
# opening the original file to encrypt
with open('app.py', 'rb') as file:
    encrypted = file.read()
     
# encrypting the file
decrypted = fernet.decrypt(encrypted)
 
# opening the file in write mode and
# writing the encrypted data
with open('dec_app.py', 'wb') as decrypted_file:
    decrypted_file.write(decrypted)