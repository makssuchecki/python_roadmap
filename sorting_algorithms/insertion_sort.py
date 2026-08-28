def insertion_sort(InputList):
    for i in range(1, len(InputList)):
        j = i-1
        nxt_element = InputList[i]

        while (InputList[j] > nxt_element) and (j >= 0):
            InputList[j + 1] = InputList[j]
            j=j-1
        InputList[j+1] = nxt_element

lst = [19, 2, 45, 51, 6, 19, 7]
insertion_sort(lst)
print(lst)