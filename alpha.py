print("\n\n\t\tCOUNT THE ALPHABETS IN THE GIVEN STRING")
print("\t\t----- --- --------- -- --- ----- ------")
a=r"king1"
print("The given string is",a)
count=0
num=0
for i in a:
    if(i.isalpha()):
        count=count+1
    else:
        num=num+1
print("\n\tNumber of the alphabets in the given string",a,"is",count)
if(num!=0):
    print("\n\tNumber of the Digits in the given string",a,"is",num)

