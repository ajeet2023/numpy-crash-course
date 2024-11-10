
class Restaurant:
	"""A class represeting a restaurant."""


	def __init__(self, name, cuisine):
		"""Initialize the restaurant."""
		self.name = name
		self.cuisine = cuisine

	def describe_restaurant(self):
		"""Display a summary of the restaurant."""
		print(f"\n{self.name} serves scrumptious {self.cuisine}.")

	def open_restaurant(self):
		"""Dsiplay a message that restaurant is open."""
		print(f"\n{self.name} is open. Come on in!")

restaurant = Restaurant('The Lunch Box', 'rajma chawal')
print(f"\nRestaurant name is {restaurant.name}.")
print(f"\nIt's famous for {restaurant.cuisine}")

restaurant.describe_restaurant()
restaurant.open_restaurant()

new_restaurant = Restaurant('Naturals', 'ice creams')
your_restaurant = Restaurant('Pista House', 'tandoor chicken')
yum_restaurant = Restaurant('KFC', 'crispy chicken')

new_restaurant.describe_restaurant()
your_restaurant.describe_restaurant()
yum_restaurant.describe_restaurant()

class Users:
	"""Representing a simple user."""
	def __init__(self, first, last, username, email, location):
		"""Initialize the user."""
		self.first = first
		self.last = last
		self.username = username
		self.email= email
		self.location = location
		self.login_attempts = 0 

	def describe_user(self):
		"""Describe the summary of the user's information."""
		print(f"\nUser's first name is: {self.first}.")
		print(f"\nUser's last name is: {self.last}.")
		print(f"\nUser's username is: {self.username}.")
		print(f"\nUser's email address is :{self.email}.")
		print(f"\nUser's location is: {self.location}")

	def greet_user(self):
		"""Sending a personalized greeting to the user."""
		print(f"\nWelcome, {self.first}!")


ajeet = Users('Ajeet', 'Mishra', 'ajeethku', 'ajeethku@amazon.com', 'Hyderabad')
anilj = Users('Anil', 'John', 'anilj', 'anilj@amazon.com', 'Delhi')
krishkum = Users('Krishna', 'Kumar', 'krishkum', 'krishkum@amazon.com', 'Banglore')

ajeet.describe_user()
anilj.describe_user()
krishkum.describe_user()

ajeet.greet_user()
anilj.greet_user()
krishkum.greet_user()








