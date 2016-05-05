class Solution(object):
    def canPermutePalindrome(self, s):
        if not s:
            return False

        # This is extended slice syntax. It works by doing [begin:end:step] -
        # by leaving begin and end off and specifying a step of -1, it reverses a string.
        # print (s[::-1])
        # if s == s[::-1]:
        #     return True
        # else:
        #     return False

        dic = {}
        for item in s:
            #print(item)
            dic[item] = dic.get(item, 0) + 1

        # return sum(v % 2 for v in dic.values()) < 2
        count1 = 0
        print dic
        for val in dic.values():
            #print (val)
            if val % 2 == 1:
                count1 += 1
            if count1 > 1:
                return False
        return True

import collections

class Solution2(object):
    def canPermutePalindrome(self, s):
        #print(collections.Counter(s).values()) # count the number of letters
        return sum(v % 2 for v in collections.Counter(s).values()) < 2

st = 'aab'
st2 = 'carerac'
s =  Solution2()
print (s.canPermutePalindrome(st2))