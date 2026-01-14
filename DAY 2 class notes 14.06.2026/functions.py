def addition(a,b):
    print(a+b)
def subtraction(a,b):
    print("Subtraction",a-b)
def multiplication(a,b):
    print("Multiplication",a*b)
def division(a,b):
    print("Division",a/b)

addition(50,20)
subtraction(70,30)
multiplication(4,5)
division(5,4)

def hello(greeting="Hello",name="world"):
    print('%s,%s' %(greeting,name))
hello()
hello('greeting','deepa')
def print_param(*params):
        print(params)
        print_param("testing")
        print_param(1,2,3,4)
        def print_param(**params):
            print(params)

        print_param(x=1,y=2,z=3)