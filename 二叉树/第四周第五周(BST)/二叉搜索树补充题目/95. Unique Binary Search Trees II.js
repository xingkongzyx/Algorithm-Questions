/* 
* 关于TreeNode root = new TreeNode(i)的放置的位置问题
? https://leetcode.cn/problems/unique-binary-search-trees-ii/solutions/331067/cong-gou-jian-dan-ke-shu-dao-gou-jian-suo-you-shu-/
? https://leetcode.cn/problems/unique-binary-search-trees-ii/solutions/47860/di-gui-zhu-xing-jie-shi-python3-by-zhu_shi_fu/
*/

var generateTrees = function (n) {
    /*
     * 递归函数的定义: 返回一个数组, 里面装着 "所有可能的二叉搜索树（BST）的根节点", 这些 BST 恰好使用了区间 [start..end] 的所有数字各一次, 并满足 BST 的大小关系. 也就是说, generateTrees(n) 就是调用 generteTreeList(1, n), 把 1..n 的所有唯一结构的 BST 都造出来.
     */
    function generateTreeList(start, end) {
        // * 这表示“空树也是一种合法选择”. 之所以返回 [null] 而不是 [], 是为了后面做左右子树的笛卡尔积组合时, 即便某一侧没有节点, 也能用 null 当作一个候选, 让“只有一边子树/两边都空”的情况被正确枚举出来. 如果这里返回空数组, 后面的嵌套循环就完全不会进入, 反而丢失了“单侧为空”的组合.
        // ! 这是让 "空子树" 参与组合的关键, 否则当某边为空时会丢解。
        if (start > end) {
            return [null];
        }

        const rootNodesList = [];

        for (let i = start; i <= end; i++) {
            let leftTreeRootList = generateTreeList(start, i - 1);
            let rightTreeRootList = generateTreeList(i + 1, end);
            for (let leftNode of leftTreeRootList) {
                for (let rightNode of rightTreeRootList) {
                    // 对于固定的根 i, 把“所有可能的左子树 × 所有可能的右子树”逐一配对, 每个配对都构成一种不同结构的 BST。把它们的根 curRoot 收集起来即可。
                    let curRoot = new TreeNode(i);
                    curRoot.left = leftNode;
                    curRoot.right = rightNode;

                    rootNodesList.push(curRoot);
                }
            }
        }

        return rootNodesList;
    }
    return generateTreeList(1, n);
};
