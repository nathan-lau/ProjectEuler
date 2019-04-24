print('Problem 9:');

import math

sum = 0;
product = 1;

def calculateHypo(num1, num2) :
    hypo = (num1 * num1) + (num2 * num2)
    hypo = math.sqrt(hypo)
    return hypo

for a in range (1,1000) :
    for b in range (1,1000) :
            c = calculateHypo(a,b);
            sum = a + b + c;
            if sum == 1000 :
                product = a * b * c;
                print('The three numbers that add to 1000 are: ', a, b, c)
                print('Product of a, b & c', product)
