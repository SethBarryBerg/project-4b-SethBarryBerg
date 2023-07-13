def fib(inputn):
    n1 = 1
    n2 = 1
    count = 0
    while count<inputn:
        term = n1
        next = n1 + n2
        n1 = n2
        n2 = next
        count += 1
    return term
print(fib(3))