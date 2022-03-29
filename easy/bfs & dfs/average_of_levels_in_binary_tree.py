# Pattern : BFS(navie approach : not using queue)
#
# Init -- New two lists to record current and next level value.
# Step1 -- Iteratively scan children of each node and calculate average in current level
# Term -- Stop when any node in current level doesn't have children, in other words, it's reaching leaf node.

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def averageOfLevels(self, root: TreeNode) -> list:
        curr_level_node, next_level_node, ans  = [root], [], []
        while curr_level_node:
            curr_level_total = 0
            for node in curr_level_node:
                curr_level_total += node.val
                if node.left: next_level_node.append(node.left)
                if node.right: next_level_node.append(node.right)                
            ans.append(curr_level_total/len(curr_level_node))
            curr_level_node, next_level_node = next_level_node, []
        return ans

# Time : O(n)
# Space : O(n)   