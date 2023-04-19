# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deepestLeavesSum(self, root: Optional[TreeNode]) -> int:
        maxlevel = 0
        tsum  = 0

        def dfs(node=root, level=0):
            nonlocal maxlevel, tsum
            if not node: return
            dfs(node.left, level+1)
            dfs(node.right, level+1)
            if maxlevel < level:
                maxlevel = level
                tsum = 0
            if maxlevel == level:
                tsum += node.val
        dfs()
        return tsum