#using input statement printing a messaging stating if we can find that car.
car = input("Please enter your car name ")

print(f"Let me see if I can find you a {car}!")

#using input telling table availability per numbers.
dinner_group = input("\nHow many people are in your group? ")
dinner_group = int(dinner_group)

if dinner_group >=8:
	print("you'll need to wait for a table.")
else:
	print("Your table is ready.")

#Using modulo operator finding if number is mutiple of 10 or not.
number = input("Enter a number, and I'll tell you if it's multiple of 10 or not: ")
number = int(number)

if number % 10 == 0:
	print(f"\nThe number {number} is muliple of 10.")
else:
	print(f"\nThe number {number} is not multiple of 10.")

current_number = 1
while current_number <= 5:
	print(current_number)
	current_number += 1

prompt = "\nTell me something I will repeat it back to you."
prompt += "\nEnter 'quit' to end the program. "

active = True
while active:
	message = input(prompt)

	if message == 'quit':
		active = False
	else:
		print(message)

prompt = "\nPlease enter the name of the city you've visited:"
prompt += "\n(Enter quit when you're finished.) "

while True:
	city = input(prompt)
	if city == 'quit':
		break
	else:
		print(f"I'd love to go to {city.title()}!")

current_number = 0
while current_number < 10:
	current_number += 1
	if current_number % 2 != 0:
	    continue
	print(current_number)
