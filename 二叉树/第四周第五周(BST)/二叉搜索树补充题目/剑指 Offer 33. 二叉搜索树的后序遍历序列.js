// https://leetcode.cn/problems/er-cha-sou-suo-shu-de-hou-xu-bian-li-xu-lie-lcof/
//? https://leetcode.cn/problems/er-cha-sou-suo-shu-de-hou-xu-bian-li-xu-lie-lcof/solution/di-gui-he-zhan-liang-chong-fang-shi-jie-jue-zui-ha/
var verifyPostorder = function (postorder) {
    function helper(startIdx, endIdx, arr) {
        if (startIdx >= endIdx) return true;

        let rootVal = arr[endIdx];
        let cutIdx = startIdx;
        //* 寻找左右子树分割点
        while (arr[cutIdx] < rootVal) cutIdx += 1;

        let rightStartIdx = cutIdx;
        let rightEndIdx = endIdx - 1;
        let leftStartIdx = startIdx;
        let leftEndIdx = rightStartIdx - 1;

        //* 确保右子树区间 [rightStartIdx, rightEndIdx] 内的所有节点都应「大于」 rootVal。实现方式为遍历，当遇到『arr[cutIdx] <= arr[endIdx]』的 cutIdx 节点则跳出；如果是合格的二叉搜索树则 cutIdx 应该「等于」 endIdx
        while (arr[cutIdx] > arr[endIdx]) cutIdx += 1;
        if (cutIdx !== endIdx) return false;

        let leftRes = helper(leftStartIdx, leftEndIdx, arr);
        if (leftRes === false) return leftRes;

        let rightRes = helper(rightStartIdx, rightEndIdx, arr);
        if (rightRes === false) return rightRes;

        return true;
    }

    return helper(0, postorder.length - 1, postorder);
};
