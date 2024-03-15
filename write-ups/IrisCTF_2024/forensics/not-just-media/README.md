# Not Just Media

## Challenge

I downloaded a video from the internet, but I think I got the wrong subtitles.

Note: The flag is all lowercase.

## Solution

The challenge give to us the file `chal.mkv`.

First I watched the video using `mpv`, and activated the subtitles with the key `v` then changed the subtitle with the key `C-j`.

Then I got a chinese text:

```
我們歡迎您接受一生中最大的挑戰，即嘗試理解這段文字的含義
```

That translates into:

```
We welcome you to take on the greatest challenge of your life, which is to try to understand the meaning of this text
```

Then I tried to find informations inside the mkv. I found a tool called `mkvextractor`.

I used the tool `mkvinfo` and found a file called `FakeFont_0.ttf` inside the mkv.

So I extracted this font:

```sh
mkvextract attachments chal.mkv 2:fake_font.ttf
```

Then I used the application `Font Viewer` to see the changes they made in the font. I didn't find anything interesting.

So I tried the chinese text using the `fake_font.ttf` then I got the flag:

`irisctf{mkvm3rg3_my_b3l0v3d}`
