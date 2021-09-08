from pwn import log

if __name__ == '__main__':
    cipher = 'AYCQYPGQCYQW'
    log.info('Statement info:')
    print(f'\tcipher: {cipher}')

    for x in range(26):
        flag = ""
        for char in cipher:
            flag += chr((ord(char) - ord('A') + x) % 26 + ord('A'))
        if 'CAESAR' in flag:
            log.info(f'Flag: {flag}')
            break
