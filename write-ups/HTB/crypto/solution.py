import string
f = open('./msg.enc','r')
ct = f.read()
ct = bytes.fromhex(ct)

def decryption(msg):
    ct = []
    for char in msg:
        ct.append((char - 18) * pow(123, -1, 256) % 256)
    return bytes(ct)

pt = decryption(ct)
print(pt)
