# DATA TYPES

# String  -> Text  -> 'Hello', 'Testing 123'

# integer -> Numbers  -> -5, 4, 3, 2, 0

# Floating -> Decimals -> 2.4, 5.2, 1000.00

###############################################

# COMPARISION OPERATORS

# == Equal      ->    a == b

# != Not equal  ->    a != b

# < Less than   ->    a < b

# > Greater than ->   a > b

# <= Less than or equal to    ->    a <= b

# >= Greater than or equal to.  ->  a >= b

################################################

# INTEGRATED FEATURES

# print()  This function looks for the default output device, 
# your terminal, and displays the value passed to it.
print("Hello")

# input()
#This function looks for the default input device; when you enter text,
#it captures the value. This value can be assigned or used.

print("Where do you live?")
location = input()
print("So you live in " + location)

#len()
#This function returns the length or count of the elements contained in the structure to which it is applied. 
# It can be a string, array, list, tuple, dictionary, or any sequence.
len("Hello") #five words


#str()
#This function can be used to convert the provided value into a String
str(55)
'55'

#int()
#This function can be used to convert the provided value into an int
int('75')
75

#float()
#This function can be used to convert the provided value to a float
some_int = 10
float(some_int)
10.0

# Creating Functions

#Functions in Python require a keyword to define them: def followed by an identifier (a name)
#that forms the function's signature. The function body contains the code that will be executed when the function is called.

def say_hello():
    return "Hello there!"


you = "mateo"
# With parameters
def say_hello(you):
    return "Hello " +  you
print(say_hello(you))
