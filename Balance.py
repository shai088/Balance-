
balance = int(input('how much money you have : DH '))


income = int(input('\nadd your income: DH '))


food = int(input('add food expense: DH '))
rent = int(input('add rent expense: DH '))
transport = int(input('add transport expense : DH '))
expenses = rent + food + transport

total_balance = (balance+income) - expenses


print('\ntotal balance: ' ,total_balance, "DH")

print('total expenses:', expenses ,"DH")

if total_balance < 0:
	print('you are in debt')