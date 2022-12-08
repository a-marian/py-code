# 872. Leaf-Similar Trees
def leafSimilar(self, root1, root2):
    def dfs(node):
        if node:
            if not node.left and not node.right:
                yield node.val
            yield from dfs(node.left)
            yield from dfs(node.right)

        return list(dfs(root1)) == list(dfs(root2))

# Time complexity: O(2T)
# Space complexity: O(2T)
# * T is the length of the given tree.
# Solved by DFS
# https://leetcode.com/problems/leaf-similar-trees/
