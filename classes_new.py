
class Website:
	"""A simplet attempt to represent a website."""

	def __init__(self, platform, does, name, launched):
		"""Innitialize attributes to describe a website."""
		self.name = name
		self.launched = launched
		self.platform = platform
		self.does = does

	def get_website_discription(self):
		""" Return neatly formatted details."""
		Website_details = f"{self.name}, {self.launched}, {self.platform}, {self.does}"
		return Website_details.title()

my_website = Website('python', 'digital marketing', 'digital vendre', '2020')
print(my_website.get_website_discription())

class Restaurant:
	"""A class represeting a restaurant."""


	def __init__(self, name, cuisine):
		"""Initialize the restaurant."""
		self.name = name
		self.cuisine = cuisine
		self.number_served = 0 

	def describe_restaurant(self):
		"""Display a summary of the restaurant."""
		print(f"\n{self.name} serves scrumptious {self.cuisine}.")

	def open_restaurant(self):
		"""Dsiplay a message that restaurant is open."""
		print(f"\n{self.name} is open. Come on in!")

	def customers_served(self):
		"""Print a statement showing customers served."""
		print(f"\nThis restaurant has served {self.number_served} customers.")

	def set_number_served(self, customers):
		"""Set the number of customers served to given value."""
		self.number_served = customers

	def increment_number_served(self, guests):
		""""Add the given number to the customers served."""
		self.number_served += guests


restaurant = Restaurant('The Lunch Box', 'rajma chawal')
print(f"\nRestaurant name is {restaurant.name}.")
print(f"\nIt's famous for {restaurant.cuisine}.")

restaurant.describe_restaurant()
restaurant.open_restaurant()
restaurant.set_number_served(56_200)
restaurant.customers_served()
restaurant.increment_number_served(100)
restaurant.customers_served()


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

	def read_attempts(self):
		"""Print a statement showing value of login attempts."""
		print(f"\n{self.username} has {self.login_attempts} login attempts.")

	def read_reset(self):
		"""Printing a statement showing vlaue of reset."""
		print(f"\n{self.username}'s login attempt has been reset to {self.login_attempts}.")

	def increment_login_attempts(self, attempts):
		"""Adding the value increment by 1."""
		self.login_attempts += attempts


		

	def reset_login_attempts(self):
		self.login_attempts = 0



ajeet = Users('Ajeet', 'Mishra', 'ajeethku', 'ajeethku@amazon.com', 'Hyderabad')
anil = Users('Anil', 'John', 'anilj', 'anilj@amazon.com', 'Delhi')
krishna = Users('Krishna', 'Kumar', 'krishkum', 'krishkum@amazon.com', 'Banglore')

ajeet.describe_user()
anil.describe_user()
krishna.describe_user()

ajeet.greet_user()
anil.greet_user()
krishna.greet_user()

ajeet.increment_login_attempts(2)
ajeet.read_attempts()
ajeet.reset_login_attempts()
ajeet.read_reset()
anil.increment_login_attempts(3)
anil.read_attempts()
anil.reset_login_attempts()
anil.read_reset()























	
