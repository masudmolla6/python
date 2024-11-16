x=lambda a,b,c:a+b+c
print(x(5,20,30))

def my_func(n):
    y=lambda c,d:c+d+n
    return y

result=my_func(40)
print(result(20,39))

def make_double(n):
    return lambda a:n*a
double=make_double(10)
print(double(3))