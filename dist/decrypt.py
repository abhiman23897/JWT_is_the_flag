# import required module
# requires cryptography
from cryptography.fernet import Fernet

# opening the key
with open('filekey.key', 'rb') as filekey:
    key = filekey.read()
 
# using the generated key
fernet = Fernet(key)
 
# opening the original file to decrypt
with open('app.py', 'rb') as file:
    encrypted = file.read()
     
# decrypting the file
decrypted = fernet.decrypt(encrypted)
 
# opening the file in write mode and
# writing the decrypted data
with open('app.py', 'wb') as decrypted_file:
    decrypted_file.write(decrypted)