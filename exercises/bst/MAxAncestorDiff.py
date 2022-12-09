"""
1026. Maximum Difference Between Node and Ancestor
"""
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):

    def maxAncestorDiff(self, root: TreeNode) -> int:
        if not root:
            return 0

        def helper(node, cur_max, cur_min):
            # if encounter leaves, return the max-min along the path
            if not node:
                return cur_max - cur_min
            # else, update max and min
            # and return the max of left and right subtrees
            cur_max = max(cur_max, node.val)
            cur_min = min(cur_min, node.val)
            left = helper(node.left, cur_max, cur_min)
            right = helper(node.right, cur_max, cur_min)
            return max(left, right)

        return helper(root, root.val, root.val)


"""
  Time complexity: O(N), where N is the number of nodes in the tree.
  This is because we visit each node in the tree exactly once and do a constant amount
  of work for each node.
  Space complexity: O(H), where H is the height of the tree.
  This is because the maximum number of nodes on the call stack will be equal to the height of the tree,
  as we need to store one function call for each level of the tree.
  https://leetcode.com/problems/maximum-difference-between-node-and-ancestor/
"""


