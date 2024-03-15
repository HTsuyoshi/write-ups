from pwn import log
import codecs

if __name__ == '__main__':
    cipher = 'YRIRY GJB CNFFJBEQ EBGGRA'
    log.info('Statement info:')
    print(f'\tcipher: {cipher}')

    flag = codecs.encode(cipher, 'rot_13')
    log.info(f'Flag: {flag}')
