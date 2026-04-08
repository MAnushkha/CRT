def sum_of_digits(n: int) -> int:
    n = abs(n)  # handle negative numbers
    total = 0
    
    while n > 0:
        total += n % 10   # get last digit
        n //= 10          # remove last digit
    
    return total
if __name__ == "__main__":
    n = int(input())
    print(sum_of_digits(n))
