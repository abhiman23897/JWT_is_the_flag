# JWT_is_the_flag

## Description

CTF developed for UMass CS 561: System Defense and Test class in Spring 2023. This CTF requires knowledge of:
- Python 3
- Python package - cryptography
- JWT (JSON web tokens)

This CTF aims at demonstrating the power of manipulating the JWT token, which is used for authorization in many enterprises today, to gain higher privileges on a website. Using these privileges, the user will be able to perform malicious activity. Hence, it is very important to use a secure key for performing the JWT token generation, and to not store the key within the code file. They secret keys should be set as environment variables, and should be stored in a secure location.

For the user to become aware of the flaw in the design of JWT in this CTF, they have to first inspect the source code. This is also encrypted using basic python cryptography library. Here, the flaw is that while creating the zip file for the source code, I have also added the key file used to encrypt the source code. To decrypt this, user must use the provided filekey.key file and the python cryptography package. Once the user has the source code, they can inspect the app.py file to find out how to login to the application.

The frontend for this code has been setup using React.js. However, this does not play much role in capturing the flag. Hence, React.js knowledge is absolutely not required.

## How to run

To run the docker container for this CTF, follow the steps below:
- Use the following command in the directory of the repository: 
```bash
docker-compose up --build -d
```

## Solution
The solution for this CTF is as follows:
- Decrypt the source_code.zip to find out how to login to the application
   - Read about the cryptography package here: https://cryptography.io/en/latest/
   - Use the filekey.key file to decrypt the app.py file in source_code.zip: 
        ```python
        from cryptography.fernet import Fernet

        with open('filekey.key', 'rb') as filekey:
            key = filekey.read()
        fernet = Fernet(key)

        with open('app.py', 'rb') as file:
            encrypted = file.read()
        decrypted = fernet.decrypt(encrypted)
        
        with open('app.py', 'wb') as decrypted_file:
            decrypted_file.write(decrypted)
        ```
- Inspect app.py to find the following holes:
   - Username and password can be any alphanumeric string of 10 characters to login.
   - Logging in generates a JWT token with the secret key mentioned in the file.
   - The flag file only checks if JWT token using the secret key has "is_admin" set to true.
- Use the browser's developer tools to inspect the JWT token generated after logging in.
- Go to jwt.io, change the "is_admin" value to true, use the secret found in app.py and paste the token back in the browser's local storage.
- Refresh the page and click on the flag button to get the flag.
## Flag Value
- CTF_SDaT{jWT_R0cKs!_f4H18@}
