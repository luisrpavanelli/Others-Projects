import requests
res = requests.get('https://www.w3.org/TR/PNG/iso_8859-1.txt')
res.raise_for_status()
playFile = open('test.txt', 'wb')
for chunk in res.iter_content(100000):
 playFile.write(chunk)
100000
78981
playFile.close()