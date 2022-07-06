//> 543, 687, 124 为同一类型
/* 
? 以root为路径起始点的最长路径，不同情况的图解: https://leetcode.cn/problems/longest-univalue-path/solution/zui-chang-tong-zhi-lu-jing-di-gui-bian-li-by-zui-w/ 


* 设计一个递归函数，返回以该节点为根节点，向下走的最长同值路径
* 知道这个值以后
* 以某个节点为根节点的最长同值路径就是，
* 如果该节点的值等于其左子树的值，则最长同值路径要加上左子树的最长同值路径，如果不等，左子树的路径为0
* 如果该节点的值等于其右子树的值，则最长同值路径要加上右子树的最长同值路径，如果不等，右子树的路径为0
* 
* 我们用一个全局变量记录这个最大值，不断更新
? 来自于: https://leetcode.cn/problems/longest-univalue-path/solution/jian-dan-yi-dong-ban-by-a380922457-7/
/ 时间复杂度: 遍历一次所有节点，时间复杂度为 O(n).
/ 空间复杂度: 递归需要栈辅助空间，只定义了几个变量，空间复杂度为 O(n).
 */
var longestUnivaluePath = function (root) {
    //*  记录全局的 Longest Univalue Path, 初始为0
    let result = 0;

    /// 函数意义是: 以「node节点」为起点, 向下走的最长同值路径, 这里返回的不包含:『左子树-root-右子树』他们三个同值的情况
    function helper(node) {
        if (node === null) return 0;

        //* 以「node 的左子节点」为起点 的最长同值路径长度
        let leftPath = helper(node.left);

        //* 以「node 的右子节点」为起点 的最长同值路径长度
        let rightPath = helper(node.right);

        //* leftPathAfterRootCheck 表示以「node节点」为起点, 向左节点延伸 的最长同值路径长度
        let leftPathAfterRootCheck = 0;

        //* 如果「node节点的左子节点」存在且它的值与「node节点」的值不相同, 无论上面计算的 LeftPath 是多少, 结合函数的整体功能 "以「node节点」为起点（表示向下发展）的最长同值路径长度", 因为不再满足『同值』的条件, 所以包含「node节点」以后它的最长同值路径长度变为 0
        if (node.left !== null && node.left.val === node.val)
            leftPathAfterRootCheck = leftPath + 1;
        else leftPathAfterRootCheck = 0;

        //* rightPathAfterRootCheck 表示以 「node节点」 为起点, 向右节点延伸 的最长同值路径长度
        let rightPathAfterRootCheck = 0;
        //* 如果「node节点的右子节点」存在且它的值与「node节点」的值不相同, 无论上面计算的 rightPath 是多少, 结合函数的整体功能 "以「node节点」为起点（表示向下发展）的最长同值路径长度", 因为不再满足『同值』的条件, 所以包含「node节点」以后它的最长同值路径长度变为 0
        if (node.right !== null && node.right.val === node.val)
            rightPathAfterRootCheck = rightPath + 1;
        else rightPathAfterRootCheck = 0;

        //* leftPathAfterRootCheck 是与「当前node节点」值相同的左子树的路径长度, rightPathAfterRootCheck 是与「当前node节点」值相同的右子树路径长度, 他们都有可能是0. 他们的和【leftPathAfterRootCheck + rightPathAfterRootCheck】 是与「当前node节点」值相同, 左右连接在一起的路径的长度. result 是题目要求的答案, 如果有更长的同值路径, 要记录下来
        result = Math.max(
            result,
            leftPathAfterRootCheck + rightPathAfterRootCheck
        );

        //* leftPathAfterRootCheck 和 rightPathAfterRootCheck 中的最大值表示以「node节点」为起点（表示向下发展）的最长同值路径长度. 与函数定义吻合
        return Math.max(
            leftPathAfterRootCheck,
            rightPathAfterRootCheck
        );
    }

    helper(root);
    return result;
};
