from pwn import *

if __name__ == '__main__':
    KEY_LEN = 50000

    io = remote('mercury.picoctf.net', 36981)
    io.recvuntil('!\n')

    cipher = io.recvline(keepends=False)
    log.info(f'cipher: {cipher}')

    random_text = str(cyclic(length=KEY_LEN - len(cipher)))
    io.sendlineafter('? ', random_text)
    io.recvuntil('!\n')

    io.sendlineafter('? ', 'a'*32)

    io.recvline()
    cipher2 = io.recvline(keepends=False)
    cipher2 = binascii.unhexlify(cipher2)
    print(cipher2)
    
    message = 'a'*32
    key = []

    for e in range(len(cipher2)):
    	key.append(ord(message[e]) ^ cipher2[e])

    log.info(f'key: {key}')
    decoded_flag = []

    cipher = binascii.unhexlify(cipher)

    for i in range(32):
	    decoded_flag.append(chr(key[i] ^ cipher[i]))

    flag = ''.join(decoded_flag)

    print(f'flag: {flag}')


    io.close()
