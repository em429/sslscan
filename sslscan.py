# sslscan.py | scans a list of domains using qualys SSLlabs scanner API

# TODO take any file using arguments

from ssllabsscanner import *
from termcolor import colored
import sys

with open('domains') as f:
    domains = f.readlines()

# Strip whitespace
domains = [x.strip() for x in domains]
# Remove empty list elements
domains = list(filter(None, domains))

for domain in domains:

    details = 'https://www.ssllabs.com/ssltest/analyze.html?d=' + domain

    print('Scanning ' + domain + '...')
    scan = newScan(domain)

    if scan['endpoints'][0]['grade'] != 'A+':
        print(colored(domain + ' recieved a grade below A+, please check for details here: ' + details, 'red'))
    elif scan['endpoints'][0]['grade'] == 'A+':
        print(colored('Scan returned desired A+ grade for ' + domain + '\n', 'green'))
    else:
        print(colored('Unknown grade recieved.. Please check details here: ' + details + '\n', 'red'))

print('Domain scan completed.')