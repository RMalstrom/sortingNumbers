import unittest

def customSort(numList):
    sortedList = []  # Empty list that will be added onto

    while numList:  # Iterate through the list of numbers
        tempVar = numList[0]  # Assign tempVar to the first number in the list

        for num in numList:  # For all numbers in the list, compare them to tempVar to find the lowest
            if num < tempVar:
                tempVar = num

        sortedList.append(tempVar)  # Add the lowest number onto the list
        numList.remove(tempVar)  # Remove the lowest number from the numList to prevent repeats

    return sortedList  # Return the sorted list instead of printing

# Testing
class TestCustomSort(unittest.TestCase):
    def testExpectedList(self):  # Test for expected values
        self.assertEqual(customSort([4, 1, 3, 2]), [1, 2, 3, 4])

    def testRepeatedCase(self):  # Test for mostly repeated values
        self.assertEqual(customSort([2, 1, 1, 1]), [1, 1, 1, 2])

    def testPreSorted(self):  # Test a list that is already sorted
        self.assertEqual(customSort([1, 2, 3, 4]), [1, 2, 3, 4])

if __name__ == '__main__':
    unittest.main()
