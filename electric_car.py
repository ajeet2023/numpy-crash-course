class Car():
	"""A simple attempt to represent a car."""

	def __init__(self, make, model, year):
		"""Initialize attributes to describe a car."""
		self.make = make
		self.model = model
		self.year = year
		self.odometer_reading = 0 


	def get_discriptive_name(self):
		"""Return a neatly formatted discriptive name."""
		long_name = f"{self.year} {self.make} {self.model}"
		return long_name.title()

	def read_odometer(self):
		"""Print a statement showing car's mileage."""
		print(f"This car has {self.odometer_reading} miles on it.")

	def update_odometer(self, mileage):
		"""Set the odometer reading to the given value.
		Reject the change if it attempts to roll the odometer back."""

		if mileage >= self.odometer_reading:
			self.odometer_reading = mileage

		else:
			print("You can't roll back an odometer.")

		def increment_odometer(self, miles):
			self.odometer_reading += miles

class Battery():
	"""A simple attempt to model a battery for an electric car."""

	def __init__(self, battery_size=95):
		"""Initialize the battery's attributes."""
		self.battery_size = battery_size

	def describe_battery(self):
		"""Print a statement describing the battery size."""
		print(f"This car has a {self.battery_size}-KWH battery.")

	def get_range(self):
		"""Print a statement about the range this battery provides."""

		if self.battery_size == 95:
			range = 180
		elif self.battery_size == 120:
			range = 330

		print(f"\nThis car can go about {range} miles on full charge.")

	def upgrade_battery(self):
		"""Upgrade the battery if possible."""
		if self.battery_size == 95:
			self.battery_size = 120	
			print("Upgraded the battery to 120.")

		else:
			print("The battery is already upgraded.")


class ElectricCar(Car):
	"""Represent aspects of a car, specefic to electric vehicles."""

	def __init__(self, make, model, year):
		"""
		Initialize attributes of a parent class
		Then initialise attributes specific to an electric car.
		"""

		super().__init__(make, model, year)
		self.battery = Battery()

my_tesla = ElectricCar('tesla', 'model s', '2021')
print(my_tesla.get_discriptive_name())
my_tesla.battery.describe_battery()

print("\nUpgrade the battery and check it again:")
my_tesla.battery.upgrade_battery()
my_tesla.battery.describe_battery()

print("\nTry upgrading the battery second time.")
my_tesla.battery.upgrade_battery()
my_tesla.battery.describe_battery()













