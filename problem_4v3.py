print('Problem 4:');

finalAnswer = 1;

def numToArray (number):
    arrayOut = [];
    while (number >= 1):
        digit = number % 10;
        number = number / 10;
        if (digit < 10):
            digit = int(digit);
        arrayOut.append(digit);
    return arrayOut;

def palindromeCheck (number):
    length = len(number);
    check = length - 1; #to interate through the current number
    x = 0;
    reverseNumber = []; #declare reverseNumber to be the same legnth as number
    while (check >= 0):
        reverseNumber.append(number[check]);
        check = check - 1;
    if number == reverseNumber:
        x = 1;
    return x;

def problemFour ():
    num1 = 1;
    num2 = 1;
    result = 1;
    check = 1;
    answer = 0;
    largestPalindrome = 0;

    for num1 in range(100,1000):
        for num2 in range(100,1000):
            result = num1 * num2;
            check = numToArray(result);
            answer = palindromeCheck(check);
            if answer == 1:
                if result > largestPalindrome:
                    largestPalindrome = result;
                #print("A palindromic number is: ", result)
    return (largestPalindrome)


finalAnswer = problemFour();
print('The largest palindromic number is: ',finalAnswer);
