import pizza

pizza.make_pizza(16, 'pepperoni')
pizza.make_pizza(12,'mushrooms', 'green peppers', 'extra cheese')

from arbitrary import make_order

make_order('green sandwitch')
make_order('chicken sandwitch', 'cheese sandwiche', 'grill sandwitch')

from arbitrary import make_order as mo

mo('green sandwitch')
mo('chicken sandwitch', 'cheese sandwiche', 'grill sandwitch')