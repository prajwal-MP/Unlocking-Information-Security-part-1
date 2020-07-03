from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes

def aes_encrypt(plaintext, k):
    iv = get_random_bytes(16)
    cipher = AES.new(k, AES.MODE_CBC,iv)
    ct_bytes = cipher.encrypt(plaintext)
    return iv+ct_bytes

def aes_decrypt(ciphertext, k):
    iv = ciphertext[:16]
    ciphertext = ciphertext[16:]
    cipher = AES.new(k, AES.MODE_CBC, iv)
    pt = cipher.decrypt(ciphertext)
    return pt.decode('latin1')
