import sys

def Student_Grade_System(name:str,n1: int,n2: int,n3: int) -> str:
   
   avg = (n1 + n2 + n3) / 3
   avg_trunc = int(avg * 100) / 100
   if avg >= 40:
      status = "Pass"
   else:
      status = "fail"
   return f"Average grade: {avg_trunc}, Status: {status}"

if __name__ == '__main__':
    if len(sys.argv) > 1:
        name = sys.argv[1]
        n1, n2, n3 = map(int, sys.argv[2:5])
    else:
        name = input()
        n1,n2,n3 = list(map(int,input().split()))
    print(Student_Grade_System(name,n1,n2,n3))

