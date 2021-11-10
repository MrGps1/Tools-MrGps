from MrGps import Valid

file = input('Path : ')
for email in open(file,'r').read().split('\n'):
	valid = Valid.Account(email)
	if 'True' in valid:
		print('Error : ',email)
	elif 'Band' in valid:
		print('Band : ',email)
	else:
		valid2 = Valid.Instagram(email)
		if 'True' in valid2:
			print('True IG : ',email)
		else:
			error = 'error'
		
		valid3 = Valid.Facebook(email)
		if 'True' in valid3:
			print('True FB : ',email)
		else:
			error = 'error'
