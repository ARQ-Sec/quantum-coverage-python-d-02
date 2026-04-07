from argon2 import PasswordHasher

def execute():
    # rule_key: quantum.arq-q-0317-python
    PasswordHasher().hash("password")

if __name__ == '__main__':
    execute()
