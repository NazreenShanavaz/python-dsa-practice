def find_missing_number(nums):
    n = len(nums) + 1  
    total = n * (n + 1) // 2
    actual_sum = sum(nums)
    missing = total - actual_sum
    return missing


lst = input("Enter numbers from 1 to n (with one missing): ")
nums = list(map(int, lst.split()))

print(f"Missing number is: {find_missing_number(nums)}")
