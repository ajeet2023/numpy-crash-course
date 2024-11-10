import json

favorite_number = input("What is your favorite number? ")

filename = 'favorite_number.json'
with open(filename, 'w') as f:
	json.dump(favorite_number, f)
	print("Thanks! I'll remember it.")

filename = 'favorite_number.json'

with open(filename) as f:
	favorite_number = json.load(f)
	print(f"I know your favorite number is {favorite_number}!")

import json

try:
	with open('favorite_number.json') as f:
		number = json.load(f)
except FileNotFoundError:
	number = input("What is your favorite number? ")
	with open('favorite_number', 'w') as f:
		json.dump(number, f)
		print("Thanks! I'll remember it.")
else:
	print(f"I know your favorite number is {number}!")

import json

def get_stored_username():
	"""Get stored username if available."""
	filename = 'username.json'
	try:
		with open(filename) as f_object:
			username = json.load(f_object)
	except FileNotFoundError:
		return None 
	else:
		return username

def get_new_username():
	"""Prompt for a new username."""
	username = input("What is your name? ")
	filename = 'username.json'
	with open(filename, 'w') as f_object:
		json.dump(username, f_object)
	return username

def greet_user():
	"""greet the user by name."""
	username = get_stored_username()
	if username:
		correct = input(f"Are you {username}? (y/n)")
		if correct == 'y':
			print(f"Welcome back {username}!")
		else:
			username = get_new_username()
			print(f"We'll remember you when you come back {username}!")
	else:
		username = get_new_username()
		print(f"We'll remember you when you come back {username}!")

	greet_user()







