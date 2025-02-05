from random import randint
from utils import factorial
from utils import nsd_finder

if __name__ == "__main__":
    a, b = [for int(el) in input().split()]
    print(f"НСД({a},{b}) = {nsd_finder(a, b)}")

if __name__ == '__main__':
    n = randint(1, 10)
    print(f"factorial of {n} = {factorial(n)}")
