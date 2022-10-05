class TreeNode:
    '''
    Tree Node
    '''
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def __init__(self):
        self.max = 0
    def Diameter(self, root: TreeNode) -> int:
        if root is None: return 0
        def traverse(root):
            if root is None: return 0
            left = traverse(root.left)
            right = traverse(root.right)
            if left + right > self.max:
                self.max = left+right
            return max(left, right) + 1
        traverse(root)
        return self.max

if __name__ == '__main__':
    root = TreeNode(10)
    root.left = TreeNode(11)
    root.left.left = TreeNode(2)
    root.left.right = TreeNode(31)
    root.right = TreeNode(12)

    print(Solution().Diameter(root))