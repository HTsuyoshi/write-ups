from pwn import *

for x in range(256):
    possibly_flag = xor(bytes.fromhex('73626960647f6b206821204f21254f7d694f7624662065622127234f726927756d'), x)
    if b'crypto' in possibly_flag:
        print (possibly_flag)
