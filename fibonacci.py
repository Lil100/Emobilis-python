def fibonacci(n):
    fib_sequence= [0,1] #initialize the first 2 numbers of the fibonacci sequence
    while len(fib_sequence) < n: #create a loop that will run as long as the length of the list is <n
        fib_sequence.append(fib_sequence[-1] + fib_sequence[-2]) #gets sum of 1st and 2nd last numbers in the list, adds the result to the new list
    return fib_sequence[:n] #return the first n elements of the fib_sequence

print(fibonacci(10)) #usage