import math

def tryBinarySearch(list, target):
    currHead = len(list) -1
    currTail = 0
    while currTail <= currHead:
        currentHalfwayPoint = math.floor((currHead + currTail) / 2)
        if list[currentHalfwayPoint] < target:
            currTail = currentHalfwayPoint + 1
        elif list[currentHalfwayPoint] > target:
            currHead = currentHalfwayPoint - 1
        else:
            return True, currentHalfwayPoint

    return False, -1
