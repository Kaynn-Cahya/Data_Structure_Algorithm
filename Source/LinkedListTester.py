from DataStructureLibrary.SinglyLinkedList import SinglyLinkedList
from SortLibrary.MyQuickSort import quickSort
from Utils import *

class LinkedListTester:

    def __init__(self):
        self.generateNewTestCases();

    def printTestCases(self):
        for testCase in self.testCases:
            testCase.display()

    def reverseTestCases(self):
        for testCase in self.testCases:
            testCase.reverse()

    def insertAtTestCases(self, value, indexToInsertAt):
        testCaseNo = 0
        for testCase in self.testCases:
            print("\r\n Inserting test case #", testCaseNo)
            testCase.insert(value, indexToInsertAt)
            testCaseNo = testCaseNo + 1

    def removeAtTestCases(self, indexToRemoveAt):
        testCaseNo = 0
        for testCase in self.testCases:
            print("\r\n Removing test case #", testCaseNo)
            testCase.removeAtIndex(indexToRemoveAt)
            testCaseNo = testCaseNo + 1

    def generateNewTestCases(self):
        self.testCases = []
        testCases = generateTestCases()
        for testCase in testCases:
            newLinkedList = SinglyLinkedList()
            # Ensures that all the linked lists are sorted
            quickSort(testCase, False)
            newLinkedList.fromList(testCase)
            self.testCases.append(newLinkedList)
