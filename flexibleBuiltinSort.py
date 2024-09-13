numList = [] # Declare empty list of numbers
cont = True # Declare loop continuation variable

while cont:
    userNumber = int(input("Please enter your numbers to sort, enter -99 to exit."))
    if userNumber == -99: # If user enters exit number, break out of the loop
        break
    else:
        numList.append(userNumber) # Add number to the end of the list

print(sorted(numList))