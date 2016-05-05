# Given a string containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.
# The brackets must close in the correct order, "()" and "()[]{}" are all valid but "(]" and "([)]" are not.

class Solution2(object):
    def isValid(self, s):
        n = len(s)
        if n == 0:
            return True

        if n % 2 != 0:
            return False

        #remove from the center and iterate again
        while '()' in s or '{}' in s or '[]' in s:
            s = s.replace('{}', '').replace('()', '').replace('[]', '')

        if s == '':
            return True
        else:
            return False


class Solution:
    # @return a boolean
    def isValid(self, s):
        stack = []
        dict = {"]":"[", "}":"{", ")":"("}
        for char in s:
            print char
            if char in dict.values():
                stack.append(char)
                print ('Stack',stack)
            elif char in dict.keys():
                if stack == [] or dict[char] != stack.pop():
                    return False
            else:
                return False
        return stack == []

l = '[][({[]})]'
s = Solution()
print s.isValid(l)