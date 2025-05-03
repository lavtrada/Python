n=int(input("Enter the number: "))
fact=1
# while n>0:
#     fact=fact*n
#     n-=1
# print(fact) # Output: 120

for i in range(1,n+1):
    fact=fact*i
print(fact) # Output: 120

