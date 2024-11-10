#
my_habits = ['eating', 'sleeping', 'reading']
for habit in my_habits:
	if habit == 'eating':
		print(habit.upper())
	else:
		print(habit.title())

print(my_habits == 'sleeping')	
if my_habits != 'sleeping':
	print("I love sleeping!")

voter = 17
if voter >=18:
	print("You're old enough to vote.")
else:	
	print("You're not eligible to vote.")

#elif statement for fees
number = 81
if number < 30:
	price = 0
elif number < 60:
	price = 40
elif number < 80:
	price = 70
elif number >= 80:
	price = 25
print(f"Your joining cost is ${price}.") 

#an elien just shot down in game
alien_color = ['green', 'yellow']
if 'green' in alien_color:
	print("This player just earned 5 points.")
if 'yellow' in alien_color:
	print("This player just earned 10 points.")
#if else statement



#elif statement

alien = 'red'
if alien == 'green':
	score = 5
elif alien == 'yellow':
	score = 10
elif alien == 'red':
	score = 15
	print(f"this player has earned {score} points.")

alien2 = 'green'
if alien2 == 'green':
	score = 5
elif alien2 == 'yellow':
	score = 10
elif alien == 'red':
	score = 15
	print(f"this player has earned {score} points.")

alien3 = 'yellow'
if alien3 == 'green':
	score = 5
elif alien3 == 'yellow':
	score = 10
elif alien3 == 'red':
	score = 15
	print(f"this player has earned {score} points.")













