# JWT_is_the_flag

## Description

CTF developed for UMass CS 561: System Defense and Test class in Spring 2023. This CTF requires knowledge of:
- Python 3
- JWT (JSON web tokens)

This CTF aims at demonstrating the power of manipulating the JWT token, which is used for authorization in many enterprises today, to gain higher privileges on a website. Using these privileges, the user will be able to perform malicious activity. Hence, it is very important to use a secure key for performing the JWT token generation, and to not store the key within the code file. 

For the user to become aware of the flaw in the design of JWT in this CTF, they have to inspect the source code. This is also encrypted using basic python cryptography library. To decrypt this, user must use the provided filekey.key file and decrypt the source_code.zip provided. 

The frontend for this code has been setup using React.js. However, this does not play much role in capturing the flag. Hence, React.js knowledge is absolutely not required.

## Solution
- Decrypt the source_code.zip to find out how to login to the application
- Username and password can be any alphanumeric string of 10 characters to login.
- On logging in, non admin JWT token will be generated and provided to user. 
- Inspect app.py in the source code to find the JWT secret key - super_secret_key@123
- Using this, encode new JWT token with same payload and headers, except for is_admin being set to true.
- Use new token to view flag content.

## Flag Value
- CTF_SDaT{jWT_R0cKs!_f4H18@}
