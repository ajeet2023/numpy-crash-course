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

class IceCreamStand(Restaurant):
	"""Representing an ice cream stand."""

	def __init__(self, name, cuisine):
		"""Initialize an ice cream stand."""
		super().__init__(name, cuisine)
		self.flavors = []

	def display_flavors(self):
		"""Display available flavors."""
		print("\nWe've following falvors avilable:")
		for flavor in self.flavors:
			print("-" + flavor.title())

naturals = IceCreamStand('The Naturals', 'ice cream')
naturals.flavors = ['vanila', 'dark chocholate', 'lovers paradise', 'rasberry']

naturals.describe_restaurant()
naturals.display_flavors()



		





