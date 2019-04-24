print('Problem 3:');

#Prime Factors
number = int(input('What is the number you want to find its prime factors ? '))
count = 0;
largest_prime = 1;
x = 1;

for x in range(1, number):
    if number % x == 0: #iterate to find the factors of the input

        for i in range(1, x):
            if x % i == 0:
                count = count + 1;

        if count == 1:
            #print('Yes!',x)
            if x > largest_prime:
                largest_prime = x;

        count = 0;

print('Largest Prime Factor:', largest_prime)
