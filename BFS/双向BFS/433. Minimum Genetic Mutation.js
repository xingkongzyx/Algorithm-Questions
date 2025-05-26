/**
 * @param {string} startGene - 起始基因序列
 * @param {string} endGene - 目标基因序列
 * @param {string[]} bank - 可供转换的合法基因序列集合
 * @return {number} - 从 startGene 变换为 endGene 所需的最小步数，不可达时返回 -1
 */
var minMutation = function (startGene, endGene, bank) {
    // 将基因库转换为 Set，便于快速查找
    const bankSet = new Set(bank);

    // 如果目标基因不在基因库中，直接返回 -1
    if (!bankSet.has(endGene)) {
        return -1;
    }

    // BFS 队列初始化
    const queue = [startGene];

    // 记录访问过的基因，避免重复访问
    let visitedSet = new Set();
    visitedSet.add(startGene);

    let mut = 0; // 记录变异的步数（层数）

    // BFS 主循环
    while (queue.length) {
        mut++; // 每进入新的一层，变异次数 +1
        let qLen = queue.length; // 当前层的元素数量

        // 遍历当前层的所有基因序列
        for (let i = 0; i < qLen; i++) {
            let curGene = queue.shift(); // 当前处理的基因序列

            // 尝试用 bankSet 中的每一个基因序列进行变异
            for (let newGene of bankSet) {
                // 如果是只相差一个字符的“邻居”，且未访问过
                if (
                    isNeighbour(newGene, curGene) &&
                    !visitedSet.has(newGene)
                ) {
                    // 如果正好是目标基因，返回当前步数
                    if (newGene === endGene) return mut;

                    // 否则加入队列，继续BFS
                    visitedSet.add(newGene);
                    queue.push(newGene);
                }
            }
        }
    }

    // 判断两个基因序列是否只差一个字符（即“邻居”关系）
    function isNeighbour(geneA, geneB) {
        if (geneA.length !== geneB.length) return false;
        let flag = false; // 是否已经发现一次字符不同

        for (let i = 0; i < geneA.length; i++) {
            if (geneA[i] !== geneB[i]) {
                // 如果已经发现一次不同，再发现就说明不相邻
                if (flag) {
                    return false;
                }
                flag = true;
            }
        }
        return flag; // 只有一次字符不同才算邻居
    }

    // 遍历结束未找到目标基因
    return -1;
};
