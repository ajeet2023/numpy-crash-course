from car import Car 

my_new_car = Car('audi', 'a4', '2022')
print(my_new_car.get_discriptive_name())

my_new_car.odometer_reading = 48
my_new_car.read_odometer()