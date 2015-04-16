def fibonacci(n):
    a = 1
    b = 1
    c = a + b
    for i in range (n-1):
        a = b
        b = c
        c = a + b
    return a

n = int(input("Entero positivo: "))
fib = fibonacci(n)
print("Fibonacci: "fib)  
