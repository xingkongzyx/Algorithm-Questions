/* 
* 如图所示, 题目所说的二叉树中的最大路径的计算来源可以分为以下四种：
* ➀ 我自己就是一条路径
* ➁ 某个结点及其左子树组成路径的和
* ➂ 某个结点及其右子树组成路径的和
* ➃ 以自己为桥梁, 跟左、右子树合并成一条路径

* 主要思路是采用递归后序遍历。遍历到某个结点时, 先获得该结点左右子树中的最大路径, 然后将左右子树中的最大路径与该结点连接形成以上四种类型的路径, 更新全局的最大路径和, 最后将1、2、3类型路径中最大的路径和返回给上一级结点。
? 图片: https://leetcode.cn/problems/binary-tree-maximum-path-sum/solution/li-jie-lu-jing-gai-nian-jian-dan-si-lu-jie-ti-fu-t/
? 分析来源? https://leetcode.cn/problems/binary-tree-maximum-path-sum/solution/javadi-gui-zi-ding-xiang-xia-bang-zhu-ji-8bmv/

? 英文: https://leetcode.com/problems/binary-tree-maximum-path-sum/solutions/603423/python-recursion-stack-thinking-process-diagram/?orderBy=most_votes
/ time and space complexity are all O(n) since all the node in the tree might be the top node of the path (same as parameter 'root' of maxPathSum), that means the recusion function will be called for N times.
 */

var maxPathSum = function (root) {
    let maxPath = -Infinity;

    /// 函数的作用是: 返回当前子树能向父节点 "提供" 的最大路径和。即, 一条从父节点延伸下来的路径, 能在当前子树中捞取的最大收益。分三种情况：➀➁➂
    function helper(node) {
        if (node === null) return 0;
        //* 首先, 使用 helper(node.left) 用来计算以「node的左子节点」为起点, 向下走所能得到的最大路径和。然后加上当前节点的值从而计算「 ➁ 某个结点及其左子树组成路径的和」
        let leftPath = helper(node.left) + node.val;
        //* 首先, 使用 helper(node.right) 用来计算以「node的右子节点」为起点, 向下走所能得到的最大路径和。然后加上当前节点的值从而计算「 ➂ 某个结点及其右子树组成路径的和」
        let rightPath = helper(node.right) + node.val;
        //* 计算「➃ 以自己为桥梁, 跟左、右子树合并成一条路径」
        let pathThroughRoot = leftPath + rightPath - node.val;
        //* 将以「node节点」为根节点的树最大路径的四种计算来源进行比较, 从而更新题目所求的『二叉树中的最大路径和 maxPath』
        maxPath = Math.max(
            maxPath,
            node.val,
            leftPath,
            
            pathThrougrightPath,hRoot
        );

        return Math.max(node.val, leftPath, rightPath);
    }
    helper(root);
    return maxPath;
};
