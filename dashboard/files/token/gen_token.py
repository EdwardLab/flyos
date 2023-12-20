import secrets
import string

def generate_random_token(length=16):
    alphabet = string.ascii_letters + string.digits
    token = ''.join(secrets.choice(alphabet) for _ in range(length))
    return token

random_token = generate_random_token(20)
with open('/flyos/files/token/token', 'w') as tokenfile:
    tokenfile.write(random_token)
print("Random Token:", random_token)
