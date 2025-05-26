/**
 * @param {string} startGene
 * @param {string} endGene
 * @param {string[]} bank
 * @return {number}
 */
var minMutation = function (startGene, endGene, bank) {
    const bankSet = new Set(bank);
    if (!bankSet.has(endGene)) {
        return -1;
    }
    let beginSet = new Set([startGene]);
    let endSet = new Set([endGene]);
    // const queue = ;
    let visitedSet = new Set([startGene, endGene]);

    let mut = 0;
    while (beginSet.size && endSet.size) {
        if (beginSet.size > endSet.size) {
            let temp = beginSet;
            beginSet = endSet;
            endSet = temp;
        }
        mut++;
        let qLen = beginSet.size;
        let nextQueue = new Set();
        for (let curGene of beginSet) {
            for (let newGene of bankSet) {
                if (isNeighbour(newGene, curGene)) {
                    if (endSet.has(newGene)) return mut;

                    visitedSet.add(newGene);
                    nextQueue.add(newGene);
                }
            }
        }
        beginSet = nextQueue;
    }

    function isNeighbour(geneA, geneB) {
        if (geneA.length !== geneB.length) return false;
        let flag = false;
        for (let i = 0; i < geneA.length; i++) {
            if (geneA[i] !== geneB[i]) {
                if (flag) {
                    return false;
                }
                flag = true;
            }
        }
        return flag;
    }

    return -1;
};
