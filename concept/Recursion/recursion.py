# factorial
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

print(factorial(3))

# palindrome 
def palindrome(string):
    if len(string) <= 1:
        return True
    if string[0] == string[-1]:
        return palindrome(string[1:-1])
    else:
        return False

def totalSum_list(data):
    if len(data) <= 1:
        return data[0]
    return data[0] + totalSum_list(data[1:])

# fibonacci
def fibonacci(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else: 
        return fibonacci(n-1)+fibonacci(n-2)


def fibonacci2(n):
    if n < 2:
        return n
    x, y = 0, 1
    for i in range(n): 
        x, y = y, x+y 
    return x
