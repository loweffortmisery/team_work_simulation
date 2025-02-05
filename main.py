from random import randint
from utils import factorial
from utils import nsd_finder
from utils import is_power_of_5

if __name__ == '__main__':
    n = randint(1, 10)
    print(f"factorial of {n} = {factorial(n)}")


if __name__ == "__main__":
    a, b = [for int(el) in input().split()]
    print(f"НСД({a},{b}) = {nsd_finder(a, b)}")

if __name__ == '__main__':
    n = int(input())
    print(f"n is power of 5? = {is_power_of_5(n)}")
