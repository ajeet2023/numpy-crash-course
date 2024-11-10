def display_message():
	"""telling everyone what I'm learning in this chapter"""
	print("I'm learning functions in this chapter.")
display_message()

def favorite_book(bookname):
	"""display the favorite book"""
	print(f"One of my favorite book is {bookname.title()}.")
favorite_book('Alice in wonderland')

def make_shirt(shirt_size, print_message):
	"""Display infromation about shirt"""
	print(f"I've ordered a {shirt_size} shirt, and {print_message} should be printed on that.")

make_shirt(shirt_size='large', print_message='I love my India')
make_shirt('large', 'I love my India')

def make_shirt(shirt_size='large shirt', print_message='I love python'):
	"""display information about shirt"""
	print(f"I've ordered a {shirt_size} shirt, and {print_message} should be printed on that. ")
make_shirt()
make_shirt(shirt_size='medium')
make_shirt(shirt_size='small', print_message='coding is a cake walk for me')

def describe_city(city_name, country_belong='Iceland'):
	"""Display infromation about a city."""
	print(f"\n{city_name.title()} is in {country_belong}.")

describe_city('Reykjavik')
describe_city('Akureyri')
describe_city('Hyderabad')

def get_formatted_name(first_name, last_name):
	"""Return a full name, neatly formatted."""
	full_name = f"{first_name} {last_name}"
	return full_name.title()
#This is an infinite loop!
while True:
	print("\nPlease tell me your name:")
	f_name = input("First name: ")
	if f_name == 'q':
		break
	l_name = input("Last name: ")
	if l_name == 'q':
		break


	formatted_name = get_formatted_name(f_name, l_name)
	print(f"\nHello, {formatted_name}!")



