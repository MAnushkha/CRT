def number_triangle(n: int) -> str:
    result = ""
    
    
    for i in range(1, n + 1):
        for j in range(1, i + 1):
            result += str(j)
        if i != n:
            result += "\n"
    
    return result