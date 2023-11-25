#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# @author: A.L.Kun
# @file : test.py
# @time : 2022/4/25 6:22
import base64
from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_v1_5 as PKCS1_cipher


def get_key(key_file):
    with open(key_file) as f:
        data = f.read()  # 获取，密钥信息
        key = RSA.importKey(data)
    return key


def encrypt_data(msg):
    public_key = get_key('rsa_public_key.pem')  # 读取公钥信息
    cipher = PKCS1_cipher.new(public_key)  # 生成一个加密的类
    encrypt_text = base64.b64encode(cipher.encrypt(msg.encode()))  # 对数据进行加密
    return encrypt_text.decode()  # 对文本进行解码码


def decrypt_data(encrypt_msg):
    private_key = get_key('rsa_private_key.pem')  # 读取私钥信息
    cipher = PKCS1_cipher.new(private_key)  # 生成一个解密的类
    back_text = cipher.decrypt(base64.b64decode(encrypt_msg), 0)  # 进行解密签名
    return back_text.decode()  # 对文本内容进行解码


msg = "A.L.Kun"
encrypt_text = encrypt_data(msg)  # 加密
print(type(encrypt_text), encrypt_text)
decrypt_text = decrypt_data(encrypt_text)  # 解密
print(decrypt_text, encrypt_text)
