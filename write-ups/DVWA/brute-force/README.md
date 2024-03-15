# Brute force

#### Low

Requirements: `hydra`, `rockyou.txt`

Using the script [exploit](./exploit-low.sh)

To use `hydra` you need to get the `PHPSESSID` variable to brute force the login forms.

Bruteforcing `admin` as username and the passwords of `rockyou.txt` wordlist as password you will get the following credentials:

```yaml
username: admin
password: password
```

#### Medium

#### High

#### Extra

#### TODO

Shellscript bruteforcer

[brute-forcer.sh](./brute-forcer.sh)
