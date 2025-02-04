def factorial(n):
    res = 1
    for i in range(1, n + 1):
        res *= i
    return res

    
def is_power_of_5(n):
    while n. 1 and n % 5 == 0:
        n //= 5
    return n == 1


def nsd_finder(a, b):
    while b:
        a, b = b, a % b
    return a
