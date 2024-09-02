print("\n\t\tBIGGEST AMONG THREE NUMBERS")
print("\t\t------- ----- ----- --------")
a=int(input())
b=int(input())
c=int(input())
print("\n\tThe given values are ",a, " ",b," "," ",c)
if(a>b):
    if(a>c):
        print("\n\tThe biggest value is ",a)
    else:
        print("\n\tThe biggest value is ",c)
else:
    if(b>c):
        print("\n\tThe biggest value is ",b)
    else:
        print("\n\tThe biggest value is ",c)

