__author__ = 'canivel'
'''
Given two binary trees, write a function to check if they are equal or not.

Two binary trees are considered equal if they are structurally identical and the nodes have the same value.
'''
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isSameTree(self, p, q):
        if p and q:
            if (p.val == q.val and self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)):
                return True
            else:
                return False

        else:
            return p == q


s = Solution()
p = [0]
q = [0]
print (s.isSameTree(p, q))