"""
1339. Maximum Product of Splitted Binary Tree
Given the root of a binary tree, split the binary tree into two subtrees by removing
one edge such that the product of the sums of the subtrees is maximized.
Return the maximum product of the sums of the two subtrees. Since the answer may be too large,
return it modulo 109 + 7.
Note that you need to maximize the answer before taking the mod and not after taking it.
Example:
    Input: root = [1,2,3,4,5,6]
    Output: 110
    Explanation: Remove the red edge and get 2 binary trees with sum 11 and 10.
    Their product is 110 (11*10)
"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:

    def maxProduct(self, root: Optional[TreeNode]) -> int:
        sum1 = 0
        total = 0

        def getTotalSum(node):
            nonlocal sum1
            if node is None:
                return 0
            curSum = node.val
            curSum += getTotalSum(node.left)
            curSum += getTotalSum(node.right)
            if total != 0:
                sum1 = curSum if abs(total // 2 - curSum) < abs(total // 2 - sum1) else sum1
            return curSum

        total = getTotalSum(root)
        # now find dividing point
        getTotalSum(root)
        return (sum1 * (total - sum1)) % (10 ** 9 + 7)


"""
 Time complexity: O(N), where N is the number of nodes in the tree.
 Space complexity: O(H), where H is the height of the tree.
https://leetcode.com/problems/maximum-product-of-splitted-binary-tree/
"""
