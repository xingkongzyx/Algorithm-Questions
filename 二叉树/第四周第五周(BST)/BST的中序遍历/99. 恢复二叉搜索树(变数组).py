class Solution:
    def recoverTree(self, root: TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        # 中序遍历二叉树，将遍历结果保存到列表中
        node = []
        def dfs(root):
            if root == None:
                return
            dfs(root.left)
            node.append(root)
            dfs(root.right)
        dfs(root)

        x,y = None,None
        pre = node[0]
        # 循环遍历，找到错误交换的x,y
        for i in range(1,len(node)):
            if pre.val > node[i].val:
                y = node[i]
                # 记录第一个出现的交换值
                if not x:
                    x = pre
            pre = node[i]
        
        # 将找到的x和y进行交换
        if x and y:
            x.val,y.val = y.val,x.val
