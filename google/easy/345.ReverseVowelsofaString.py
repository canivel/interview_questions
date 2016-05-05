class Solution(object):
    def reverseVowels(self, s):
        s = list(s)
        VOWEL_LIST = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
        vowels = [c for c in s if c in VOWEL_LIST]
        print(vowels)
        vowels.reverse()
        print vowels
        vowel_index = 0
        for index, _ in enumerate(s):
            if s[index] in VOWEL_LIST:
                s[index] = vowels[vowel_index]
                vowel_index += 1
        return ''.join(s)


st = 'hello'
st2 = 'leetcode'
s =  Solution()
print (s.reverseVowels(st))