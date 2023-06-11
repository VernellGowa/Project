import bcrypt 

def encrypt(password):
    password = password.encode('utf-8')
    
    hashedPassword = bcrypt.hashpw(password, bcrypt.gensalt())
    return hashedPassword

print(encrypt("mypasswordstring"))