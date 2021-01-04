#https://www.dotnetperls.com/ascii-table-python


import requests
import re
import hashlib


host = '178.128.46.168'
port = 30926


def solve():
    url = 'http://{}:{}/'.format(host, port)

    session = requests.Session()
    response = session.get(url)
    body = response.content.decode("utf-8")
    cookie = session.cookies.get('PHPSESSID')

    print(response)
    print(body)
    print(cookie)

    ini = "<html>\n<head>\n<title>emdee five for life</title>\n</head>\n<body style=\"background-color:powderblue;\">\n<h1 align='center'>MD5 encrypt this string</h1><h3 align='center'>"
    fin = "</h3><center><form action=\"\" method=\"post\">\n<input type=\"text\" name=\"hash\" placeholder=\"MD5\" align='center'></input>\n</br>\n<input type=\"submit\" value=\"Submit\"></input>\n</form></center>\n</body>\n</html>\n"

    search = re.search("{}(.*){}".format(ini, fin), body)
    toHash = search.group(1)

    print(toHash)

    hash = hashlib.md5(toHash.encode('utf-8')).hexdigest()

    print(cookie)
    print(hash)

    data = {"hash": hash}
    cookies = {"PHPSESSID": cookie}

    response = session.post(url, data, cookies)

    print(response)
    print(response.content.decode("utf-8"))



def main():

    solve()

main()

