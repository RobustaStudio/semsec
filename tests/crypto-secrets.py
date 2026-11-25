import hashlib
import random

import requests
from Crypto.Cipher import AES


def store(password):
    # ruleid: robusta-py-crypto-md5-password
    return hashlib.md5(password.encode()).hexdigest()


def etag(body):
    # ok: robusta-py-crypto-md5-password
    return hashlib.md5(body).hexdigest()


def encrypt(key, data):
    # ruleid: robusta-py-crypto-ecb-mode
    cipher = AES.new(key, AES.MODE_ECB)
    return cipher.encrypt(data)


def encrypt_gcm(key, data):
    # ok: robusta-py-crypto-ecb-mode
    cipher = AES.new(key, AES.MODE_GCM)
    return cipher.encrypt_and_digest(data)


def reset_token():
    # ruleid: robusta-py-crypto-weak-random
    token = random.randint(100000, 999999)
    return token


def call():
    # ruleid: robusta-py-tls-verify-false
    requests.get("https://internal", verify=False)
    # ok: robusta-py-tls-verify-false
    requests.get("https://internal")
