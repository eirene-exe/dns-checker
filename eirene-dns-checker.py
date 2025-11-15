import requests
import json
from os import system

clear = lambda: system('cls||clear')

system('title Eirene Dns-Checker')
clear()
domain = input('Enter your domain: ')
clear()

url_NS = f'https://www.whatsmydns.net/api/details?server=pqjokmjw&type=NS&query={domain}'
url_A = f'https://www.whatsmydns.net/api/details?server=pqjokmjw&type=A&query={domain}'

response_ns = requests.get(url_NS)
response_ns2 = json.loads(response_ns.text)

response_A = requests.get(url_A)
response_A2 = json.loads(response_A.text)


print('Nameservers: ')
print(response_ns2['data'][0]['response'][0])
print(response_ns2['data'][0]['response'][1])

print('\nHosting Ip: ')
print(response_A2['data'][0]['response'][0])
print(response_A2['data'][0]['response'][1])
