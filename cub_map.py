#Plotting 5 cubes:

import matplotlib.pyplot as plt

x_values = [1, 2, 3, 4, 5]
cubes = [1, 8, 27, 64, 125]

# Make plot 

plt.scatter(x_values, cubes, edgecolor='none', s=40)

#customize plot.

plt.title("Cubes", fontsize=24)
plt.xlabel('Value', fontsize=14)
plt.ylabel('Cubes of Value', fontsize=14)
plt.tick_params(axis='both', labelsize=14)

#show plot.

plt.show()


#plotting 500 cubes.

x_values = range(1,5001)
y_values = [x**3 for x in x x_values]

#make plot.

plt.scatter(x_values, cubes, 'edgecolor=none', s=40)
plt.title("Cubes", fontsize=24)
plt.xlabel('Value', fontsize=14)
plt.ylabel('Cubes of Value', fontsize=14)
plt.tick_params(axis='both', labelsize=14)
plt.axis([0, 5100, 0, 5100**3])






