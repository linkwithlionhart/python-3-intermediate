#1/8
"""
Positional arguments: arguments that are called by their position in the function definition.
Keyword arguments: arguments that are called by their name.
Default arguments: arguments that are given default values.
"""

# Position arguments
def print_name(first_name, last_name): 
  print(first_name, last_name)

print_name('Jiho', 'Baggins')

# Keyword arguments
def print_name(first_name, last_name): 
  print(first_name, last_name)

print_name(last_name='Baggins', first_name='Jiho')

# Default arguments
def print_name(first_name='Jiho', last_name='Baggins'): 
  print(first_name, last_name)

print_name()

tables = {
  1: ['Jiho', False],
  2: [],
  3: [],
  4: [],
  5: [],
  6: [],
  7: [],
}
print(tables)

# Write your code below: 
def assign_table(table_number, name, vip_status=False):
  tables.update({table_number: [name, vip_status]})
  return tables

print(assign_table(6, 'Yoni', False))
print(assign_table(name='Martha', table_number=3, vip_status=True))
print(assign_table(4, 'Karla'))

#2 Variable number of arguments: *args (positional arugment packing)
"""
Notice how the print() function does not care how many arguments we pass to it. 
It has no expectation that we are going to pass in one argument or even a million! 
So the question is, how does print() accomplish this?

Well, in Python, there is an additional operator called the unpacking operator (*). 
The unpacking operator allows us to give our functions a variable number of arguments by performing what’s known as positional argument packing.
"""

# Write your code below:
def print_order(*order_items):
  print(order_items)

print_order(
  'Orange Juice',
  'Apple Juice',
  'Scrambled Eggs',
  'Pancakes',
)

#3 Working with *args
tables = {
  1: {
    'name': 'Jiho',
    'vip_status': False,
    'order': 'Orange Juice, Apple Juice'
  },
  2: {},
  3: {},
  4: {},
  5: {},
  6: {},
  7: {},
}
print(tables)

def assign_table(table_number, name, vip_status=False): 
  tables[table_number]['name'] = name
  tables[table_number]['vip_status'] = vip_status
  tables[table_number]['order'] = ''

# Write your code below:
def assign_and_print_order(table_number, *order_items):
  tables[table_number]['order'] = order_items
  for item in order_items:
    print(item)

assign_table(2, 'Arwa', True)
assign_and_print_order(2, 'Steak', 'Seabass', 'Wine Bottle')
print(tables)

#4 Variable number of keyword arguments: **kwargs
"""
Python doesn’t stop at allowing us to accept unlimited positional arguments; 
it also gives us the power to define functions with unlimited keyword arguments. 
The syntax is very similar but uses two asterisks ** instead of one. 
We typically call these kwargs as a shorthand for keyword arguments.

**kwargs takes the form of a dictionary with all the keyword argument values passed to arbitrary_keyword_args. 
Since **kwargs is a dictionary, we can use standard dictionary functions like .get() to retrieve values.
Just as we saw with *args, the name of kwargs is completely arbitrary.
"""
tables = {
  1: {
    'name': 'Chioma',
    'vip_status': False,
    'order': {
      'drinks': 'Orange Juice, Apple Juice',
      'food_items': 'Pancakes'
    }
  },
  2: {},
  3: {},
  4: {},
  5: {},
  6: {},
  7: {},
}
print(tables)


# Write your code below: 
def assign_food_items(**order_items):
  print(order_items)
  food = order_items.get('food')
  drinks = order_items.get('drinks')
  print(food)
  print(drinks)

# Example Call
assign_food_items(food='Pancakes, Poached Egg', drinks='Water')

tables = {
  1: {
    'name': 'Chioma',
    'vip_status': False,
    'order': {
      'drinks': 'Orange Juice, Apple Juice',
      'food_items': 'Pancakes'
    }
  },
  2: {},
  3: {},
  4: {},
  5: {},
  6: {},
  7: {},
}

def assign_table(table_number, name, vip_status=False): 
  tables[table_number]['name'] = name
  tables[table_number]['vip_status'] = vip_status
  tables[table_number]['order'] = {}

assign_table(2, 'Douglas', True)
print('--- tables with Douglas --- \n', tables)

def assign_food_items(table_number, **order_items):
  food = order_items.get('food')
  drinks = order_items.get('drinks')
  tables[table_number]['order']['food_items'] = food
  tables[table_number]['order']['drinks'] = drinks

assign_food_items(2, food='Seabass, Gnocchi, Pizza', drinks='Margarita, Water')
print('\n --- tables after update --- \n', tables)

#5 All together now! *args and *kwargs
"""
So far we have seen how both *args and **kwargs can be combined with standard arguments. 
This is useful, but in some cases, we may want to use all three types together! 
Thankfully Python allows us to do so as long as we follow the correct order in our function definition. 
The order is as follows:

1. Standard positional arguments
2. *args
3. Standard keyword arguments
4. **kwargs
"""
# Write your code below: 
def single_prix_fixe_order(appetizer, *entrees, sides, **dessert_scoops):
  print(appetizer)
  print(entrees)
  print(sides)
  print(dessert_scoops)

single_prix_fixe_order('Baby Beets', 'Salmon', 'Scallops', sides='Mashed Potatoes', scoop_1='Vanilla', scoop_2 = 'Cookies and Cream')