"""
A path in a binary tree is a sequence of nodes where each pair of adjacent nodes in the sequence
has an edge connecting them. A node can only appear in the sequence at most once.
Note that the path does not need to pass through the root.
The path sum of a path is the sum of the node's values in the path.
Given the root of a binary tree, return the maximum path sum of any non-empty path.
Example:
    Input: root = [1,2,3]
    Output: 6
    Explanation: The optimal path is 2 -> 1 -> 3 with a path sum of 2 + 1 + 3 = 6.
"""
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    maxSum = -sys.maxsize - 1

    def max_path_sum(self, root: Optional[TreeNode]) -> int:
        def get_max_path_sum(node):
            if node is None:
                return 0

            left_sum = max(get_max_path_sum(node.left), 0)
            right_sum = max(get_max_path_sum(node.right), 0)
            self.maxSum = max(self.maxSum, node.val + left_sum + right_sum)

            return node.val + max(left_sum, right_sum)

        get_max_path_sum(root)
        return self.maxSum
"""
 Time complexity: O(N), where N is the number of nodes in the tree.
 Space complexity: O(H), where H is the height of the tree.
 We don't use any auxiliary data structure, but the recursive call stack can go 
 as deep as the tree's height. In the worst case, the tree is a linked list, 
 so the height is nnn. Therefore, the space complexity is O(n).
https://leetcode.com/problems/binary-tree-maximum-path-sum/
"""
