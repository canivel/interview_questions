__author__ = 'canivel'
'''
Given a string of numbers and operators, return all possible results from computing all the
different possible ways to group numbers and operators. The valid operators are +, - and *.

Example 1
Input: "2-1-1".

((2-1)-1) = 0
(2-(1-1)) = 2
Output: [0, 2]


Example 2
Input: "2*3-4*5"

(2*(3-(4*5))) = -34
((2*3)-(4*5)) = -14
((2*(3-4))*5) = -10
(2*((3-4)*5)) = -10
(((2*3)-4)*5) = 10
Output: [-34, -14, -10, -10, 10]
'''

class Solution(object):
    def diffWaysToCompute(self, input):
        if input.isdigit():
            return [int(input)]
        res = []
        for i in range(len(input)):
            if input[i] in "-+*":
                res1 = self.diffWaysToCompute(input[:i])
                res2 = self.diffWaysToCompute(input[i+1:])
                for j in res1:
                    for k in res2:
                        res.append(self.calculator(j, k, input[i]))
        return res

    def calculator(self, m, n, op):
        if op == "+":
            return m+n
        elif op == "-":
            return m-n
        else:
            return m*n


if __name__ == "__main__":
    s =  Solution()
    input = "2*3-4*5"
    print (s.diffWaysToCompute(input))