import urllib.request
import ssl
import json

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

#url = input('Enter Url:')

url = 'http://py4e-data.dr-chuck.net/comments_1711782.json'
uh = urllib.request.urlopen(url, context=ctx)

info = json.loads(uh.read())
intended_data = info['comments']

# for index, fruit in enumerate(my_list)
sum = 0
for counter,i in enumerate(intended_data):
    sum += i['count']
print('No of Entries:',counter, '\nSum:', sum)

