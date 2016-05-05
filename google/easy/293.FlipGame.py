class Solution(object):
    def generatePossibleNextMoves(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        res = []

        # If we've got less than two items, there's no solution
        if len(s) < 2:
            return res

        # Look at each pair of twos in the string
        # If they are "++" flip them and add that to the result
        for i in range(len(s) - 2):
            if s[i] + s[i + 1] == "++":
                res.append(s[:i] + "--" + s[i + 2:])

        # Better to check the last ones here instead of making the for-loop
        #  do extra work each iteration
        if s[-1] + s[-2] == "++":
            if len(s) == 2:
                res.append("--")
            else:
                res.append(s[:-2] + "--")

        return res

        #return [s[:i] + "--" + s[i + 2:] for i in range(len(s) - 1) if s[i:i + 2] == '++']
