> In the shadowed realm where the Phreaks hold sway,
>
> A mole lurks within, leading them astray.
>
> Sending keys to the Talents, so sly and so slick,
>
> A network packet capture must reveal the trick.
>
> Through data and bytes, the sleuth seeks the sign,
>
> Decrypting messages, crossing the line.
>
> The traitor unveiled, with nowhere to hide,
>
> Betrayal confirmed, they'd no longer abide.

We were given the file `phreaky.pcap` that has a lot of emails with zip attachments and the password:

![wireshark with emails](/img/phreak_wireshark.png)

I just had to extract each one of them.

Then I merged them:

```bash
cat *.zip.* > flag.pdf
```

In the end of the pdf we can find the flag:

![flag](/img/phreak_flag.png)

Flag: HTB{Th3Phr3aksReadyT0Att4ck}

