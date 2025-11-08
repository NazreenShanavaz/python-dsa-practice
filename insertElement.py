def insertElement(nums, m, val):
    i=m-1
    while i>=0 and nums[i]>val:
        nums[i+1]=nums[i]
        i-=1
    nums[i+1]=val
    return nums
    
nums=[1,3,5,0,0]
m=3
val=4
print(insertElement(nums, m, val))
    
        