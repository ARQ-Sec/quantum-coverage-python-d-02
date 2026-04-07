import bcrypt

def execute():
    # rule_key: quantum.arq-q-0316-python
    bcrypt.hashpw(b"password", bcrypt.gensalt())

if __name__ == '__main__':
    execute()
