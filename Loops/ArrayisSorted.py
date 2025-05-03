nums=[3,4,5,1,2]
drop=0
for i in range(len(nums)-1):
    if nums[i]>nums[i+1]:
        drop+=1
if drop<=1:
    print("true")
else:
    print("false")
