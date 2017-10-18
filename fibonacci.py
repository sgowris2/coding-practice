def fibonacci(n):

    if n <= 0:
        return 0

    if n <= 2:
        return 1

    a = 1
    b = 1

    print(a)
    print(b)

    for i in range(0, n - 2):
        c = a + b
        a = b
        b = c
        print(b)


def fibonacci_recursive(n, memos):

    if n <= 0:
        return 0

    if n <= 2:
        return 1

    memo = memos.get(n, None)
    if memo:
        print('printed from memos: ', memo)
        return memo

    return fibonacci_recursive(n-1, memos) + fibonacci_recursive(n-2, memos)


def print_fib_recursive(n):

    memos = {1: 1, 2: 1}

    for i in range(1, n+1):
        f = fibonacci_recursive(i, memos)
        memos[i] = f
        print(f)


if __name__ == '__main__':

    _n = 10
    print_fib_recursive(_n)
