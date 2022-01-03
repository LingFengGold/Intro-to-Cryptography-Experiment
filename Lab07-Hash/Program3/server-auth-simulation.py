from __future__ import annotations
from typing import Dict
import os
import getpass
import hashlib

database: Dict[str, UserPassword] = dict()


class UserPassword:
    def __init__(self):
        self.username: str = ''
        self.password_hash: bytes = b''
        self.salt: bytes = b''
        self.method: str = 'scrypt'

    def verify_password(self, password: str) -> bool:
        # TODO
        password_bytes: bytes = bytes(password, encoding="utf8")
        password_hash: bytes = hashlib.scrypt(password_bytes, salt=self.salt, n=4, r=8, p=16)
        if password_hash == self.password_hash:
            return True


def database_add_item(user: UserPassword) -> None:
    if user.username in database:
        raise Exception('User {} already exists.'.format(user.username))
    database[user.username] = user


def login_user(username: str, password_plaintext: str) -> bool:
    if username not in database:
        raise Exception('User {} does not exist.'.format(username))
    return database[username].verify_password(password_plaintext)


def register_user(username: str, password_plaintext: str) -> None:
    # TODO
    password_bytes: bytes = bytes(password_plaintext, encoding="utf8")
    salt_bytes: bytes = os.urandom(21)
    password_hash: bytes = hashlib.scrypt(password_bytes, salt=salt_bytes, n=4, r=8, p=16)
    user = UserPassword()
    user.username = username
    user.password_hash = password_hash
    user.salt = salt_bytes
    database_add_item(user)


if __name__ == '__main__':
    while True:
        try:
            print('Usage:')
            print('\tR - register a new user')
            print('\tL - login with an existing user')
            print('\tQ - exit')
            print('')
            command: str = input('Input command:')
            if command == 'Q':
                exit(0)
            elif command == 'R' or command == 'L':
                username: str = input('Input username:')
                # password: str = getpass.getpass('Input password:') # will not work properly for PyCharm, IDLE, etc.
                password: str = input('Input password:')
                if command == 'R':
                    register_user(username, password)
                    print('User created successfully.')
                elif command == 'L':
                    login_valid: bool = login_user(username, password)
                    if login_valid:
                        print('User logged in successfully.')
                    else:
                        print('Password verification failed. Can not logged in.')
                else:
                    assert False
            else:
                raise Exception('Invalid command.')
        except Exception as e:
            print('Error: {}'.format(e))
