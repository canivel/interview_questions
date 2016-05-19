def reverse_string(s):
    return ' '.join(x for x in s.split(' ')[::-1])


s = " Testing reverse string"
print(reverse_string(s))