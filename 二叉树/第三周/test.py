from tkinter.messagebox import NO


class Solution(object):
    def mergeTrees(self, root1, root2):
        """
        :type root1: TreeNode
        :type root2: TreeNode
        :rtype: TreeNode
        """
        if(root1 != None and root2 == None):
            return root1
        elif(root1 == None and root2 != None):
            return root2
        elif(root1 == None and root2 == None):
            return None

        newVal = root1.val + root2.val
        newNode = TreeNode(newVal)
        newNode.left = self.mergeTrees(root1.left, root2.left)
        newNode.right = self.mergeTrees(root1.right, root2.right)
        return newNode
