def make_order(*sandwiches):
	"""summarize the sandwiches we're about to make."""
	print("\nMaking the order for following sandwiches:")
	for sandwiche in sandwiches:
		print(f"-{sandwiche}")

make_order('green sandwitch')
make_order('chicken sandwitch', 'cheese sandwiche', 'grill sandwitch')

def build_profile(first, last, **user_info):
	"""Build a dictionary containing everything we know about a user."""
	user_info['first_name'] = first
	user_info['last_name'] = last
	return user_info

user_profile = build_profile('Ajeet', 'Mishra',
	                         place='Hyderabad',
	                         age='24',
	                         marital_status='unmarried')
print(user_profile)


def car_details(manufacturer, model, **car_info):
	"""Writing a function that stores information about a car in a dictionary."""
	car_info['manufacturer_name'] = manufacturer
	car_info['model_name'] = model
	return car_info

car = car_details('Toyota', 'Fortuner',
	              color='black',
	              seating_capicity=7)
print(car)
	                      
                            


