# skat's SD Card

## Challenge

"Do I love being manager? I love my kids. I love real estate. I love ceramics. I love chocolate. I love computers. I love trains."

## Solution

They lend us the file `mmcblk0p2.img`.

I used the command `file`:

```
mmcblk0p2.img: Linux rev 1.0 ext4 filesystem data, UUID=4aa56689-dcb4-4759-90e6-179beae559ac, volume name "rootfs" (extents) (large files)
```

Found out that is a *ext4* filesystem*.

I mounted the `mmcblk0p2.img` image into a folder.

```sh
mount mmcblk0p2.img <folder>
```

Then started searching for hints, I found his `.bash_history`:

```sh
ip a
ps -aux
ls */
tree
tree -a
ssh-keygen
cat .ssh/id_rsa.pub
cd Downloads/
git clone
git clone git@github.com:IrisSec/skats-interesting-things.git
cd skats-interesting-things/
ls
cat README.md 
cat article6.txt 
cd ../
ls
rm -rf skats-interesting-things/
exit
```

I also find his `id_rsa` key, that was private. So I used `ssh2john` to create the hashfile:

```sh
ssh2john id_rsa > id_rsa.pub
```

```sh
john id_rsa.hash --wordlist=/usr/share/wordlists/rockyou.txt
```

Then I found that the password of `id_rsa` was **id_rsa**.

I cloned his repository:

```sh
git clone git@github.com:IrisSec/skats-interesting-things.git
```

And then list the old commits:

```sh
git log
```

Then I checked out for the right commit:

```sh
git checkout <id>
```

Then I got the flag:

irisctf{0h_cr4p_ive_left_my_k3ys_out_4nd_ab0ut}

I have used TSK that I could recover most of the files in the filesystem. But I couldn't find inside the diffs inside a git file. I wasted so much time...
