print("\n\n\t\tFinding the given string is palindrome or not")
print("\t\t------- --- ------ ------ -- ---------- -- ---")
a=input()
print("\n\n\tThe given string is ",a)
rev=""
for i in a:
    rev = i + rev

if(a==rev):
    print("\n\tThe given string ",a," is palindrome")
else:
     print("\n\tThe given string ",a," is  not palindrome")
