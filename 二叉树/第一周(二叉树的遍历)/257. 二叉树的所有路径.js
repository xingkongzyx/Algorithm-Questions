// ! 前序遍历(中，左，右)，这样才方便让父节点指向孩子节点，找到对应的路径。
// ! 涉及到回溯，因为我们要把路径(currentPath)记录下来,需要回溯来回退一个路径,再进入另一个路径。

/* 
* 1. 递归函数函数参数以及返回值:
* 要传入根节点，记录每一条路径的currentPath，和存放结果集的totalPaths，这里递归不需要返回值
* 
* 2. 确定递归终止条件:
* 当 cur不为空，其左右孩子都为空的时候，就找到叶子节点。找到叶子节点意味着这条路径完成, 需要进行结束的处理逻辑(把路径放进totalPaths里).
* 
* 再来看一下终止处理的逻辑。这里使用array 结构的currentPath转为string格式，在把这个string 放进 totalPaths里。
? 那么为什么使用了 array 结构来记录路径呢？ 因为在下面处理单层递归逻辑的时候，要做回溯，使用array方便来做回溯。

* 3. 确定单层递归逻辑
* 因为是前序遍历，需要先处理中间节点，中间节点就是我们要记录路径上的节点，先放进currentPath中。然后是递归和回溯的过程. 要先判断左右节点是否为null, 如果不是则分别对其递归获取他们的路径。递归完，还要做回溯，因为 currentPath 不能一直加入节点，它还要删节点，然后才能加入新的节点。
! 回溯和递归是一一对应的，有一个递归，就要有一个回溯. 并且它们要放在同一个括号里

*/

var binaryTreePaths = function (root) {
    let currentPath = [];
    let totalPaths = [];
    helper(root, currentPath, totalPaths);
    return totalPaths;
};

function helper(node, currentPath, totalPaths) {
    currentPath.push(node.val);
    if (node.left === null && node.right === null) {
        let strPath = currentPath.join("->");
        totalPaths.push(strPath);
        return;
    }

    if (node.left) {
        helper(node.left, currentPath, totalPaths);
        currentPath.pop();
    }

    if (node.right) {
        helper(node.right, currentPath, totalPaths);
        currentPath.pop();
    }
}
