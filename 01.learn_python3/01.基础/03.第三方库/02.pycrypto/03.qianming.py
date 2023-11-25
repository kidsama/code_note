#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# @author: A.L.Kun
# @file : test.py
# @time : 2022/4/25 6:22
import base64
from Crypto.PublicKey import RSA
from Crypto.Hash import SHA
from Crypto.Signature import PKCS1_v1_5 as PKCS1_signature


def get_key(key_file):
    with open(key_file) as f:
        data = f.read()
        key = RSA.importKey(data)
    return key


def rsa_private_sign(data):
    private_key = get_key('rsa_private_key.pem')  # 导入私钥
    signer = PKCS1_signature.new(private_key)  # 设置签名的类
    digest = SHA.new()  # 创建sha加密的类
    digest.update(data.encode())  # 将要加密的数据进行sha加密
    sign = signer.sign(digest)  # 对数据进行签名
    # 对签名进行处理
    signature = base64.b64encode(sign)  # 对数据进行base64加密
    signature = signature.decode()  # 再进行编码
    return signature  # 返回签名


def rsa_public_check_sign(text, sign):
    publick_key = get_key('rsa_public_key.pem')  # 导入公钥
    verifier = PKCS1_signature.new(publick_key)  # 生成验证信息的类
    digest = SHA.new()  # 创建一个sha加密的类
    digest.update(text.encode())  # 将获取到的数据进行sha加密
    return verifier.verify(digest, base64.b64decode(sign))  # 对数据进行验证，返回bool值


msg = 'A.L.Kun'
sign = rsa_private_sign(msg)
print(rsa_public_check_sign(msg, sign))
