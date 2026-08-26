def bubblesort(lst):
    n = len(lst)
    for i in range(n):
        for j in range(n - i - 1):
            if lst[j] > lst[j+1]:
                lst[j], lst[j+1] = lst[j+1], lst[j]
list = [19,2,31,45,6,11,121,27]
bubblesort(list)
print(list)