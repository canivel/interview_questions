#Recursive / Divide and Conquer / Very eficiente for large datasets
#O(nlogn)

def mergeSort(alist):
    print("Splitting ",alist)
    if len(alist)>1:
        mid = len(alist)//2
        lefthalf = alist[:mid]
        righthalf = alist[mid:]

        mergeSort(lefthalf)
        mergeSort(righthalf)

        i=0
        j=0
        k=0
        while i < len(lefthalf) and j < len(righthalf):
            if lefthalf[i] < righthalf[j]:
                alist[k]=lefthalf[i]
                i=i+1
            else:
                alist[k]=righthalf[j]
                j=j+1
            k=k+1

        while i < len(lefthalf):
            alist[k]=lefthalf[i]
            i=i+1
            k=k+1

        while j < len(righthalf):
            alist[k]=righthalf[j]
            j=j+1
            k=k+1
    print("Merging ",alist)

import time
a = [2, 1, 4, 2, 1,43,21,21, 32,43,22, 33, 11, 8, 34, 2, 13]
x = 78

start = time.time()
mergeSort(a)
print a
print ('Time elapse {}'.format((time.time() - start)*60))
