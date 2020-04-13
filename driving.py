country = input('Where is your country: ')
age = input('Enter your age: ')
age = int(age)
if country == 'Taiwan':
	if age >= 18:
		print('you can go for driving lisence.')
	else:
		print('you cannot go for driving lisence.')