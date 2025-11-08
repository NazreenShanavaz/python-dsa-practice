def remove_duplicates(nums):
    """
    Removes duplicates from a sorted list in-place.

    Parameters:
    nums (list): A sorted list of integers.

    Returns:
    int: The number of unique elements.
    """
    if not nums:
        return 0
    k=1
    for i in range(1, len(nums)):
        if nums[i] != nums[k-1]:
            nums[k]=nums[i]
            k+=1
    return k
numm1 = input("Enter the sorted list of numbers: ")
nums = list(map(int,numm1.split()))
k = remove_duplicates(nums)
print("Number of unique elements:", k)
print("List after removing duplicates:", nums[:k])