# This program sorts a list of 4 numbers

num1 = input("Please enter your first number: ")
num2 = input("Please enter your second number: ")
num3 = input("Please enter your third number: ")
num4 = input("Please enter your fourth number: ")\


# numList = [22,22,22,56] # Placeholder list for testing

numList = [num1, num2, num3, num4] # Create a list from user input
sortedList = [] # Empty list that will be added onto

while numList: # Iterate through the list of numbers
    tempVar = numList[0] # Assign tempVar to the first number in the list

    for num in numList: # For all numbers in the list compare them to the tempVar to find the lowest
        if num < tempVar:
            tempVar = num

    sortedList.append(tempVar) # Add the lowest number onto the list
    numList.remove(tempVar) # Remove the lowest number from the numList to prevent repeats

print(sortedList) # Finally print the sorted list