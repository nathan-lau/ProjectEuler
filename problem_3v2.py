print('Problem 3:');

#Prime Factors
num = int(input('What is the number you want to find its prime factors ? '))
prime = 2;

print('Input:', num)

while num > prime * prime :
    if num % prime == 0:
        print('Prime factor: ', prime)
        num = num / prime; #divide by prime number. This will eliminate non-primes
    else:
        prime = prime + 1;
        #move on to the next integer to try

print('Largest Prime Factor: ', num)


#print('Largest Prime Factor:', largest_prime)
