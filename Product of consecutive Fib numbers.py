def productFib(prod):
    fib, i = [0, 1], 1
    if prod == 1:
        return [1, 1, True]
    while fib[len(fib)-1] < prod**0.5:
        fib.append(fib[i]+fib[i-1])
        i+=1
    if fib[len(fib)-1]*fib[len(fib)-2] == prod or fib[len(fib)-1]==1:
        return [fib[len(fib)-2], fib[len(fib)-1], True]
    else:
        if fib[len(fib) - 2] * fib[len(fib) - 1] > prod:
            return [fib[len(fib)-2], fib[len(fib)-1], False]
        else:
            return [fib[len(fib)-1], fib[len(fib)-1]+fib[len(fib)-2], False]
