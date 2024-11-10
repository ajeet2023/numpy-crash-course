#Using for loop to write about pizzas
pizzas = ['small pizza', 'medium pizza', 'large pizza']
for pizza in pizzas:
	print(f"I like {pizza.title()}.")
print("\nI really love pizaa.")
for value in list(range(1, 21)):
    print(value)
digits = list(range(1, 1000001))
print(min(digits))
print(max(digits))
print(sum(digits))
odd_numbers = list(range(1, 20, 3))
print(odd_numbers)
new_numbers = []
for value in range(3, 30):
	new_numbers.append(value*3)
print(new_numbers)
cubes = []
for value in range(1, 10):
	cubes.append(value**3)
print(cubes)
pizzas = ['small pizza', 'medium pizza', 'large pizza']
print("my favorite pizza is:")
for pizza in pizzas[-1:]:
	print(pizza.title())
my_hobbies = ['reading books', 'watching movies', 'playing badminton', 'watching news']
Jhon_hobbbies =my_hobbies[:]
Jhon_hobbbies.append('boozing and watching porn')
my_hobbies.append('sprituality and workout')
print("My hobbies are:")
print(my_hobbies)
print("\nJhon's hobbies are:")
print(Jhon_hobbbies)

for hobbies in Jhon_hobbbies[-1:]:
	print(hobbies.title())

cars = ['audi', 'bmw', 'subaru', 'toyta']

for car in cars:
	if car == 'bmw':
		print(car.upper())
	else:
		print(car.title())

my_habits = ['reading books', 'yoga', 'gym', 'watching movies']
'yoga' in my_habits




