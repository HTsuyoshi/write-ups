from pwn import *

cypher = "label"

print(b"crypto{" + xor(cypher, 13) + b"}")

