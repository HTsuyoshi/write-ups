from pwn import remote, log

SQUARE_SIZE = 6

def generate_square(alphabet):
	assert len(alphabet) == pow(SQUARE_SIZE, 2)
	matrix = []
	for i, letter in enumerate(alphabet):
		if i % SQUARE_SIZE == 0:
			row = []
		row.append(letter)
		if i % SQUARE_SIZE == (SQUARE_SIZE - 1):
			matrix.append(row)
	return matrix

def get_index(letter, matrix):
	for row in range(SQUARE_SIZE):
		for col in range(SQUARE_SIZE):
			if matrix[row][col] == letter:
				return (row, col)
	print("letter not found in matrix.")
	exit()

def encrypt_pair(pair, matrix):
	p1 = get_index(pair[0], matrix)
	p2 = get_index(pair[1], matrix)

	if p1[0] == p2[0]:
		return matrix[p1[0]][(p1[1] + 1)  % SQUARE_SIZE] + matrix[p2[0]][(p2[1] + 1)  % SQUARE_SIZE]
	elif p1[1] == p2[1]:
		return matrix[(p1[0] + 1)  % SQUARE_SIZE][p1[1]] + matrix[(p2[0] + 1)  % SQUARE_SIZE][p2[1]]
	else:
		return matrix[p1[0]][p2[1]] + matrix[p2[0]][p1[1]]


def encrypt_string(s, matrix):
    result = ""
    plain = s
    if len(s) % 2 != 0:
        plain += "l"
    for i in range(0, len(plain), 2):
        result += encrypt_pair(plain[i:i + 2], matrix)
    return result

def decipher(cipher):
    pass

if __name__ == '__main__':
    server = remote('mercury.picoctf.net', 19860)

    log.info('Statement info:')
    server.recvuntil(': ')
    alphabet = str(server.recvline(keepends=False))
    server.recvuntil(': ')
    cipher = str(server.recvline(keepends=False))
    print(f'\talphabet: {alphabet}')
    print(f'\tcipher: {cipher}')

    plaintext = decipher(cipher)
    log.info('Sending:')
    print(f'\tplaintext: {plaintext}')

    server.sendafter('? ', data=plaintext)
    flag = server.recv()

    log.info(flag)

