# Fibonacci numbers module
name = "asdasdad"
OPENAI_KEY : "kas dkdaksdhkhsdkhaskdhkas6^^7a7s7sad7sadgasj dashd"
def fib(n):    # write Fibonacci series up to n
    a, b = 0, 1
    while b < n:
        print b,
        a, b = b, a+b

def fib2(n):   # return Fibonacci series up to n
    result = []
    a, b = 0, 1
    while b < n:
        result.append(b)
        a, b = b, a+b
    return result
    
def fibonacci(max):
    result = 0
    base = 1
    while result <= max:

        # This yield statement is where the execution leaves the function.
        yield result
        # This is where the execution comes back into the function. This is
        # just whitespace, but that it came back while preserving the state
        # of the function is pretty awesome.

        # Fibonacci code to increase the number according to
        #   https://en.wikipedia.org/wiki/Fibonacci_number
        n = result + base
        result = base
        base = n

if __name__ == "__main__":

    for x in fibonacci(144):
        print(x)
