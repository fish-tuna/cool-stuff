def mergeSort(nums: List[int]) -> int:
    old = []
    new = []
    for i in nums:
        old.append([i])
    while len(old) != 1:
        for i in range(len(old))[::2]:
            if i < len(old) - 1:
                j = 0
                k = 0
                newArr = []
                while j < len(old[i]) and k < len(old[i + 1]):
                    if old[i][j] < old[i + 1][k]:
                        newArr.append(old[i][j])
                        j += 1
                    else:
                        newArr.append(old[i + 1][k])
                        k += 1
                if j == len(old[i]):
                    newArr += old[i + 1][k:]
                else:
                    newArr += old[i][j:]
                new.append(newArr)
            else:
                new.append(old[i])
        old = new
        new = []
    return old[0][0]
    
print(mergeSort([4, 5, 6, 7, 0, 1, 2, 3])) # Outputs 0
