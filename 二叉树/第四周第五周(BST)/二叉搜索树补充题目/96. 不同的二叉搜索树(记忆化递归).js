/* 
超出时间限制
var numTrees = function (n) {
    if (n === 0 || n === 1) return 1;

    let sum = 0;

    for (let i = 1; i <= n; i++) {
        let leftRes = numTrees(i - 1);
        let rightRes = numTrees(n - i);
        sum += leftRes * rightRes;
    }

    return sum;
};
 */

/* 
? https://leetcode.cn/problems/unique-binary-search-trees/solutions/1319816/a-qiu-javadi-gui-jie-fa-by-emeraki-qi2d/
* 递归函数的定义是: 用数字 1...n 能构造的不同 BST 的数量。
* 递归基例
*    当 n = 0：空树也是一种合法的 BST → 返回 1。
*    当 n = 1：只有一个节点，唯一的一棵树 → 返回 1。
*
* 递归情况
* 遍历每个数 i 作为根：
*    左子树有 numTrees(i - 1) 种可能。
*    右子树有 numTrees(n - i) 种可能。
*    左右子树组合：leftRes * rightRes 种。
*    累加所有 i 的结果。
*/
var numTrees = function (n) {
    const map = new Map();
    map.set(0, 1);
    map.set(1, 1);
    function calculate(n) {
        if (map.has(n)) {
            return map.get(n);
        }

        let sum = 0;

        for (let i = 1; i <= n; i++) {
            let leftRes = calculate(i - 1);
            let rightRes = calculate(n - i);
            sum += leftRes * rightRes;
        }
        map.set(n, sum);

        return sum;
    }
    return calculate(n);
};
