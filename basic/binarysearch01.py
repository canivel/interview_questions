import time

def search_1(a, x):
    if x in a:
        return a.index(x)

#(On)
def search_2(a, x):
    for i in range(len(a) -1):
        if a[i] == x:
            return i

#(Ologn)
def search_3(a, x):
    low = 0
    high = len(a) - 1
    while low <= high:
        mid = (low+high)/2

        if a[mid] == x:
            return mid
        elif a[mid] < x:
            low = mid + 1
        else: #a[mid] > x:
            high = mid - 1
    return -1


#(Ologn)
def search_3(a, x):
    low = 0
    high = len(a) - 1
    while low <= high:
        mid = (low+high)/2

        if a[mid] == x:
            return mid
        elif a[mid] < x:
            low = mid + 1
        else: #a[mid] > x:
            high = mid - 1
    return -1

#(Ologn) RECURSIVE
def search_4(a, x, low, high):

    mid = (low + high) / 2
    if a[mid] == x:
        return mid
    elif a[mid] < x:
        low = mid + 1
        return search_4(a, x, low, high)
    else:  # a[mid] > x:
        high = mid - 1
        return search_4(a, x, low, high)
    return -1

a = [1, 2, 3, 4, 5, 7, 9, 10, 22, 34, 56, 78, 90, 99]
x = 78

start = time.time()
print search_1(a, x)
print ('Time elapse {}'.format((time.time() - start)*60))

start = time.time()
print search_2(a, x)
print ('Time elapse {}'.format((time.time() - start)*60))

start = time.time()
print search_3(a, x)
print ('Time elapse {}'.format((time.time() - start)*60))

start = time.time()
low = 0
high = len(a) - 1
print search_4(a, x, low, high)
print ('Time elapse {}'.format((time.time() - start)*60))