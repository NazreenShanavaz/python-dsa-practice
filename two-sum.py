def two_sum(nums,target):
    prevMap = {}
    for i,n in enumerate(nums):
        diff = target - n
        if diff in prevMap:
            return[prevMap[diff],i]
        prevMap[n]=i
    return None

numss=input('enter the numbers:')
nums=list(map(int,numss.split()))
target=int(input('enter the target:'))

result=two_sum(nums,target)
if result:
    i, j = result
    print(f"Numbers: {nums[i]} + {nums[j]} = {target}")
else:
    print("No two numbers add up to the target.")