country = input('Where is your country: ')
age = input('Enter your age: ')
age = int(age)
if country == 'Taiwan':
	if age >= 18:
		print('you can go for driving lisence.')
	else:
		print('you cannot go for driving lisence.')
elif country == 'the USA':
	if age >= 16:
		print('you can go for driving lisence.')
	else:
		print('you cannot go for driving lisence.')
else:
	print('you can only insert Taiwan / the USA')