print('Problem 1:');

sum1 = 0;
sum2 = 0;
sum3 = 0;
total = 0;

for x in range(1, 1000):
    if x % 3 == 0:
        sum1 = sum1 + x;
            #print('Interation3', x)
            #print('Sum1', sum1)
    if x % 5 == 0:
        sum2 = sum2 + x;
        #print('Interation5', x)
        #print('Sum2', sum2)
    if x % 3 == 0:
        if x % 5 == 0:
            sum3 = sum3 + x;

total = sum1 + sum2 - sum3;
print('Total:', total)
