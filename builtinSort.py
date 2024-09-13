import random
timeToRepeat = 25 # This controls the amount of times to repeat the sorting with random numbers

while timeToRepeat > 0:

    # Generate 4 random numbers to sort.
    num1 = random.randint(1,100)
    num2 = random.randint(1,100)
    num3 = random.randint(1,100)
    num4 = random.randint(1,100)

    # Print the sorted list of numbers
    print(sorted([num1,num2,num3,num4]))

    # Count down timeToRepeat
    timeToRepeat = timeToRepeat - 1
