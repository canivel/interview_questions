# Given a list of N numbers, use a single list comprehension to produce a new list that only contains those values that are:
# (a) even numbers, and
# (b) from elements in the original list that had even indices
#
# For example, if list[2] contains a value that is even, that value should be included in the new list, since it is also
# at an even index (i.e., 2) in the original list. However, if list[3] contains an even number, that number should not be
# included in the new list since it is at an odd index (i.e., 3) in the original list.


list_n = [x for x in range(20)]

print(list_n[::2])

a =[x for x in list_n if x % 2 != 0]

print (a)

# b = [x for x in list_n if]