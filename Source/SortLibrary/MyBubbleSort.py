def listSwapAtIndexes(list, indexA, indexB):
    temp = list[indexA]
    list[indexA] = list[indexB]
    list[indexB] = temp

def bubbleSort(list):
    hasSorted = False;
    for index in range(0, len(list) - 1):
        if list[index] > list[index  + 1]:
            listSwapAtIndexes(list, index, index + 1)
            hasSorted = True;

    if (hasSorted):
        bubbleSort(list)
