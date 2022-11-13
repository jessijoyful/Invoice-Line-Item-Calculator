def input_price():
	
	try:
		price = float(input('Enter price: '))
		return price

	except ValueError:
		print("Invalid decimal number. Please try again.")
		return input_price()

def input_quantity():
	
	try:
		quantity = int(input('Enter quantity: '))
		return quantity

	except ValueError:
		print('Invalid integer. Please try again.')
		return input_quantity()


choice = ""

print('The Invoice Line Item Calculator')

while choice!='n':
	print()

	price = input_price()
	quantity = input_quantity()

	total = price*quantity

	print()

	print(f'PRICE:{price:>11.2f}')
	print(f'QUANTITY:{quantity:>4}')
	print(f'TOTAL:{total:>12.2f}')

	choice = input("Enter another line item? (y/n): ")

print()
print('Bye!')