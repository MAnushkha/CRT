'''
input: 4
output:
* * * * 
* * * *
* * * *
* * * *

N = int(input())
for i in range(1, N + 1):
    for j in range(1, N + 1):
        print("*", end = " ")
    print()    

n = 4                                    n = 4
*                                        * * * *
* *                                      * * * 
* * *                                    * *
* * * *                                  *
N = int(input())
for i in range(1, N + 1):
    for j in range(i):
        print("*", end = " ")
    print()
n = 4                               n = 4
A                                   * * * *
A B                                 *     *
A B C                               *     *
A B C D                             * * * *