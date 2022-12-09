"""
1026. Maximum Difference Between Node and Ancestor
"""
class Solution(object):

    def __init__(self):
        self.maxDiff = 0

    def maxAncestorDiff(self, root, maxv = 0, minv = 5001):
        if root == None:
            return 0
        maxv = max(maxv, root.val)
        minv = min(minv, root.val)

        self.maxDiff = max(self.maxDiff, abs(maxv - minv))
        self.maxAncestorDiff(root.left, maxv, minv)
        self.maxAncestorDiff(root.val, maxv, minv)
        return self.maxDiff


"""
  Time complexity: O(N), where N is the number of nodes in the tree.
  This is because we visit each node in the tree exactly once and do a constant amount
  of work for each node.
  Space complexity: O(H), where H is the height of the tree.
  This is because the maximum number of nodes on the call stack will be equal to the height of the tree,
  as we need to store one function call for each level of the tree.
  https://leetcode.com/problems/maximum-difference-between-node-and-ancestor/
"""
class TreeNode(object):
    def __init__(self, x):
         self.val = x
         self.left = None
         self.right = None

