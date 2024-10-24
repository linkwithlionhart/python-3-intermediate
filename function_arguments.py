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

#7 Function Call Unpacking & Beyond
my_num_list = [3, 6, 9]

def sum(num1, num2, num3):
  print(num1 + num2 + num3)

sum(*my_num_list)

# OR
numbers  = {'num1': 3, 'num2': 6, 'num3': 9}

def sum(num1, num2, num3):
  print(num1 + num2 + num3)

sum(**numbers)
"""
Using the unpacking operator (*) we are spreading the contents of our list my_num_list into the individual arguments 
in our function definition. We are immediately saved the hassle of writing loops and are given the flexibility to use 
any iterable with three elements.
"""
def calculate_price_per_person(total, tip, split):
  total_tip = total * (tip/100)
  split_price = (total + total_tip) / split
  print(split_price)

# Write your code below: 
table_7_total = [534.50, 20.0, 5]
calculate_price_per_person(*table_7_total)
# unpacks the list neatlyy into the required arugments
calculate_price_per_person(534.50, 20.0, 5)
# traditional way must be entered positionally and directly

#8 Review
"""
We learned:
How to pack positional arguments in a function with *args.
How to work with *args using iteration and other positional arguments.
How to pack keyword arguments in a function with **kwargs.
How to work with **kwargs using iteration and other keyword arguments.
How to combine all different types of arguments to gain the most flexibility in our function declarations.
How to use an unpacking operator (* or **) to unpack arguments in a function call.
How to use an unpacking operator (* or **) on iterables.
"""
tables = {
  1: {
    'name': 'Jiho',
    'vip_status': False,
    'order': {
      'drinks': 'Orange Juice, Apple Juice',
      'food_items': 'Pancakes',
      'total': [534.50, 20.0, 5]
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

def assign_food_items(table_number, **order_items):
  food = order_items.get('food')
  drinks = order_items.get('drinks')
  tables[table_number]['order']['food_items'] = food
  tables[table_number]['order']['drinks'] = drinks

def calculate_price_per_person(total, tip, split):
    total_tip = total * (tip/100)
    split_price = (total + total_tip) / split
    print(split_price)

# The ability to remove a table’s guests when they leave the restaurant.
leave_info = [1, True]
def remove_guest(table_number, leave=True):
  if leave == True:
    tables[table_number] = {}
    print(f'Table {table_number} is cleared.')
  else:
    print(f'Error. Guest has not left.')
remove_guest(*leave_info)
print(tables)

# An adjustment to the calculate_price_per_person() function to access a tables 'total' and return the result.
