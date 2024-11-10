print ("Give me two numbers, and I will add them for you.")
print("Enter q to quit.")

while True:
	first_number = input("\nFirst number: ")
	if first_number == 'q':
		break
	second_number = input("\nSecond number: ")
	if second_number == 'q':
		break
	try:
		answer = int(first_number) + int(second_number)
	except ValueError:
		print("Sorry, you can't add text with a numeric number.")
	else:
		print(answer)

filenames = ['dogs.txt', 'cats.txt']

for filename in filenames:
	try:
		with open(filename) as f:
			contents = f.read()
			print(contents)
	except FileNotFoundError:
		pass





		
		
			







