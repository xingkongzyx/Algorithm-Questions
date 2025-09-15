/* 
题意与括号规则
用先序遍历(root → left → right)把结点的 val 串起来，并按下面的括号规则拼接子树: 
 - 叶子结点: 只输出数值(不加括号)。
 - 只有左子树: root(left)(右子树省略)。
 - 只有右子树: 必须保留空的左括号占位 → root()(right)。
 - 同时有左右子树: root(left)(right)。

* 递归函数 DFS 的作用是: 构建以 node 为根节点的二叉树的字符串，并返回该字符串
* 单层递归的逻辑: 对应 approach 部分
 
* 前序遍历没什么好说的, 难点在于加括号时区分左右子树。
* 左子树加括号的条件是: 1.左子树不空, 2.左子树为空, 但右子树不空；
* 右子树加括号的条件是: 右子树不空

* Approach:
* Here we recursively traverse the nodes in binary tree and check:
* • If there exists a left or right child, we add parentheses for left child and put inside whatever we find on left subtree.
* • If there exists only right child, we add parentheses for right child and add inside whatever we find in right subtree.
* • The difference that can observed is that for left part we create parentheses even when there is no left child, but for right part we create parentheses only when there is right child.
/ Time Complexity: O(N), where N is the number of nodes in the Binary Tree.
/ Space Complexity: O(H), where H is the height of the Binary Tree (Recursion stack space)
? 思路: https://leetcode.com/problems/construct-string-from-binary-tree/discuss/2542357/C%2B%2B-or-Recursive-Pre-Order-Traversal-Approach
*/
var tree2str = function (root) {
    const res = [];

    const DFS = (curNode) => {
        if (!curNode) return;

        // 处理当前节点
        res.push(String(curNode.val));

        // 如果「左子树」或者「右子树」有任何一个存在, 都需要处理左子树(对应示例2)
        if (curNode.left || curNode.right) {
            res.push("(");
            DFS(curNode.left); // 若为 null，不会往 res 追加任何内容 → 得到 "()"
            res.push(")");
        }

        // 如果「右子树」存在, 则需要处理右子树。如果不存在, 则不需要处理
        if (curNode.right) {
            res.push("(");
            DFS(curNode.right);
            res.push(")");
        }
    };

    DFS(root);
    return res.join("");
};

/* 
! 下面是一段错误的版本，如果把“给每个孩子各配一对括号”的结构，误实现成了“给整段孩子共同配一对括号”
这段代码的核心问题是括号放错了位置，以及在“只有右孩子没有左孩子”时没有输出一对空括号 ()。
题目要求的格式是（先序遍历）：
    - 打印当前节点值；
    - 如果有左子树或有右子树，必须打印一对括号包住左子树字符串（左子树为空也要打空括号，以区分“没有左子树但有右子树”的情况）；
    - 如果有右子树，再打印一对括号包住右子树字符串。

而你现在是在进入孩子递归前只推入了一个 "("，等左右都处理完才推入一个 ")"，相当于用一对括号把“左右子树的合体”一起包了，这和题目的“每个孩子各自一对括号”的语法不一致 
*/
var tree2strWrong = function (root) {
    const path = [];
    function DFS(node) {
        if (node === null) return;

        path.push(node.val);

        path.push("(");

        if (node.left || node.right) {
            DFS(node.left);
        }

        if (node.right) {
            DFS(node.right);
        }
        path.push(")");
    }
    DFS(root);
    return path.join("");
};
