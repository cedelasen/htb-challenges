We have to create an script to extract info obtained with a GET, finally hash the string and send it via POST, reusing the cookie.

```
┌──(kali㉿kali)-[~/htb-challenges/web/md5_4_life]
└─$ python3 files/crack.py 
<Response [200]>
<html>
<head>
<title>emdee five for life</title>
</head>
<body style="background-color:powderblue;">
<h1 align='center'>MD5 encrypt this string</h1><h3 align='center'>ZHYdqx1uLNhYpQyyhMic</h3><center><form action="" method="post">
<input type="text" name="hash" placeholder="MD5" align='center'></input>
</br>
<input type="submit" value="Submit"></input>
</form></center>
</body>
</html>

v4c6m4cqbf42scu38bckkp8ea0
ZHYdqx1uLNhYpQyyhMic
v4c6m4cqbf42scu38bckkp8ea0
400b3e03bbb0fe74e9064681412091f8
<Response [200]>
<html>
<head>
<title>emdee five for life</title>
</head>
<body style="background-color:powderblue;">
<h1 align='center'>MD5 encrypt this string</h1><h3 align='center'>ZHYdqx1uLNhYpQyyhMic</h3><p align='center'>HTB{N1c3_ScrIpt1nG_B0i!}</p><center><form action="" method="post">
<input type="text" name="hash" placeholder="MD5" align='center'></input>
</br>
<input type="submit" value="Submit"></input>
</form></center>
</body>
</html>
```
