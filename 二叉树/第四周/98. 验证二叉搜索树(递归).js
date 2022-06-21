// O(n) time, O(d) space d is the longest branch of the tree
/*
 * 1. 确定递归函数的参数和返回值
 *  递归函数的参数传入的就是根节点和当前限定这个节点的value的最大值最小值，返回的boolean value
 ! 注意递归函数要有bool类型的返回值，在寻找某一条边（或者一个节点）的时候，递归函数会有bool类型的返回值。本题是同样的道理，我们在寻找一个不符合条件的节点，如果没有找到这个节点就遍历了整个树，如果找到不符合的节点了，立刻返回。

 * 2. 确定终止条件
 *  如果root为空，就说明我们已经遍历完成了这条subtree，并且这条子树符合要求，返回true。
 *
 * 3. 确定单层递归的逻辑
 > 前序遍历，
 * 首先判断当前节点是否满足(minVal, maxVal)的区间.然后根据左/右节点传入对应的maxVal以及minVal，一旦发现某一子树不符合要求，就返回false。
 *
 */
var isValidBST = function (root) {
    let minVal = -Infinity;
    let maxVal = Infinity;

    let res = helper(root, minVal, maxVal);
    return res;
};

function helper(root, minVal, maxVal) {
    /* 
    / 思路：引入上下边界
 
    / 对于树的每个节点 val ，设其上下边界 minVal , maxVal. 
    / 判断根结点时，须满足 minVal < val < maxVal ，否则返回 false
    / 判断左节点时，仅 上界 变化 ( 新上界为 maxVal 与 root.val 较小值。又因 root.val 必小于 maxVal，故新上界为 root.val )
    / 判断右节点时，仅 下界 变化 ( 同理，新下界为 root.val )    
    */
    if (root === null) return true;

    if (root.val > minVal && root.val < maxVal) {
    } else {
        return false;
    }

    let isLeftValid = helper(root.left, minVal, root.val);
    if (isLeftValid === false) return false;

    let isRightValid = helper(root.right, root.val, maxVal);
    if (isRightValid === false) return false;

    return true;
}
