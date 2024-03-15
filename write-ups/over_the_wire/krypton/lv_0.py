import base64
from pwn import log

if __name__ == '__main__':
    cipher = 'S1JZUFRPTklTR1JFQVQ='
    log.info('Statement info:')
    print(f'\tcipher: {cipher}')

    flag = base64.b64decode(cipher)
    log.info(f'Flag: {flag}')
