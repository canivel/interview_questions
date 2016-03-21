__author__ = 'canivel'
import time
start = time.time()

#### 1 ####
a=0
b=1
for i in range(10):
    print (b)
    b = a+b
    a = b-a

#### 2 ####
# r=10
a, b = 0, 1
result = []
for i in range(r):
    result.append(b)
    a, b = b, a+b

#### 3 ####
def fib(n):
    fibValues = [0, 1]
    for i in range(2, n + 1):
        fibValues.append(fibValues[i - 1] + fibValues[i - 2])
    return fibValues[n]

print('{} Runtime: {}'.format(fib(10), time.time() - start))

#### 4 ####
def fibonacci(n):
    """Fibonacci numbers generator, first n"""
    a, b, counter = 0, 1, 0
    while True:
        if (counter > n):
            return
        yield a
        a, b = b, a + b
        counter += 1

f = fibonacci(5)
for x in f:
    print (x)
