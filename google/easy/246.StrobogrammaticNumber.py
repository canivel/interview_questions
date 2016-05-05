class Solution(object):
    def isStrobogrammatic(self, num):
        maps = {("0", "0"), ("1", "1"), ("6", "9"), ("8", "8"), ("9", "6")}

        i, j = 0, len(num) - 1
        while i <= j:
            if (num[i], num[j]) not in maps:
                return False
            i += 1
            j -= 1
        return True



st = 69
st2 = 818
st3 = 1
s =  Solution()
print (s.isStrobogrammatic(st3))