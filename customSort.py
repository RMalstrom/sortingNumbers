# This program sorts a list of 4 numbers without use of min() max()

# INCOMPLETE NON FUNCTIONAL

num1 = input("Please enter your first number: ")
num2 = input("Please enter your second number: ")
num3 = input("Please enter your third number: ")
num4 = input("Please enter your fourth number: ")

numList = [num1,num2,num3,num4]
sortedList = []
counter = 0
while counter < numList.__sizeof__():
    interval = 0
    if (numList.pop(interval) < numList.pop(interval + 1)):
        largestNum = numList.pop(interval + 1)
        interval = interval + 1
    else:
        largestNum = numList.pop(interval)
        interval = interval + 2
        #this is a test