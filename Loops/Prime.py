n=int(input("Enter the total number of prime number you want: ")) # 3
count=2
while n>0:
    flag=0
    for i in range(2,count//2+1):
        if count%i==0:
            flag=1
            break
    if flag==0:
        n-=1
        print(count)
  
    count+=1

    
