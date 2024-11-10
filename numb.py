#counting numbers from 1-20



numbers = list(range(1, 100_00_0))
print(min(numbers))
print(max(numbers))
print(sum(numbers))

odd_numbers = list (range(1, 20, 3))
print(odd_numbers)

threes = []
for value in range(3, 30):
	threes.append(value*3)

print(threes)


cubes = []
for value in range(1, 10):
	cube = value ** 3
	cubes.append(cube)

print(cubes)


cubes = [value**3 for value in range(1,10)]
print(cubes)








