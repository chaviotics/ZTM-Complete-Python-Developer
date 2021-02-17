import re



password_pattern = re.compile(r"[a-zA-Z0-9$%^&]{8,}\d") # should be ([A-Za-z0-9$%#@]{7,}[0-9])
password = 'superscret123$%^&1'

check = password_pattern.fullmatch(password)
print(check)