from Crypto.Cipher import AES
from Crypto import Random
import itertools
import sys # ignore
sys.path.insert(0,'.') # ignore
from Root.prev_func import aes_decrypt, is_english

def brute_force_aes(ciphertext):
    # return plaintext (in 'latin1', from aes_decrypt()), k
    key_start = '036'
    key_end = '0000000'
    for i in range(1000000):
        key = bytes(key_start+'0'*(6-len(str(i)))+str(i)+key_end, encoding='utf-8')
        if is_english(aes_decrypt(ciphertext,key)):
            return aes_decrypt(ciphertext,key),key
    
"""
Brute force a message encrypted with AES-CBC, given that it was encrypted with a key that represents a phone number of someone from Tel-Aviv, padded with zeroes (in other words, 9 digits, beginning with 036, and with trailing '0' to a length of 16 bytes, like this: 036######0000000).

You should test your brute-force cracker code using the outputs from your encrypt function of Hackxercise 6.
"""
