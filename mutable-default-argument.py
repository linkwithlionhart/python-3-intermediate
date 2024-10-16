# Situation

def createStudent(name, age, grades=[]):
    return {
        'name': name,
        'age': age,
        'grades': grades
    }

chrisley = createStudent('Chrisley', 15)
dallas = createStudent('Dallas', 16)

def addGrade(student, grade):
    student['grades'].append(grade)
    # To help visualize the grades we have added a print statement
    print(student['grades'])

addGrade(chrisley, 90)
addGrade(dallas, 100)

"""
Problem: returns 
[90]
[90, 100]

Instead of:
[90]
[100]
"""

"""
Why?
Default parameter values are evaluated from left to right when the function definition is executed. 
This means that the expression is evaluated once, when the function is defined, 
and that the same “pre-computed” value is used for each call.

This means that when we call a function, the default values we provide for parameters are only created once, 
and used for each subsequent call of the function. 
This means our grades=[] from our earlier function was only created once and anytime we tried to access it, 
the same list was being modified. 
"""
# We can even see that the memory id of the grades property for both students is the same (using the built-in id() function):
print(id(chrisley['grades'])) # 139828567365696
print(id(dallas['grades'])) # 139828567365696

# Solution
def createStudent(name, age, grades=None):
  if grades is None:
    grades = []
  return {
    'name': name,
    'age': age,
    'grades': grades
  }

def addGrade(student, grade):
    student['grades'].append(grade)
    # To help visualize the grades we have added a print statement
    print(student['grades'])

chrisley = createStudent('Chrisley', 15)
dallas = createStudent('Dallas', 16)

addGrade(chrisley, 90) # returns [90]
addGrade(dallas, 100) # returns [100]

"""
To summarize, we learned:

What a Python gotcha is.
What mutable objects are in Python.
A common gotcha that occurs when using mutable default arguments.
A workaround for mutable default arguments by using None paired with a conditional statement.
"""