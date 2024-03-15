def bytes2matrix(text):
    """ Converts a 16-byte array into a 4x4 matrix.  """
    return [list(text[i:i+4]) for i in range(0, len(text), 4)]

def matrix2bytes(matrix: list[list[int]]):
    """ Converts a 4x4 matrix into a 16-byte array.  """
    return ''.join([matrix[i][j].to_bytes(1, byteorder='little').decode() for i in range(0,4) for j in range(0,4)])

if __name__ == '__main__':

    matrix = [
        [99, 114, 121, 112],
        [116, 111, 123, 105],
        [110, 109, 97, 116],
        [114, 105, 120, 125],
    ]

    print(matrix2bytes(matrix))
