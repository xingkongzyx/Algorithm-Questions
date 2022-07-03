// ! 前序遍历
/* 
/ 要找「最后一行」的「最左边的值」。首先「最后一行」是通过深度最大来找的，「最左边的值」是通过前序遍历来完成的，『前序遍历』的执行顺序是访问当前节点，再递归访问它的左子树，最后递归访问右子树。从 root 开始，『前序遍历』的轨迹是一直向下走，所以当第一次到达〔深度最大〕的位置的时候，正是递归函数通过『前序遍历』第一次接触到「最后一行」的时候，又因为『前序遍历』是一直是遍历完当前节点继续递归遍历左子树的节点，所以到达「最后一行」最先接触的就是「最左边的值」

* 1. 确定递归函数的参数和返回值
* 参数必须要遍历的树的根节点，还有就是一个int型的变量用来记录最长深度。 这里就不需要返回值了，所以递归函数的返回类型为void。
* 
* 本题还需要类里的两个全局变量, maxLen 用来记录最大深度, maxLeftValue 记录最大深度最左节点的数值。
* 
* 2. 确定终止条件
* 当遇到叶子节点的时候，就需要统计一下最大的深度了，所以需要遇到叶子节点来更新最大深度。

? https://leetcode.cn/problems/find-bottom-left-tree-value/solution/bu-yong-quan-ju-bian-liang-di-gui-fan-hui-shi-yao-/
*/

var findBottomLeftValue = function (root) {
    let maxDepth = -1;
    let maxLeftValue;

    function traversal(node, currentDepth) {
        // * 2. 确定终止条件
        if (node.left === null && node.right === null) {
            //# 结合前面所讲的看，因为要「大于」才会更新，所以每一层只会更新一次，『前序遍历』会遍历到左边的节点，所以只会更新每层最左侧的节点，符合题目要求
            if (currentDepth > maxDepth) {
                maxDepth = currentDepth;
                maxLeftValue = node.val;
            }
            return;
        }

        if (node.left) {
            currentDepth++; // 有左侧节点，深度加一，说明还能继续递归
            traversal(node.left, currentDepth);
            currentDepth--; // 回溯，遍历完了左侧节点，深度要退回原来的value
        }

        if (node.right) {
            currentDepth++;
            traversal(node.right, currentDepth);
            currentDepth--;
        }
        return;
    }

    traversal(root, 0);
    return maxLeftValue;
};
