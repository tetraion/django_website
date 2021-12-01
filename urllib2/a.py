import urllib.request

response = urllib.request.urlopen('https://www.google.com/')
print('url:', response.geturl())
print('code:', response.getcode())
print('Content-Type:', response.info()['Content-Type'])
content = response.read()
print(content)
response.close() 