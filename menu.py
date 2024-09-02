print("\n\t\tProgram to create a menu")
print("\t\t------- -- ------ - ----")

def addition(a,b):
    add = a+b
    print("\n\tAddition of two numbers : ",add)
def subraction(a,b):
    sub = a-b
    print("\n\tSubraction of two numbers : ",sub)
def multiplication(a,b):
    mul = a*b
    print("\n\tMultiplication of two numbers : ",mul)
def division(a,b):
    div = a/b
    print("\n\tdivision of two numbers : ",int(div))


print("Menu")
print("----")
print("1. Addition")
print("2. Subraction")
print("3. Multiplication")
print("4. Division")
print("5. Exit")

while True:
    choice=int(input())
    if(choice==1):
        print("\n\tAddition")
        print("\t-----------")
        a=int(input())
        b=int(input())
        print("\n\tFirst number : ",a)
        print("\n\tSecond number : ",b)
        addition(a,b)
    elif(choice==2):
        print("\n\tsubraction")
        print("\t--------------")
        a=int(input())
        b=int(input())
        print("\n\tFirst number : ",a)
        print("\n\tSecond number : ",b)
        subraction(a,b)
    elif(choice==3):
        print("\n\tmultiplication")
        print("\t---------------")
        a=int(input())
        b=int(input())
        print("\n\tFirst number : ",a)
        print("\n\tSecond number : ",b)
        multiplication(a,b)
    elif(choice==4):
        print("\n\tdivision")
        print("\t-----------")
        a=int(input())
        b=int(input())
        print("\n\tFirst number : ",a)
        print("\n\tSecond number : ",b)
        division(a,b)
    elif(choice==5):
        print("\n\tExit")
    else:
       print("Invalid value")
       break
    
