/*
 * 递归函数 getDepth 的作用是: 计算以 node 为根节点的二叉树的最大深度, 并使用全局变量 result 记录
 * 递归函数 getDepth 的终止条件：遇到叶子节点时, 将当前这一分支的深度与目前的最大深度比较并更新。由于以叶子节点作为终止条件, 所以在递归过程中保证当前节点 node 不为空
 * 单层递归的逻辑:
 * ➀ 如果当前节点的左子树存在, 递归计算左子树的最大深度
 * ➁ 如果当前节点的右子树存在, 递归计算右子树的最大深度
 */
var maxDepth = function (root) {
    //* 如果根节点就是 Null, 说明深度是 0
    if (root === null) return 0;
    //* result 代表的是最大深度
    let result = 0;

    function getDepth(node, depth) {
        //* 终止条件, 如果左右节点都是空, 深度不可能再继续增加, 直接返回
        if (node.left === null && node.right === null) {
            //* 在到达叶子节点时检查depth. 因为传入的 depth 已经代表了在当前这一层的深度是多少(root节点默认为1), 看 depth 是否已经超过了其他叶子节点所在深度
            if (depth > result) result = depth;
            return;
        }

        if (node.left) {
            depth += 1;
            getDepth(node.left, depth);
            depth -= 1;
        }
        if (node.right) {
            depth += 1;
            getDepth(node.right, depth);
            depth -= 1;
        }
    }
    //* root节点的所在深度默认为1
    getDepth(root, 1);
    return result;
};

/* 
* 更加标准的前序遍历
* curDepth 并不是在统计“从根到叶子路径的总长度”，而是实时表示 “我当前正处于树的第几层”。
    # 进入节点时层数 +1
    # 离开节点时层数 -1
    # 所以任何时刻，curDepth 都是“调用栈的深度”，即当前遍历路径的层数。
* 而 maxDepth 就是遍历过程中遇到的 curDepth 最大值。

       A
      / \
     B   C
        /
       D

Step 1: 从根 A 开始
进入 A → curDepth = 1
👉 表示“我现在在第 1 层”

Step 2: 进入左子树 B
进入 B → curDepth = 2
👉 表示“我现在在第 2 层”
B 没孩子 → 返回时回溯：curDepth = 1
👉 我回到了 A 这一层

Step 3: 进入右子树 C
进入 C → curDepth = 2
👉 “我现在在第 2 层”
继续进入 D：curDepth = 3
👉 “我现在在第 3 层”
D 没孩子 → 回溯：curDepth = 2
👉 回到 C 这一层

Step 4: C 的右子树空 → 返回
C 的递归结束 → 回溯：curDepth = 1
👉 回到 A 这一层

Step 5: A 的左右子树都走完了
回溯：curDepth = 0
👉 “我离开了整棵树”
*/
var maxDepth = function (root) {
    let maxDepth = 0;
    let curDepth = 0;
    function DFS(node) {
        if (node === null) return;

        curDepth += 1;
        maxDepth = Math.max(curDepth, maxDepth);

        DFS(node.left);
        DFS(node.right);

        curDepth -= 1;
    }
    DFS(root);
    return maxDepth;
};
