# Given a string, we can "shift" each of its letter to its successive letter, for example: "abc" -> "bcd". We can keep "shifting" which forms the sequence:
#
# "abc" -> "bcd" -> ... -> "xyz"
# Given a list of strings which contains only lowercase alphabets, group all strings that belong to the same shifting sequence.
#
# For example, given: ["abc", "bcd", "acef", "xyz", "az", "ba", "a", "z"],
# Return:
#
# [
#   ["abc","bcd","xyz"],
#   ["az","ba"],
#   ["acef"],
#   ["a","z"]
# ]
# Note: For the return value, each inner list's elements must follow the lexicographic order.

import collections

class Solution(object):
    def groupStrings(self, strings):
        if len(strings) == 1:
            return [strings]
        if len(strings) == 0:
            return []
        final_list = []
        sizes = []
        strings.sort(key = len)
        last_size = 0
        for s in strings:
            if last_size != 0 and last_size != len(s):
                final_list.append(sizes)
                sizes = []
            sizes.append(s)
            last_size = len(s)

        if len(sizes) > 0:
            final_list.append(sizes)
        if len(final_list) > 0:
            final_list.sort()
        else:
            final_list.append(sizes)
        return final_list

        # i = 0
        # for s in strings:
        #     size = len(s)
        #     if size not in sizes:
        #         sizes.append(size)
        #         new_list.append(s)
        #
        # print sizes

    def groupStrings(self, strings):
        groups = collections.defaultdict(list)
        print groups
        for s in strings:
            groups[tuple((ord(c) - ord(s[0])) % 26 for c in s)] += s,
        return map(sorted, groups.values())



st = ["abc", "bcd", "acef", "xyz", "az", "ba", "a", "z"]
st = ["ab","ba"]
s =  Solution()
print (s.groupStrings(st))