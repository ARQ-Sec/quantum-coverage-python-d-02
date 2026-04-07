from cryptography.hazmat.primitives.asymmetric import rsa

def execute():
    # rule_key: quantum.arq-q-0312-python
    key = rsa.generate_private_key(public_exponent=65537, key_size=2048)
    RSA = key

if __name__ == '__main__':
    execute()
