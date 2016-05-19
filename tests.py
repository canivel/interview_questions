def climbStairs(n):
    a, b = 1, 1
    for i in range(n):
        a, b = b, a + b
        print a
    return a

print climbStairs(10)
