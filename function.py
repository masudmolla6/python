# def my_name(firstName, lastName):
#     print("My Name is ",firstName +" "+lastName)
#
#
# my_name("Masud", "Rana")
from copyList import result


# def my_function(*kids):
#     print("The Youngest child is", kids[0])
#
# my_function("Rahim", "Karim", "Kadir")
# def my_function(child3, child2, child1):
#   print("The youngest child is " + child2)
#
# my_function(child1 = "Emil", child3 = "Tobias", child2 = "Linus")

# def my_function(country = "Norway"):
#   print("I am from " + country)

# my_function("Sweden")
# my_function("India")
# my_function()
# my_function("Brazil")

def food_function(food):
    for x in food:
        print(x)

# fruits = ["apple", "banana", "cherry"]
# food_function(fruits)

# def make_double(number):
#     return number*5

# result=make_double(3)
# print(result)

# def make_pfunc(x, /):
#     print(x)
# make_pfunc(6)
# def make_pfunc(x, /):
#     print(x)
# make_pfunc(x=23)


# def my_func(*,x):
#     print(x)
# my_func(x=45)

# def my_function(a, b, /, *, c, d):
#     print(a+b+c+d)
# my_function(2,3,c=5,d=6)

def tri_recursion(k):
  if(k > 0):
    result = k + tri_recursion(k - 1)
    print(result)
  else:
    result = 0
  return result

print("Recursion Example Results:")
tri_recursion(6)