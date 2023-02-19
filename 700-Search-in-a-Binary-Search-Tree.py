# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    """
    You are given the root of a binary search tree (BST) and an integer val.

    Find the node in the BST that the node's value equals val and return the subtree rooted with that node.
    If such a node does not exist, return null.
    """

    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        currentNode = root
        if not root:
            return None

        if val > currentNode.val:
            return self.searchBST(currentNode.right, val)
        elif val < currentNode.val:
            return self.searchBST(currentNode.left, val)
        else:
            return currentNode
