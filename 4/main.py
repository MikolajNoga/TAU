def delta_function(a, b, c):
    return b * b - (4 * a * c)


def fibonacci(n):
    if n in {0, 1}:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)


def gcd(a, b):
    while b:
        a, b = b, a % b
    return a


if __name__ == '__main__':
    flag = 1
    choose = 0
    while flag:
        choose = int(input("Choose function: \n1.Delta\n2.Fibonacci\n3.GCD(greatest common divisor)\n4.Exit\n"))
        if choose == 1:
            print(delta_function(float(input("a:")), float(input("b:")), float(input("c:"))))
        elif choose == 2:
            print(fibonacci(int(input("Enter which number you want to get:"))))
        elif choose == 3:
            print(gcd(int(input("First number:")), int(input("Second number:"))))
        elif choose == 4:
            flag = 0
        else:
            print("Wrong input")
