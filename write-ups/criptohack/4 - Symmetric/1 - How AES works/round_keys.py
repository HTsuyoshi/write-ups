from structure_of_aes import matrix2bytes

state = [
    [206, 243, 61, 34],
    [171, 11, 93, 31],
    [16, 200, 91, 108],
    [150, 3, 194, 51],
]

round_key = [
    [173, 129, 68, 82],
    [223, 100, 38, 109],
    [32, 189, 53, 8],
    [253, 48, 187, 78],
]

if __name__ == '__main__':

    def add_round_key(s, k):
        def xor(s: int, k: int):
            return s^k
        return [[*map(xor,s[i], k[i])] for i in range(0,4)]

    print(matrix2bytes(add_round_key(state, round_key)))

