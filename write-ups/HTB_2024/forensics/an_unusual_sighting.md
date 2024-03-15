> As the preparations come to an end, and The Fray draws near each day, our newly
established team has started work on refactoring the new CMS application for
the competition. However, after some time we noticed that a lot of our work
mysteriously has been disappearing! We managed to extract the SSH Logs and the
Bash History from our dev server in question. The faction that manages to
uncover the perpetrator will have a massive bonus come competition!

Connecting with `nc` in the server we receive this message:

> +---------------------+---------------------------------------------------------------------------------------------------------------------+
>
> |        Title        |                                                     Description                                                     |
>
> +---------------------+---------------------------------------------------------------------------------------------------------------------+
>
> | An unusual sighting |                        As the preparations come to an end, and The Fray draws near each day,                        |
>
> |                     |             our newly established team has started work on refactoring the new CMS application for the competition. |
>
> |                     |                  However, after some time we noticed that a lot of our work mysteriously has been disappearing!     |
>
> |                     |                     We managed to extract the SSH Logs and the Bash History from our dev server in question.        |
>
> |                     |               The faction that manages to uncover the perpetrator will have a massive bonus come the competition!   |
>
> |                     |                                                                                                                     |
>
> |                     |                                            Note: Operating Hours of Korp: 0900 - 1900                               |
>
> +---------------------+---------------------------------------------------------------------------------------------------------------------+
>
>
> Note 2: All timestamps are in the format they appear in the logs
>
> What is the IP Address and Port of the SSH Server (IP:PORT)

So we just have to analyze the `sshd.log` file and the `bash_history.txt` file to answer the questions.:

Answer #1 the first lines of the `sshd.log`:

> What is the IP Address and Port of the SSH Server (IP:PORT)
>
> \> 100.107.36.130:2221
>
> [+] Correct!

Answer #2 is just below of the first question:

> What time is the first successful Login
>
> \> 2024-02-13 11:29:50
>
> [+] Correct!

As we saw in the banner the company works from 09:00 until 19:00 so we search for unusual hours:

```bash
grep -E -v '\[?????????? (0[9]|1[0-9]).*' sshd.log
```

Answer #3 find the perpetrator:

> What is the time of the unusual Login
>
> \> 2024-02-19 04:00:14
>
> [+] Correct!

Answer #4 can be answered with the same command of the question five:

> What is the Fingerprint of the attacker's public key
>
> \> OPkBSs6okUKraq8pYo4XwwBg55QSo210F09FCe1-yj4
>
> [+] Correct!

With answer #6 and #7 we can use the same grep function on the file `bash_history.txt`:

```bash
grep -E -v '\[?????????? (0[9]|1[0-9]).*' bash_history.txt
```

Answer #6:

> What is the first command the attacker executed after logging in
>
> \> whoami
>
> [+] Correct!

Answer #7:

> What is the final command the attacker executed before logging out
>
> \> ./setup
>
> [+] Correct!

Flag: HTB{B3sT_0f_luck_1n_th3_Fr4y!!}
