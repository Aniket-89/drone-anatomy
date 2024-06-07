import secrets
import string

def generate_secret_key(length=20):
    alphabet = string.ascii_letters + string.digits
    return ''.join(secrets.choice(alphabet) for _ in range(length))

# Example usage:
secret_key = generate_secret_key(32)
print(secret_key)