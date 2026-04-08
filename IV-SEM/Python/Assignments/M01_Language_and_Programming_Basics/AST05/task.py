from typing import List


def Collatz_Sequence(n: int)-> List:
   seq = [n]
   while n != 1:
     if n % 2 == 0:
         n = (n//2)
     elif n % 2 == 1:
         n = 3 * n + 1
     seq.append(n)
   return seq

if __name__ == '__main__':
    n = int(input())
    print(Collatz_Sequence(n))