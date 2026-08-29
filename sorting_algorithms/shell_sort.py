def shell_sort(input_list):
    gap = len(input_list) // 2
    while gap > 0:
        for i in range(gap, len(input_list)):
            temp = input_list[i]
            j = i

            while j >= gap and input_list[j - gap] > temp:
                input_list[j] = input_list[j - gap]
                j = j-gap
            input_list[j] = temp
        gap = gap // 2

lst = [19, 53, 15, 67, 2, 68, 15, 9, 1]
shell_sort(lst)
print(lst)