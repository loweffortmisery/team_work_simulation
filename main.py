from random import randint
from utils import factorial
from utils import nsd_finder
from utils import is_power_of_5

if __name__ == '__main__':
    n = int(input("Введіть число для підрахунку факторіалу: "))
    print(f"factorial of {n} = {factorial(n)}")


if __name__ == "__main__":
    a, b = [int(el) for el in input("Введіть числа для підрахунку НСД: ").split()]
    print(f"НСД({a},{b}) = {nsd_finder(a, b)}")

if __name__ == '__main__':
    n = int(input("Ведіть число для перевірки на те чи є воно степенем 5-и: "))
    print(f"n is power of 5? = {is_power_of_5(n)}")
