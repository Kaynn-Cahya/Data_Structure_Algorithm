from SortLibrary.MyBubbleSort import bubbleSort
from SearchLibrary.MyBinarySearch import tryBinarySearch
from SortLibrary.MyQuickSort import quickSort
from Utils import *

class BasicListTester:
    def __init__(self):
        self.testCases = generateTestCases()
        self.isSorted = False;

    def testBubbleSort(self):
        self.warnIfAlreadySorted()
        for testCase in self.testCases:
            bubbleSort(testCase)
        self.isSorted = True
        self.printTestCases()

    def testBinarySearch(self):
        if self.isSorted == False:
            print("ERR: Sort the list first before doing a binary search")
            return

        for testCase in self.testCases:
            print("\r\nCurrent case: ", testCase)
            target = getNumericalInput("Please input a target number to search in the list: ")

            success, result = tryBinarySearch(testCase, target)
            if success:
                print("Found object at index: ", result)
            else:
                print("Target object is not found in the list!")

    def testQuickSort(self, useLomutoPartition):
        self.warnIfAlreadySorted()
        for testCase in self.testCases:
            quickSort(testCase, useLomutoPartition)
        self.isSorted = True
        self.printTestCases()


#region Utils

    def warnIfAlreadySorted(self):
        if self.isSorted:
            print("WARN: Everything is already sorted!")

    def generateNewTestCases(self):
        self.testCases = generateTestCases()
        self.isSorted = False;

    def printTestCases(self):
        for item in self.testCases:
            print(item)
        print("Is sorted: ", self.isSorted)

#endreigon
