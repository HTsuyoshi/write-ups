from pwn import log

if __name__ == '__main__':
    numbers = [16, 9, 3, 15, 3, 20, 59, 6, 20, 8, 5, 14, 21, 13, 2, 5, 18, 19, 13, 1, 19, 15, 14, 61]
    log.info('cipher = {}'.format(''.join(f'{x},' for x in numbers)))
    log.info('flag = {}'.format(''.join(chr(64+x) for x in numbers)))
