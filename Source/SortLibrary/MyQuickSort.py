import math

def listSwapAtIndexes(list, indexA, indexB):
    temp = list[indexA]
    list[indexA] = list[indexB]
    list[indexB] = temp

def quickSort(list, useLomutoPartition = True):
    tail = 0
    head = len(list) - 1
    if tail < head:
        if useLomutoPartition:
            p = lomutoPartition(list, tail, head)
            recQuickSort(list, tail, p - 1, useLomutoPartition)
            recQuickSort(list, p + 1, head, useLomutoPartition)
        else:
            p = hoarePartition(list, tail, head)
            recQuickSort(list, tail, p, useLomutoPartition)
            recQuickSort(list, p + 1, head, useLomutoPartition)

def recQuickSort(list, tail, head, useLomutoPartition):
    if tail < head:
        if useLomutoPartition:
            p = lomutoPartition(list, tail, head)
            recQuickSort(list, tail, p - 1, useLomutoPartition)
            recQuickSort(list, p + 1, head, useLomutoPartition)
        else:
            p = hoarePartition(list, tail, head)
            recQuickSort(list, tail, p, useLomutoPartition)
            recQuickSort(list, p + 1, head, useLomutoPartition)

def lomutoPartition(list, tail, head):
    pivot = list[head]
    currIndex = tail
    for i in range(tail, head):
        if list[i] < pivot:
            listSwapAtIndexes(list, currIndex, i)
            currIndex = currIndex + 1
    listSwapAtIndexes(list, currIndex, head)
    return currIndex

def hoarePartition(list, tail, head):
    pivot = list[math.floor(tail + (head - tail)/ 2)]
    while True:
        while list[tail] < pivot:
            tail = tail + 1

        while list[head] > pivot:
            head = head - 1

        if tail >= head:
            return head

        listSwapAtIndexes(list, tail, head)
        tail = tail + 1
        head = head - 1
