print("\n\t\tPrime Number Between 2 Numbers")
print("\t\t----- ------ ------- - -------\n")
lower=int(input())
upper=int(input())
print("prime number between ",lower," and ",upper)
for num in range(lower,upper):
        if(num>1):
            for i in range(2,num):
                    if((num%i)==0):
                            break
            else: 
                print("\n\t",num)
             
          
    
