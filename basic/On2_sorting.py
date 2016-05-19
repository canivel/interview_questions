#insertionSort
# for small dataset O(n2)
def insertion_sort(a):
    for i in range(1, len(a)):
        for j in range(i-1, -1, -1):
            if (a[j] > a[j+1]):
                a[j], a[j+1] = a[j+1], a[j]
            else:
                break

    return a

#O(n2) faster than the first one
def insertion_sort2(a):
    for i in range(1, len(a)):
        j = i - 1
        while a[j] > a[j +1] and j >= 0:
            a[j], a[j+1] = a[j+1], a[j]
            j -= 1

    return a


#SelectionSort
# for small dataset O(n2)
def selection_sort(a):
    for i in range(0, len(a) - 1):
        minIndex = 1
        for j in range(i+1, len(a)):
            if a[j] < a[minIndex]:
                minIndex = j
        if minIndex != 1:
            a[i], a[minIndex] = a[minIndex], a[i]

    return a

#BubbleSort
# for small dataset O(n2)
def bubblesort(a):
    for i in range(0, len(a) - 1):
        for j in range(0, len(a) - 1 - i):
            if (a[j] > a[j + 1]):
                a[j], a[j + 1] = a[j + 1], a[j]
            else:
                break
    return a

import time
a = [2, 1, 4, 2, 1,43,21,21, 32,43,22, 33, 11, 8, 34, 2, 13]
x = 78

start = time.time()
print insertion_sort(a)
print ('Time elapse {}'.format((time.time() - start)*60))

start = time.time()
print insertion_sort2(a)
print ('Time elapse {}'.format((time.time() - start)*60))
