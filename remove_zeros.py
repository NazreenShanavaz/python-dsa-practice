def remove_zeros(num1):
    """
    Removes all zeros from the input list.

    Parameters:
    num1 (list): A list of integers.

    Returns:
    list: A new list with all zeros removed.
    """
    k=0
    for i in range(len(num1)):
        if num1[i]!=0:
            num1[k]=num1[i]
            k+=1
    return num1[:k]

numm1 = input("Enter the list of numbers: ")
num1 = list(map(int,numm1.split())) 
print("List after removing zeros:", remove_zeros(num1))
    