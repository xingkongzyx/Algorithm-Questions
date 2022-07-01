/* 
* 我们对整棵二叉树进行一次遍历。设根节点的值为「rootVal」，我们只需要通过遍历，在左右子树中找出严格大于「rootVal」的「最小节点的值」，即为「所有节点中的第二小的值」。
//? 前序遍历解法: 1. https://leetcode.cn/problems/second-minimum-node-in-a-binary-tree/solution/gong-shui-san-xie-yi-ti-shuang-jie-shu-d-eupu/ 
? 2. 官方解法
/时间复杂度：O(n)，其中 nn是二叉树中的节点个数。我们最多需要对整棵二叉树进行一次遍历。
/空间复杂度：O(n)。我们使用深度优先搜索的方法进行遍历，需要使用的栈空间为 O(n)。
? 
*/
/// 递归函数的含义是: 从 root 为根的树进行搜索，找到值比「初始根节点 rootVal」大的最小数。后使用全局变量 ans 存储答案。
var findSecondMinimumValue = function (root) {
    let ans = -1;

    function dfs(node, rootVal) {
        if (node === null) return;

        //# 中
        //* 如果当前节点的值大于等于 ans 并且此时的 ans 不是 -1，那么说明「以当前节点为根的子树」中所有节点的值都大于等于 ans, 肯定不可能存在我们想找的值. 直接结束当前递归, 无需对该子树进行遍历.
        if (ans !== -1 && node.val >= ans) return;
        //* 如果遇到了一个数字比 rootVal 大, 如果此时 ans 还为 -1, 说明这是第一次遇到比 rootVal 大的值, 直接更新 ans. 否则与 ans 已有的值进行比较选取较小的(因为求的就是第二小的值)
        if (node.val > rootVal) {
            if (ans === -1) ans = node.val;
            else ans = Math.min(ans, node.val);
        }

        //# 左
        dfs(node.left, rootVal);
        //# 右
        dfs(node.right, rootVal);
    }

    dfs(root, root.val);
    return ans;
};
