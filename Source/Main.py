from BasicListTester import BasicListTester
from LinkedListTester import LinkedListTester

linkedListTester = LinkedListTester()

linkedListTester.printTestCases()
print("\r\n")

### Reversing Linked List
print("Reversing linked list...")
linkedListTester.reverseTestCases()
print("After reversing: ")
linkedListTester.printTestCases()
print("\r\n")

### Removing linked list nodes by index
indexToRemove = 11
print("Removing at index ", indexToRemove)
linkedListTester.removeAtTestCases(indexToRemove)
print("\r\n")
linkedListTester.printTestCases()
print("\r\n")

### Inserting into linked list by index
indexToInsert = 9
valueToInsert = 100
print("Inserting at index ", indexToInsert)
linkedListTester.insertAtTestCases(valueToInsert, indexToInsert)
print("\r\n")
linkedListTester.printTestCases()
print("\r\n")
