/* 
大体思路就是从低到上，先给叶子节点父节点放个摄像头，然后隔两个节点放一个摄像头，直至到二叉树头结点。
*/
var minCameraCover = function (root) {
    let result = 0;
    function traverse(node) {
        // 空节点, 根据上面讲解, 遇到空节点必须返回该节点有覆盖的状态
        if (node === null) return 2;
        let left = traverse(node.left);
        let right = traverse(node.right);

        // 情况1
        // 左右节点都有覆盖
        if (left === 2 && right === 2) return 0;

        // 情况2
        // left == 0 && right == 0 左右节点无覆盖
        // left == 1 && right == 0 左节点有摄像头，右节点无覆盖
        // left == 0 && right == 1 左节点有无覆盖，右节点摄像头
        // left == 0 && right == 2 左节点无覆盖，右节点覆盖
        // left == 2 && right == 0 左节点覆盖，右节点无覆盖
        if (left === 0 || right === 0) {
            result++;
            return 1;
        }

        // 情况3
        // left == 1 && right == 2 左节点有摄像头，右节点有覆盖
        // left == 2 && right == 1 左节点有覆盖，右节点有摄像头
        // left == 1 && right == 1 左右节点都有摄像头
        // 其他情况前段代码均已覆盖
        if (left === 1 || right === 1) return 2;
    }
    if (traverse(root) === 0) {
        result++;
    }

    return result;
};
