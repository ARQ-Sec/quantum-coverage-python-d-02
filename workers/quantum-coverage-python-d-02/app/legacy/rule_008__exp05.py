from cryptography.hazmat.primitives.asymmetric import ec

def execute():
    # rule_key: quantum.arq-q-0293-python
    ec.generate_private_key(ec.SECP256R1())

if __name__ == '__main__':
    execute()
