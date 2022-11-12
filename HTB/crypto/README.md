# Baby Encryption

The challenge provide us the file `BabyEncryption.zip`.

This file contains the following files:

- `chall.py`: It seems to be the code used to encrypt the secret message
- `msg.enc`: It seems to be the result of the encryption.

The algorithm `encryption` inside `chall.py` uses the _affine cipher_.

So, every byte inside the message is multiplied by `123` and summed to `18` over module `256`.

$$ciphertext_{i} = (message_{i} \times 123) + 18 \mod{256}$$

We can use the Euclidean algorithm to find the modular inverse of `123`: `179`

To recover the message:

$$(ciphertext_{i} - 18) * 179 mod{256}$$
