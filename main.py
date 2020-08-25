# -*- coding; utf-8 -*-

import calculation as cal

a = 3
b = 4

def main():
    print("안녕하세요 ,main 입니다.")
    print("a + b = ", cal.subtract(a,b))
    print("a - b =", cal.plus(a, b))
    print("a * b =", cal.multiple(a, b))

if __name__ == "__main__":
    main()

