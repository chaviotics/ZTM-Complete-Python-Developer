username = 'Chav'
password = 'imomama'
 
password_len = len(password)
password_encrypted = '*' * password_len

print(f"{username}, your {'*' * len(password)}, is {len(password)} letters long.")