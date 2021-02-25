def fib(a):
    x = 0
    j = 1
    save = 0
    for _ in range(int(a)):
        print(x)
        save = x
        x = j
        j = x+save

    return x

a = int(input("Enter Fib: "))

fib(a)