import urllib.request, urllib.parse, urllib.error
import json
import ssl
import os

os.system('cls')

api_key = 42
serviceurl = 'http://py4e-data.dr-chuck.net/json?'

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

while True:
    # address = input("Enter Location:")
    address = "University of Kerala"
    # if len(address) < 1: break

    parms = dict()
    parms['address'] = address
    parms['key'] = api_key
    url = serviceurl + urllib.parse.urlencode(parms)
    print('Retrieving', url)
    uh = urllib.request.urlopen(url, context=ctx)

    # data = uh.read()
    data1 = uh.read()
    print('Retrieved', len(data1), 'characters')
    data = json.loads(data1)
    # print(data.decode())
    intended_data = data["results"][0]["place_id"]
    break

print('place id',intended_data)
    # tree = ET.fromstring(data)

    # results = tree.findall('result')
    # lat = results[0].find('geometry').find('location').find('lat').text
    # lng = results[0].find('geometry').find('location').find('lng').text
    # location = results[0].find('formatted_address').text

    # print('lat', lat, 'lng', lng)
    # print(location)