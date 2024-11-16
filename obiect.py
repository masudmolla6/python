# class MyClass:
#     x=4
# p1=MyClass()
# print(p1.x)

# class Person:
#     def __init__(self, name, age):
#         self.name=name,
#         self.age=age
# 
# p1=Person("Masud", 26)
# print(p1.name)
# print(p1.age)


class Person:
    def __init__(self, name,age):
        self.name=name
        self.age=age
    def __str__(self):
        return f"{self.name}({self.age})"
p2=Person("Masud", 26)
# print(p2)


class User:
    def __init__(self, name, age):
        self.name=name
        self.age=age

    def my_func(self):
        print("Hello My Name is", self.age)
u1=User("Masud", 26)
# u1.name="Masud Rana"
# del u1.name
# del u1
# u1.my_func()


userName=input("Enter Your Name: ")
print(userName)
