import urllib.request, urllib.parse, urllib.error
import http.cookiejar
def get(url,prams,headers):
    cookie_filename = 'cookie.txt'
    cookie = http.cookiejar.MozillaCookieJar(cookie_filename)
    cookie.load(cookie_filename, ignore_discard=True, ignore_expires=True)
    print(cookie)
    # for item in cookie:
    #     print('Name = ' + item.name)
    #     print('Value = ' + item.value)
    handler = urllib.request.HTTPCookieProcessor(cookie)
    prams = urllib.parse.urlencode(prams).encode()
    opener = urllib.request.build_opener(handler)
    # geturl = url + "?" + prams
    response = urllib.request.Request(url,data=prams,headers =headers,method='POST')
    get_response = opener.open(response)
    print(get_response.read().decode())
