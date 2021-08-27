# arguments
def my_function(x):
  print(x + " bombadi")

my_function("hava")
my_function("heyat")
my_function("python")

# defoult parametrer value

def my_function(country = "Azerbaijan"):
  print("I am from " + country)

my_function("Turkey")
my_function("India")
my_function()
my_function("Brazil")

# Passing a List as an Argument

def my_function(food):
  for x in food:
    print(x)

fruits = ["apple", "banana", "cherry"]

my_function(fruits)

# return

def my_function(x):
  return 5 * x

print(my_function(3))
print(my_function(5))
print(my_function(9))