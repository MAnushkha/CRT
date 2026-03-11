'''
Armstrong number:
input: 153
output: 153 is an Armstrong number
input: 24
output: 24 is not an Armstrong number

N = int(input())
count = len(str(N))
s = 0
for digit in str(N):
    int(digit) **= count
    s += int(digit) ** count 
print("Armstrong number" if s == N else "Not an Armstrong number")
Perfect number:
input: 6
output: 6 is a perfect number
6 ===> 1, 2, 3
1 + 2 + 3 = 6
N = int(input())
s = 0
for i in range(1, N // 2 + 1):
    if N % i == 0:
        s += i
print("Perfect number" if s == N else "Not a perfect number")
Strong number:
input: 123
output: 
Explanation: 1! + 2! + 3! = 1 + 2 + 6 = 9
'''
def factorial(n):
    if n < 0:
        return "Factorial does not exist for negative numbers"
    elif n == 0 or n == 1:
        return 1
    else:
        factorial = 1
        for i in range(1, n + 1):
            factorial *= i
        return factorial
N = int(input())
s = 0
for digit in str(N):
    s += factorial(int(digit))
print("Strong number" if s == N else "Not a strong number")
