# string frormating
from addItems import mySelf

number1=45
number2=56
x="is"
# print(f"Our Result {x}", number1+number2)

price=45645

text=f"The price is {price:,} dollar"
print(text)

# sum=f"Result is {50+(4*5)}"
# print(sum)

penPrice=60
result=f"Pen Price is Very {"Expensive" if penPrice > 50 else "cheap"}"

# print(result)

fruits="apple"

me=f"I Love {fruits.upper()}"
# print(me)

def my_name(name):
    return name

mySelf8=f"My Name is {my_name("Masud Rana")}"
# print(mySelf8)

roll=34
name="Masud"
student1="The student name is {0} and roll is {1}"
# print(student1.format(name, roll))

myOrder="I have a {carname}, it is a {model}"
print(myOrder.format(carname="volvo", model="Mustang"))