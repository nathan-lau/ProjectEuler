print('Problem 4')

num1 = 1;
num2 = 1;
result = 1;
palindrome = 1;
rev = 0;
c = [];

for num1 in range(1, 3):
    for num2 in range(1,3):
        result = num1 * num2;
        #print('Answer:', result)

        b = str(result)
        print (b)

        for digit in b:
            c.append (int(digit))
            print ('Result for C', c)
    c.remove
