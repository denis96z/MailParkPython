import sys

def fizz_buzz():
    for i in range(1, 101):
        if i % 15 == 0:
            print('FizzBuzz')
        elif i % 3 == 0:
            print('Fizz')
        elif i % 5 == 0:
            print('Buzz')
        else:
            print(i)

def euler1():
    def f(n):
        p = 999 // n
        return n * (p * (p + 1)) // 2
    return f(3) + f(5) - f(15)

def euler2():
    first = 1
    second = 1
    sum = 0
    temp = 2
    while temp <= 4000000:
        sum += temp
        first = second + temp
        second = temp + first
        temp = first + second
    return sum

def euler4():
    def is_palindrome(n):
        s = str(n)
        return s == s[::-1]

    m = 0
    for i in range(999, 100, -1):
        for j in range(999, 100, -1):
            n = i * j
            if is_palindrome(n) and n > m:
                m = n
    return m

def main():
    f = input('Function name: ')

    try:
        eval('print(' + f + '())')
    except NameError:
        print('Function not found')

if __name__ == "__main__":
    main()