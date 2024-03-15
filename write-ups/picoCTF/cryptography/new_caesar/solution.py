from pwn import log
import string

LOWERCASE_OFFSET = ord("a")
ALPHABET = string.ascii_lowercase[:16]
cipher = "dcebcmebecamcmanaedbacdaanafagapdaaoabaaafdbapdpaaapadanandcafaadbdaapdpandcac"

def b16_decode(cipher):
    dec = ""
    for c in range(0, len(cipher), 2):
        char1 = ord(cipher[c]) - LOWERCASE_OFFSET
        char2 = ord(cipher[c+1]) - LOWERCASE_OFFSET

        binary = '{0:04b}'.format(char1) + '{0:04b}'.format(char2)
        dec += chr(int(binary, 2))
    return dec

def shift(c, k):
	t1 = ord(c) + LOWERCASE_OFFSET
	t2 = ord(k) + LOWERCASE_OFFSET
	return ALPHABET[(t1 - t2) % len(ALPHABET)]

if __name__ == '__main__':
    
    log.info('Statement info:')
    print(f'\tOffset: {LOWERCASE_OFFSET}')
    print(f'\tAlphabet: {ALPHABET}')
    print(f'\tCipher: {cipher}')
    
    status = log.progress('Starting brute force Alphabet')
    for key in ALPHABET:
        status.status(key)
        assert all([k in ALPHABET for k in key])
        assert len(key) == 1
        
        dec = ""
        for i, c in enumerate(cipher):
            dec += shift(c, key[i % len(key)])

        dec = b16_decode(dec)
        if dec.isascii():
            status.success()
            print(f'Flag: picoCTF{{{dec}}}')
