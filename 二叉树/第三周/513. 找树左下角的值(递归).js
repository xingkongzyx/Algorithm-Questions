// ! 前序遍历
/* 
/ 要找最后一行最左边的值。最后一行是通过深度最大来找的，最左边的值是通过前序遍历，在第一次进入最后一行的时候第一个到的值就是最左边的值
* 1. 确定递归函数的参数和返回值
* 参数必须要遍历的树的根节点，还有就是一个int型的变量用来记录最长深度。 这里就不需要返回值了，所以递归函数的返回类型为void。
* 
* 本题还需要类里的两个全局变量, maxLen 用来记录最大深度, maxleftValue 记录最大深度最左节点的数值。
* 
* 2. 确定终止条件
* 当遇到叶子节点的时候，就需要统计一下最大的深度了，所以需要遇到叶子节点来更新最大深度。


*/

var findBottomLeftValue = function (root) {
    let maxDepth = -1;
    let maxLeftValue;

    function traversal(node, currentDepth) {
        // * 2. 确定终止条件
        //# 查找最左的时候 利用先序遍历，这样得到的第一个节点一定是最左边， 因为这一层深度不可能比他大。 如果要求最大深度中的最小值，就深度判断时候加上大于等于就好了。
        if (node.left === null && node.right === null) {
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
