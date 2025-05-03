arr=[4, 1, 3, 9, 7]
for i in range(len(arr)):
    min=arr[0]
    for j in range(i+1,len(arr)):
        if arr[j]<arr[i]:
            temp=arr[i]
            arr[i]=arr[j]
            arr[j]=temp
for i in range(len(arr)):
    print(arr[i])   