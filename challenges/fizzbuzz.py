def fizzbuzz(n):
    for i in range(1, n+1):
        if i % 3 == 0 and i % 5 == 0:
            print((f'{i} % 3 == 0', 'fizzbuzz'))
        elif i % 3 == 0:
            print((f'{i} % 3 == 0', 'fizz'))
        elif i % 5 == 0:
            print((f'{i} % 3 == 0', 'buzz'))
        else:
            print(i)

fizzbuzz(20)
