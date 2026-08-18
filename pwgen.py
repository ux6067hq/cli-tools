#!/usr/bin/env python3
import secrets, string

def generate(length=16):
    chars = string.ascii_letters + string.digits
    return ''.join(secrets.choice(chars) for _ in range(length))

if __name__ == '__main__':
    print(generate())
