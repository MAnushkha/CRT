def Lower_bound(li, x):
    low, high = 0, len(li) - 1
    while low < high:
        mid = (low + high) // 2
        if li[mid] < x:
            low = mid + 1
        else:
            high = mid 
    return low 

print(Lower_bound([10, 15, 23, 27, 30, 35, 36], 25))
print(Lower_bound([10, 15, 23, 27, 30, 35, 36], 33))
print(Lower_bound([10, 15, 23, 27, 30, 35, 36], 40))

