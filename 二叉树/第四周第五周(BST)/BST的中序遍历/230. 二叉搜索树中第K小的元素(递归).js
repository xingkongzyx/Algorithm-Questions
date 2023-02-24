/* 
/ 时间复杂度：O(H+k), 其中 H 为树的高度, 因为需要递归找到最小的节点再开始数 k 个节点；
/ 空间复杂度：O(H), 因为递归用了系统栈, 而栈的深度最多只有树的高度。

? https://leetcode.cn/problems/kth-smallest-element-in-a-bst/solutions/1051273/fu-xue-ming-zhu-er-cha-shu-san-chong-bia-yn34/

*/
var kthSmallest = function (root, k) {
    //* 用一个全局变量保存当前访问到第几个节点。
    let count = k;
    //* 用一个全局变量保存最终的结果；
    let result = null;
    function inOrderDFS(node) {
        if (node === null) return;
        inOrderDFS(node.left);
        count -= 1;
        //* 当 count 等于 0, 说明此时遍历到了第k个节点, 直接返回, 这也是时间复杂度中 k 的来源
        if (count == 0) {
            result = node.val;
            return;
        }
        inOrderDFS(node.right);
    }
    inOrderDFS(root);
    return result;
};
