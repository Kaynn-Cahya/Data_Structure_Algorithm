def listSwapAtIndexes(list, indexA, indexB):
    temp = list[indexA]
    list[indexA] = list[indexB]
    list[indexB] = temp

def brickSort(list):
    isSorted = False
    while isSorted == False:
        isSorted = True
        for index in range(1, len(list) - 1, 2):
            if list[index] > list[index + 1]:
                listSwapAtIndexes(list, index, index + 1)
                isSorted = False
        for index in range(0, len(list) - 1, 2):
            if list[index] > list[index + 1]:
                listSwapAtIndexes(list, index, index + 1)
                isSorted = False
