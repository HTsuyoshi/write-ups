from pwn import *

KEY1 = bytes.fromhex('a6c8b6733c9b22de7bc0253266a3867df55acde8635e19c73313')

KEY1x2 = bytes.fromhex('37dcb292030faa90d07eec17e3b1c6d8daf94c35d4c9191a5e1e')

KEY2 = xor(KEY1, KEY1x2)

KEY2x3 = bytes.fromhex('c1545756687e7573db23aa1c3452a098b71a7fbf0fddddde5fc1')

KEY3 = xor(KEY2, KEY2x3)

FxKEY1x2x3 = bytes.fromhex('04ee9855208a2cd59091d04767ae47963170d1660df7f56f5faf')

FLAG = xor(KEY1, KEY2, KEY3, FxKEY1x2x3)

print(FLAG)
