from pwn import log

def ROT(cipher, n):
    flag = ''
    for x in cipher:
        offset = ord('a')
        if x.isalpha():
            if x.isupper():
                offset = ord('A')
            flag += chr((ord(x) - offset + n) % 26 + offset) 
        else:
            flag += x
    return flag

if __name__ == '__main__':
    with open('ciphertext', 'r') as f:
        ciphertext = f.read()

    log.info('Statement info:')
    print(f'\tciphertext: {ciphertext}')

    ciphertext = ciphertext[8:-1]
    for n in range(26):
        flag = ROT(ciphertext, n)
        if 'cross' in flag:
            log.info(f'Flag: picoCTF{{{flag}}}')
