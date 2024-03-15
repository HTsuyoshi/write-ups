from pwn import log

if __name__ == '__main__':
    cipher = 'UFJKXQZQUNB'
    key = 'SOLVECRYPTO'
    log.info('Statement info:')
    print(f'cipher: {cipher}')
    print(f'key: {key}')

    flag = ''
    for c, k in zip(cipher, key):
        flag += chr((ord(c) - ord(k) - 2*ord('A')) % 26 + ord('A'))

    log.info(f'Flag: picoCTF{{{flag}}}')

