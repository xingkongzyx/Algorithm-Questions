//? https://leetcode.cn/problems/cong-shang-dao-xia-da-yin-er-cha-shu-iii-lcof/solution/mian-shi-ti-32-iii-cong-shang-dao-xia-da-yin-er--3/
var levelOrder = function (root) {
    if (root === null) return [];
    let queue = [root];
    const result = [];
    //* 维护一个变量用于决定当前行是按照从左到右还是从右到左的顺序打印
    let count = 1;
    while (queue.length > 0) {
        const currentLevelNodesNum = queue.length;
        const currentLevelNodes = [];
        for (let i = 0; i < currentLevelNodesNum; i++) {
            const poppedNode = queue.shift();
            currentLevelNodes.push(poppedNode.val);
            if (poppedNode.left) queue.push(poppedNode.left);
            if (poppedNode.right) queue.push(poppedNode.right);
        }
        if (count % 2 == 1) {
            //* 如果count是奇数，说明这一层要正序打印(将 currentLevelNodes 数组直接加入 result)
            result.push(currentLevelNodes);
        } else {
            //* 如果count是偶数，说明这一层要逆序打印(将 currentLevelNodes 的倒序数组加入 result)
            result.push(currentLevelNodes.reverse());
        }
        count++;
    }
    return result;
};
