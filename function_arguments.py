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
"""Notice how the print() function does not care how many arguments we pass to it. It has no expectation that we are going to pass in one argument or even a million! So the question is, how does print() accomplish this?

Well, in Python, there is an additional operator called the unpacking operator (*). The unpacking operator allows us to give our functions a variable number of arguments by performing what’s known as positional argument packing.
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


