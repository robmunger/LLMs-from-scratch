# I've deleted everything that's boring from https://learnxinyminutes.com/python/ and https://learnxinyminutes.com/pythonstatcomp/

""" Multiline strings can be written
    using three "s, and are often used
    as documentation.
"""
# Exponentiation (x**y, x to the yth power)
2**3  # => 8

# (is vs. ==) is checks if two variables refer to the same object, but == checks
# if the objects pointed to have the same values.
a = [1, 2, 3, 4]  # Point a at a new list, [1, 2, 3, 4]
b = [1, 2, 3, 4]  # Point b at a new list, [1, 2, 3, 4]
b is a            # => False, a and b do not refer to the same object
b == a            # => True, a's and b's objects are equal

# Strings are created with " or '
"This is a string."
'This is also a string.'

# Strings can be added too
"Hello " + "world!"  # => "Hello world!"
# String literals (but not variables) can be concatenated without using '+'
"Hello " "world!"    # => "Hello world!"

# None is an object
None  # => None

# Don't use the equality "==" symbol to compare objects to None
# Use "is" instead. This checks for equality of object identity.
"etc" is None  # => False
None is None   # => True

####################################################
## 2. Variables and Collections
####################################################

# By default the print function also prints out a newline at the end.
# Use the optional argument end to change the end string.
print("Hello, World", end="!")  # => Hello, World!

# There are no declarations, only assignments.
# Convention in naming variables is snake_case style
some_var = 5
some_var  # => 5

# if can be used as an expression
# Equivalent of C's '?:' ternary operator
"yay!" if 0 > 1 else "nay!"  # => "nay!"

# Lists are arrays.
li = []
li.append(1)    # li is now [1]
li.pop()        # => 3 and li is now [1, 2, 4]
li[0]   # => 1
# Look at the last element
li[-1]  # => 1

# You can look at ranges with slice syntax.
# The start index is included, the end index is not
# (It's a closed/open range for you mathy types.)
li = [1, 2, 4, 3]
li[1:3]   # Return list from index 1 to 3 => [2, 4]
li[2:]    # Return list starting from index 2 => [4, 3]
li[:3]    # Return list from beginning until index 3  => [1, 2, 4]
li[::2]   # Return list selecting elements with a step size of 2 => [1, 4]
li[::-1]  # Return list in reverse order => [3, 4, 2, 1]
# Use any combination of these to make advanced slices
# li[start:end:step]

# Make a one layer deep copy using slices
li2 = li[:]  # => li2 = [1, 2, 4, 3] but (li2 is li) will result in false.

# Remove arbitrary elements from a list with "del"
del li[2]  # li is now [1, 2, 3]

# Remove first occurrence of a value
li.remove(2)  # li is now [1, 3]
li.remove(2)  # Raises a ValueError as 2 is not in the list

# Insert an element at a specific index
li.insert(1, 2)  # li is now [1, 2, 3] again

# Get the index of the first item found matching the argument
li.index(2)  # => 1
li.index(4)  # Raises a ValueError as 4 is not in the list

# You can add lists
# Note: values for li and for other_li are not modified.
li + other_li  # => [1, 2, 3, 4, 5, 6]

# Concatenate lists with "extend()"
li.extend(other_li)  # Now li is [1, 2, 3, 4, 5, 6]

# Check for existence in a list with "in"
1 in li  # => True

# Tuples are like lists but are immutable.
tup = (1, 2, 3)
tup[0]      # => 1
tup[0] = 3  # Raises a TypeError

# Note that a tuple of length one has to have a comma after the last element but
# tuples of other lengths, even zero, do not.
type((1))   # => <class 'int'>
type((1,))  # => <class 'tuple'>
type(())    # => <class 'tuple'>

# You can do most of the list operations on tuples too
len(tup)         # => 3
tup + (4, 5, 6)  # => (1, 2, 3, 4, 5, 6)
tup[:2]          # => (1, 2)
2 in tup         # => True

# You can unpack tuples (or lists) into variables
a, b, c = (1, 2, 3)  # a is now 1, b is now 2 and c is now 3
# You can also do extended unpacking
a, *b, c = (1, 2, 3, 4)  # a is now 1, b is now [2, 3] and c is now 4
# Tuples are created by default if you leave out the parentheses
d, e, f = 4, 5, 6  # tuple 4, 5, 6 is unpacked into variables d, e and f
# respectively such that d = 4, e = 5 and f = 6
# Now look how easy it is to swap two values
e, d = d, e  # d is now 5 and e is now 4


# Dictionaries store mappings from keys to values
empty_dict = {}
# Here is a prefilled dictionary
filled_dict = {"one": 1, "two": 2, "three": 3}

# Note keys for dictionaries have to be immutable types. This is to ensure that
# the key can be converted to a constant hash value for quick look-ups.
# Immutable types include ints, floats, strings, tuples.
invalid_dict = {[1,2,3]: "123"}  # => Yield a TypeError: unhashable type: 'list'
valid_dict = {(1,2,3):[1,2,3]}   # Values can be of any type, however.

# Look up values with []
filled_dict["one"]  # => 1

# Get all keys as an iterable with "keys()". We need to wrap the call in list()
# to turn it into a list. We'll talk about those later.  Note - for Python
# versions <3.7, dictionary key ordering is not guaranteed. Your results might
# not match the example below exactly. However, as of Python 3.7, dictionary
# items maintain the order at which they are inserted into the dictionary.
list(filled_dict.keys())  # => ["three", "two", "one"] in Python <3.7
list(filled_dict.keys())  # => ["one", "two", "three"] in Python 3.7+


# Get all values as an iterable with "values()". Once again we need to wrap it
# in list() to get it out of the iterable. Note - Same as above regarding key
# ordering.
list(filled_dict.values())  # => [3, 2, 1]  in Python <3.7
list(filled_dict.values())  # => [1, 2, 3] in Python 3.7+

# Check for existence of keys in a dictionary with "in"
"one" in filled_dict  # => True
1 in filled_dict      # => False

# Looking up a non-existing key is a KeyError
filled_dict["four"]  # KeyError

# Use "get()" method to avoid the KeyError
filled_dict.get("one")      # => 1
filled_dict.get("four")     # => None
# The get method supports a default argument when the value is missing
filled_dict.get("one", 4)   # => 1
filled_dict.get("four", 4)  # => 4

# "setdefault()" inserts into a dictionary only if the given key isn't present
filled_dict.setdefault("five", 5)  # filled_dict["five"] is set to 5
filled_dict.setdefault("five", 6)  # filled_dict["five"] is still 5

# Adding to a dictionary
filled_dict.update({"four":4})  # => {"one": 1, "two": 2, "three": 3, "four": 4}
filled_dict["four"] = 4         # another way to add to dict

# Remove keys from a dictionary with del
del filled_dict["one"]  # Removes the key "one" from filled dict

# From Python 3.5 you can also use the additional unpacking options
{"a": 1, **{"b": 2}}  # => {'a': 1, 'b': 2}
{"a": 1, **{"a": 2}}  # => {'a': 2}


# Sets store ... well sets
empty_set = set()

# Check if set on the left is a superset of set on the right
{1, 2} >= {1, 2, 3}  # => False

# Check for existence in a set with in
2 in filled_set   # => True
10 in filled_set  # => False

# Make a one layer deep copy
filled_set = some_set.copy()  # filled_set is {1, 2, 3, 4, 5}
filled_set is some_set        # => False


####################################################
## 3. Control Flow and Iterables
####################################################

# Let's just make a variable
some_var = 5

# Here is an if statement. Indentation is significant in Python!
# Convention is to use four spaces, not tabs.

"""
For loops iterate over lists
prints:
    dog is a mammal
    cat is a mammal
    mouse is a mammal
"""
for animal in ["dog", "cat", "mouse"]:
    # You can use format() to interpolate formatted strings
    print("{} is a mammal".format(animal))

# "range(number)"  starts at 0.
#"range(lower, upper)" returns an iterable of numbers from the lower number to the upper number, not including the last

"""
"range(lower, upper, step)" returns an iterable of numbers
from the lower number to the upper number, while incrementing
by step. If step is not indicated, the default value is 1.
prints:
    4
    6
"""
for i in range(4, 8, 2):
    print(i)


# Handle exceptions with a try/except block
try:
    # Use "raise" to raise an error
    raise IndexError("This is an index error")
except IndexError as e:
    pass                 # Refrain from this, provide a recovery (next example).
except (TypeError, NameError):
    pass                 # Multiple exceptions can be processed jointly.
else:                    # Optional clause to the try/except block. Must follow
                         # all except blocks.
    print("All good!")   # Runs only if the code in try raises no exceptions
finally:                 # Execute under all circumstances
    print("We can clean up resources here")



####################################################
## 4. Functions
####################################################

# You can do both at once, if you like
def all_the_args(*args, **kwargs):
    print(args)
    print(kwargs)
"""
all_the_args(1, 2, a=3, b=4) prints:
    (1, 2)
    {"a": 3, "b": 4}
"""

# When calling functions, you can do the opposite of args/kwargs!
# Use * to expand args (tuples) and use ** to expand kwargs (dictionaries).
args = (1, 2, 3, 4)
kwargs = {"a": 3, "b": 4}
all_the_args(*args)            # equivalent: all_the_args(1, 2, 3, 4)
all_the_args(**kwargs)         # equivalent: all_the_args(a=3, b=4)
all_the_args(*args, **kwargs)  # equivalent: all_the_args(1, 2, 3, 4, a=3, b=4)



# Python has first class functions
def create_adder(x):
    def adder(y):
        return x + y
    return adder

add_10 = create_adder(10)
add_10(3)   # => 13

# Closures in nested functions:
# We can use the nonlocal keyword to work with variables in nested scope which shouldn't be declared in the inner functions.
def create_avg():
    total = 0
    count = 0
    def avg(n):
        nonlocal total, count
        total += n
        count += 1
        return total/count
    return avg
avg = create_avg()
avg(3)  # => 3.0
avg(5)  # (3+5)/2 => 4.0
avg(7)  # (8+7)/3 => 5.0

# There are also anonymous functions
(lambda x: x > 2)(3)                  # => True
(lambda x, y: x ** 2 + y ** 2)(2, 1)  # => 5

# There are built-in higher order functions
list(map(add_10, [1, 2, 3]))          # => [11, 12, 13]
list(map(max, [1, 2, 3], [4, 2, 1]))  # => [4, 2, 3]

# We can use list comprehensions for nice maps and filters
# List comprehension stores the output as a list (which itself may be nested).
[add_10(i) for i in [1, 2, 3]]         # => [11, 12, 13]
[x for x in [3, 4, 5, 6, 7] if x > 5]  # => [6, 7]

# You can construct set and dict comprehensions as well.
{x for x in "abcddeef" if x not in "abc"}  # => {'d', 'e', 'f'}
{x: x**2 for x in range(5)}  # => {0: 0, 1: 1, 2: 4, 3: 9, 4: 16}


####################################################
## 5. Modules
####################################################

# You can shorten module names
import math as m
math.sqrt(16) == m.sqrt(16)  # => True

# Python modules are just ordinary Python files. You
# can write your own, and import them. The name of the
# module is the same as the name of the file.

# You can find out which functions and attributes
# are defined in a module.
import math
dir(math)

# If you have a Python script named math.py in the same
# folder as your current script, the file math.py will
# be loaded instead of the built-in Python module.
# This happens because the local folder has priority
# over Python's built-in libraries.


####################################################
## 6. Classes
####################################################

class Human:
    # A class attribute. It is shared by all instances of this class
    species = "H. sapiens"

    # Basic initializer, this is called when this class is instantiated.
    # Note that the double leading and trailing underscores denote objects
    # or attributes that are used by Python but that live in user-controlled
    # namespaces. Methods(or objects or attributes) like: __init__, __str__,
    # __repr__ etc. are called special methods (or sometimes called dunder
    # methods). You should not invent such names on your own.
    def __init__(self, name):
        # Assign the argument to the instance's name attribute
        self.name = name

        # Initialize property
        self._age = 0   # the leading underscore indicates the "age" property is
                        # intended to be used internally
                        # do not rely on this to be enforced: it's a hint to other devs

    # An instance method. All methods take "self" as the first argument
    def say(self, msg):
        print("{name}: {message}".format(name=self.name, message=msg))

    # A class method is shared among all instances
    # They are called with the calling class as the first argument
    @classmethod
    def get_species(cls):
        return cls.species

    # A static method is called without a class or instance reference
    @staticmethod
    def grunt():
        return "*grunt*"

    # A property is just like a getter.
    # It turns the method age() into a read-only attribute of the same name.
    # There's no need to write trivial getters and setters in Python, though.
    @property
    def age(self):
        return self._age

    # This allows the property to be set
    @age.setter
    def age(self, age):
        self._age = age

    # This allows the property to be deleted
    @age.deleter
    def age(self):
        del self._age


# When a Python interpreter reads a source file it executes all its code.
# This __name__ check makes sure this code block is only executed when this
# module is the main program.
if __name__ == "__main__":
    # Instantiate a class
    i = Human(name="Ian")
    i.say("hi")                     # "Ian: hi"
    j = Human("Joel")
    j.say("hello")                  # "Joel: hello"
    # i and j are instances of type Human; i.e., they are Human objects.

    # Call our class method
    i.say(i.get_species())          # "Ian: H. sapiens"
    # Change the shared attribute
    Human.species = "H. neanderthalensis"
    i.say(i.get_species())          # => "Ian: H. neanderthalensis"
    j.say(j.get_species())          # => "Joel: H. neanderthalensis"

    # Call the static method
    print(Human.grunt())            # => "*grunt*"

    # Static methods can be called by instances too
    print(i.grunt())                # => "*grunt*"

    # Update the property for this instance
    i.age = 42
    # Get the property
    i.say(i.age)                    # => "Ian: 42"
    j.say(j.age)                    # => "Joel: 0"
    # Delete the property
    del i.age
    # i.age                         # => this would raise an AttributeError


####################################################
## 6.1 Inheritance
####################################################

# Inheritance allows new child classes to be defined that inherit methods and
# variables from their parent class.

# Using the Human class defined above as the base or parent class, we can
# define a child class, Superhero, which inherits variables like "species",
# "name", and "age", as well as methods, like "sing" and "grunt"
# from the Human class, but can also have its own unique properties.

# To take advantage of modularization by file you could place the classes above
# in their own files, say, human.py

# To import functions from other files use the following format
# from "filename-without-extension" import "function-or-class"

from human import Human


# Specify the parent class(es) as parameters to the class definition
class Superhero(Human):

    # If the child class should inherit all of the parent's definitions without
    # any modifications, you can just use the "pass" keyword (and nothing else)
    # but in this case it is commented out to allow for a unique child class:
    # pass

    # Child classes can override their parents' attributes
    species = "Superhuman"

    # Children automatically inherit their parent class's constructor including
    # its arguments, but can also define additional arguments or definitions
    # and override its methods such as the class constructor.
    # This constructor inherits the "name" argument from the "Human" class and
    # adds the "superpower" and "movie" arguments:
    def __init__(self, name, movie=False,
                 superpowers=["super strength", "bulletproofing"]):

        # add additional class attributes:
        self.fictional = True
        self.movie = movie
        # be aware of mutable default values, since defaults are shared
        self.superpowers = superpowers

        # The "super" function lets you access the parent class's methods
        # that are overridden by the child, in this case, the __init__ method.
        # This calls the parent class constructor:
        super().__init__(name)

    # override the sing method
    def sing(self):
        return "Dun, dun, DUN!"

    # add an additional instance method
    def boast(self):
        for power in self.superpowers:
            print("I wield the power of {pow}!".format(pow=power))


    # Get the "Method Resolution Order" used by both getattr() and super()
    # (the order in which classes are searched for an attribute or method)
    # This attribute is dynamic and can be updated
    print(Superhero.__mro__)    # => (<class '__main__.Superhero'>,
                                # => <class 'human.Human'>, <class 'object'>)

    # Calls parent method but uses its own class attribute
    print(sup.get_species())    # => Superhuman


# Multiple inheritance: Define Batman as a child that inherits from both Superhero and Bat
# class Batman(Superhero, Bat):


####################################################
## 7. Advanced
####################################################

# Generators help you make lazy code.
def double_numbers(iterable):
    for i in iterable:
        yield i + i

# Generators are memory-efficient because they only load the data needed to
# process the next value in the iterable. This allows them to perform
# operations on otherwise prohibitively large value ranges.
# NOTE: `range` replaces `xrange` in Python 3.
for i in double_numbers(range(1, 900000000)):  # `range` is a generator.
    print(i)
    if i >= 30:
        break

# Just as you can create a list comprehension, you can create generator
# comprehensions as well.
values = (-x for x in [1,2,3,4,5])
for x in values:
    print(x)  # prints -1 -2 -3 -4 -5 to console/terminal

# You can also cast a generator comprehension directly to a list.
values = (-x for x in [1,2,3,4,5])
gen_to_list = list(values)
print(gen_to_list)  # => [-1, -2, -3, -4, -5]


# Decorators are a form of syntactic sugar.
# They make code easier to read while accomplishing clunky syntax.

# Wrappers are one type of decorator.
# They're really useful for adding logging to existing functions without needing to modify them.

def log_function(func):
    def wrapper(*args, **kwargs):
        print("Entering function", func.__name__)
        result = func(*args, **kwargs)
        print("Exiting function", func.__name__)
        return result
    return wrapper

@log_function               # equivalent:
def my_function(x,y):       # def my_function(x,y):
    return x+y              #   return x+y
                            # my_function = log_function(my_function)
# The decorator @log_function tells us as we begin reading the function definition
# for my_function that this function will be wrapped with log_function.
# When function definitions are long, it can be hard to parse the non-decorated
# assignment at the end of the definition.

my_function(1,2)  # => "Entering function my_function"
                  # => "3"
                  # => "Exiting function my_function"

# But there's a problem.
# What happens if we try to get some information about my_function?

print(my_function.__name__)  # => 'wrapper'
print(my_function.__code__.co_argcount)  # => 0. The argcount is 0 because both arguments in wrapper()'s signature are optional.

# Because our decorator is equivalent to my_function = log_function(my_function)
# we've replaced information about my_function with information from wrapper

# Fix this using functools

from functools import wraps

def log_function(func):
    @wraps(func)  # this ensures docstring, function name, arguments list, etc. are all copied
                  # to the wrapped function - instead of being replaced with wrapper's info
    def wrapper(*args, **kwargs):
        print("Entering function", func.__name__)
        result = func(*args, **kwargs)
        print("Exiting function", func.__name__)
        return result
    return wrapper

@log_function
def my_function(x,y):
    return x+y

my_function(1,2)  # => "Entering function my_function"
                  # => "3"
                  # => "Exiting function my_function"

print(my_function.__name__)  # => 'my_function'
print(my_function.__code__.co_argcount)  # => 2


# https://learnxinyminutes.com/pythonstatcomp/

'''
Free Online
Automate the Boring Stuff with Python
The Official Docs
Hitchhiker's Guide to Python
Python Course
First Steps With Python
A curated list of awesome Python frameworks, libraries and software
Official Style Guide for Python
Python 3 Computer Science Circles
Dive Into Python 3
Python Tutorial for Intermediates
Build a Desktop App with Python
'''