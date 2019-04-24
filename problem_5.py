print('Problem 5:');

#number = int(input('Enter Number: '))
remainderCheck = 20;
startingNumber = 2500;

while remainderCheck > 0 :
    if (startingNumber % remainderCheck) == 0:
        remainderCheck = remainderCheck - 1;
    else :
        startingNumber = startingNumber + 1;
        remainderCheck = 20;

print(startingNumber);
