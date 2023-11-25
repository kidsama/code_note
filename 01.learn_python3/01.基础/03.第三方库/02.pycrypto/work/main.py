from Crypto.Cipher import PKCS1_v1_5  # 加密
from Crypto import Random, Hash
from Crypto.PublicKey import RSA


def encrypt_with_rsa(text, pub_key):
    """[使用公钥进行加密]
    """
    cipher_pub_obj = PKCS1_v1_5.new(RSA.importKey(pub_key))
    secret_byte_obj = cipher_pub_obj.encrypt(text.encode())
    return secret_byte_obj


def decrypt_with_rsa(secret_byte_obj, pri_key):
    """[使用私钥解密]
    """
    cipher_pri_obj = PKCS1_v1_5.new(RSA.importKey(pri_key))
    byte_obj = cipher_pri_obj.decrypt(secret_byte_obj, Random.new().read)
    text = byte_obj.decode()
    return text


def getkey_from_file():
    try:
        with open("/home/apt-data/config/key/kuas-publicKey") as f:
            key = f.read()
            f.close()
            return key
    except FileNotFoundError as e:
        raise e


if __name__ == '__main__':
    text = "asdasd"
    pub_key = getkey_from_file()
    encrypt_key = encrypt_with_rsa(text, pub_key)
    print(encrypt_key)
