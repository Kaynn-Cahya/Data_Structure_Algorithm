import random

def generateTestCases(count = 5):
    testCases = []
    for generatedCount in range(0, count):
        temp = []
        testCaseLength = random.randint(5,20)
        for testCaseItem in range(0, testCaseLength):
            temp.append(random.randint(0,100))
        testCases.append(temp)
    return testCases

def isNumber(s):
    try:
        int(s)
        return True
    except ValueError:
        return False

def getNumericalInput(askMessage):
    userInput = "something"
    while isNumber(userInput) != True:
        print(askMessage)
        userInput = input()
    return int(userInput)
