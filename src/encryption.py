import bcrypt 

def encrypt(password):
    if password == '':
        raise ValueError("Password cannot be empty")
    
    password = password.encode('utf-8')
    hashedPassword = bcrypt.hashpw(password, bcrypt.gensalt())
    return hashedPassword
        
def decrypt(password, hashedPassword):
    if password == '':
        raise ValueError("Password cannot be empty")
    
    password = password.encode('utf-8')
    hashedPassword = hashedPassword.encode('utf-8')
    return bcrypt.checkpw(password, hashedPassword)

print(decrypt(encrypt("vernell")))