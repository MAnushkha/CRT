'''N = int(input("Enter a number: "))
count = 0
while N > 0:
    count += 1
    N = N // 10
print(count)
print(len(str(N)))
''
N = int(input())
temp = 0
s = 0
while N > 0:
    s += (N % 10)
    N //= 10
print(s)
print(sum(map(int, str(temp))))
'''
# odd and even count 
'''
N = int(input())              
even = odd = 0
while N > 0:
    if (N % 2) == 0:
        even += 1
    else:
        odd += 1
    N //= 10
print(even, odd)  
'''
N = int(input())
while N > 9:
    N = sum(map(int, str(N)))
print(N)
