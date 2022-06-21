/* 
* 1. 确定递归函数的参数及返回值
* 要递归遍历，参数中少不了下一个遍历的节点
* 因为我们使用全局变量保存前一个节点的值，因此不需要返回值
* 
* 2. 确定递归函数终止条件
* 越过叶子节点时，终止递归
* 修改当前节点的值且更新全局变量的值后终止递归
* 
* 3.确定每次进入递归函数做什么
! 注意要右中左来遍历二叉树， 中节点的处理逻辑就是让cur的数值加上前一个节点的数值。
* 递归root的右节点，找到所有比当前节点值大的节点；
* 当递归到最右时，我们终止递归，开始累加这条路径上的所有节点值，即，当前节点值累加全局变量的值并更新全局变量的值为累加后的值
* 递归左节点；
* 终止当前递归
*/

var convertBST = function (root) {
    let prevNodeVal = null;
    let rnlTraverse = function (currentNode) {
        if (currentNode === null) return null;
        rnlTraverse(currentNode.right);

        if (prevNodeVal === null) prevNodeVal = currentNode.val;
        else {
            currentNode.val += prevNodeVal;
            prevNodeVal = currentNode.val;
        }
        rnlTraverse(currentNode.left);
    };
    rnlTraverse(root);
    return root;
};
