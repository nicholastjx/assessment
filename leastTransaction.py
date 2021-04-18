def enterUsers():
	person= {}
	while True:
		name = input('Enter your name, or <ENTER> to finish adding people: ')
		name = name.strip()
		if(len(person)<2) and (len(name) == 0):
			print('No valid number of users! So NO calculation is done!')
			break
		else:
			if len(name) == 0:
				break
			while True:
				try:
					amount = float(input('Enter amount you paid: '))
					person[name] = amount
					break
				except:
					print('Enter numbers only.')
	return person

def checkAmount(person):
	oweMoney = {}
	collectMoney = {}
	total = 0.0
	for i in person:
			total += person[i]
	perPerson = total/len(person)
	for i in person:
		if(person[i] > perPerson):
			collectMoney[i] = person[i] - perPerson
		elif(person[i] < perPerson):
			oweMoney[i] = perPerson - person[i]
	return [oweMoney,collectMoney]

def payment(data):
	count = 0
	for i in data[1]:
		for ii in data[0]:
			if(data[1][i] == data[0][ii]):
				print(f'{ii} pays {i} ${data[0][ii]:.2f}')
				count+=1
				data[1].pop(i)
				data[0].pop(ii)
				return count
	
	for k in data[1]:
		for kk in data[0]:
			if(data[1][k] > data[0][kk]):
				data[1][k] -= data[0][kk]
				print(f'{kk} pays {k} ${data[0][kk]:.2f}')
				
				count+=1
				data[0].pop(kk)
				return count
			elif(data[1][k] < data[0][kk]):
				data[0][kk] -= data[1][k]
				print(f'{kk} pays {k} ${data[1][k]:.2f}')
				count+=1
				data[1].pop(k)
				return count
	return count

def start():	
	person = enterUsers()
	if (len(person)>1):
		data = checkAmount(person)
		transaction = 0
		while True:
			transaction += payment(data)
			if(len(data[0]) == 0):
				break
		print(f'Number of transactions: {transaction}')
	print('End of Program')

def testResult(person):	
	if (len(person)>1):
		data = checkAmount(person)
		transaction = 0
		while True:
			transaction += payment(data)
			if(len(data[0]) == 0):
				break
		print(f'Number of transactions: {transaction}')
	print('End of Program')
	print()
	return transaction
