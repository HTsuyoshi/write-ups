from pwn import log
from Crypto.Util.number import long_to_bytes
import gmpy2

if __name__ == '__main__':
    with open('ciphertext', 'r') as f:
        N = int(f.readline().split(': ')[1])
        e = int(f.readline().split(': ')[1])
        f.readline()
        c = int(f.readline().split(': ')[1])
    log.info('Statement info:')
    print(f'\tN: {N}')
    print(f'\te: {e}')
    print(f'\tc: {c}')

    progress = log.progress('Finding i that i*N + c has a cube root of 1/e: ')
    i = 0
    while True:
        progress.status(str(i))
        flag, is_root = gmpy2.iroot(i*N + c, e)
        if is_root:
            progress.success()
            flag = long_to_bytes(flag).decode().strip()
            log.info(f'Flag: {flag}')
            break
        i += 1
