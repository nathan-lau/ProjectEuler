print('Problem 2:');

fib_new = 0;
fib_prev_1 = 0; #the 1st starting value
fib_prev_2 = 1; #the 2nd starting value
fib_sum = 0;

while fib_new < 4000000:
    fib_new = fib_prev_1 + fib_prev_2;
    print(fib_new)
    fib_prev_1 = fib_prev_2;
    fib_prev_2 = fib_new;

    if fib_new % 2 == 0:
        fib_sum = fib_sum + fib_new

print('Total Value:', fib_sum)
