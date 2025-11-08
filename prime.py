def prime(num):
    if num <= 1:
        return False 
    for i in range(2, num):
        if num % i == 0:
            return False  
    return True  

num = int(input('enter the number:'))
if prime(num):
    print('it is a prime no')
else:
    print('not prime')