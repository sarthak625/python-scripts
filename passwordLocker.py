#! python3
# passwordLocker.py - A password locker program

import sys
import pyperclip

PASSWORDS = {
	'gmail': 'F7minlBDDuvMJuxESSKHFhTxFtjVB6',
    'blog': 'VmALvQyKAxiVH5G8v01if1MLZF3sdt',
    'luggage': '12345'
}

if len(sys.argv) < 2:
	print ('Usage: python passwordLocker.py [account] - copy account password')
	sys.exit()

account = sys.argv[1]

if account in PASSWORDS:
	pyperclip.copy(PASSWORDS[account])
	print('Password for '+account+' copied to clipboard')
else:
	print('There is no account named '+account)