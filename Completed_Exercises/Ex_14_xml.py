import urllib.request
import xml.etree.ElementTree as ET
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = 'http://py4e-data.dr-chuck.net/comments_1711781.xml'
uh = urllib.request.urlopen(url, context=ctx)
data = uh.read()
tree = ET.fromstring(data)
# print(data.decode())
counts = tree.findall('.//count')
# print(len(counts))
numbers = list()
for c in counts:
    # print(c.text)
    numbers.append(int(c.text))
# print(numbers)
a = sum(numbers)
print(a)
