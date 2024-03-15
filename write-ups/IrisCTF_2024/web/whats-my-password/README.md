# Whats My Password?

From the files provided the `sql.setup` show us that there is 3 users: `root`, `skat` and `coded`.

The user `skat` has the flag in his passsword.

Its an simple SQL injection. Using the following payload we can retrieve the password of `skat`.

```
{
  "username": "skat",
  "password": "a\" or ( 1=1 and username = \"skat\")--\""
}
```

irisctf{my_p422W0RD_1S_SQl1}
