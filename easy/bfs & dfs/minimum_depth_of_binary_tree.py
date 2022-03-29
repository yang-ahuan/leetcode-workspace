# Pattern : BFS & DFS
#
# Init -- New two lists to record current and next level node.
# Step1 -- Iteratively scan children of each node.l
# Term -- When reaching leaf node, stop scanning.

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def minDepth(self, root: TreeNode) -> int:
        if not root: return 0
        current_level_node, next_level_node, ans = [root], [], 0
        while current_level_node:
            ans += 1
            for node in current_level_node:
                if node.right: next_level_node.append(node.right)
                if node.left: next_level_node.append(node.left)
                if not (node.right or node.left): return ans
            current_level_node, next_level_node = next_level_node, []

# Time : O(n)
# Space : O(n)