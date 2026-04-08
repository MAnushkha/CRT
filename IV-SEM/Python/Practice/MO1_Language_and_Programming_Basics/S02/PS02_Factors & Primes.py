#Read a number from the user and print all the factors of that number. 
'''
N = int(input())
for i in range(1, N // 2 + 1):
    if N % i == 0:
        print(i, end = " ")
'''
#Read a number from the user and count the number of factors and display the count.
'''
N = int(input())
count = 0
for i in range(1, N // 2 + 1):
    if N % i == 0:
        count += 1 
print(count + 1)      

#Prime number 
N = int(input())
count = 0
for i in range(1, N // 2 + 1):
    if N % i == 0:
        count += 1  
print("Prime" if count == 0 else "Not Prime")       
'''
#Display all the prime numbers between 1 and N (both inclusive).
'''
start = int(input())
end = int(input())
if start == 1:
    start = 2
for N in range(start, end + 1):
    count = 0
    for i in range(2, N // 2 + 1):
        if N % i == 0:
            count += 1
    if count == 0:
        print(N, end = " ")
'''
#Factorial of a number
'''
N = int(input())
if N < 0:
    print("Factorial does not exist for negative numbers")
elif N == 0 or N == 1:
    print(1)
else:
    factorial = 1
    for i in range(1, N + 1):
        factorial *= i
    print(factorial)
'''
#GCD of two numbers
