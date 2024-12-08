class DisjointSetUnion {
    constructor(n) {
        this.fathers = new Array(n);
        for (let i = 0; i < n; i++) {
            this.fathers[i] = i;
        }
    }

    find(u) {
        if (u == this.fathers[u]) {
            return u;
        } else {
            this.fathers[u] = this.find(this.fathers[u]);
            return this.fathers[u];
        }
    }

    join(u, v) {
        u = this.find(u);
        v = this.find(v);

        if (u === v) return;

        this.fathers[v] = u;
    }

    isSame(u, v) {
        u = this.find(u);
        v = this.find(v);
        return u === v;
    }
}

var findRedundantDirectedConnection = function (edges) {
    const numOfEdges = edges.length;
    // 因为 edges 中的边 label 是从 1 开始，所以 inDegree 长度定义需要 numOfEdges + 1
    const inDegree = new Array(numOfEdges + 1).fill(0);
    for (let i = 0; i < numOfEdges; i++) {
        const [start, end] = edges[i];
        inDegree[end] += 1;
    }

    // 找入度为2的节点所对应的边，注意要倒序，因为优先删除最后出现的一条边
    const tempArr = [];
    for (let i = numOfEdges - 1; i >= 0; i--) {
        // 遍历 edges 中的被指向的边，查看它在 inDegree 中的入度的值，记录的是在 edges 中的索引的值
        if (inDegree[edges[i][1]] === 2) {
            tempArr.push([i]);
        }
    }

    function isTreeAfterRemoveEdge(deleteEdgeIdx) {
        const union = new DisjointSetUnion(edges.length + 1);
        for (let i = 0; i < edges.length; i++) {
            if (i === deleteEdge) continue;

            if (union.isSame(edges[i][0], edges[i][1])) {
                return false;
            }

            union.join(edges[i][0], edges[i][1]);
        }
    }

    function getRemoveEdge() {
        const union = new DisjointSetUnion(edges.length + 1);
        for (let i = 0; i < numOfEdges; i++) {
            // 遍历所有的边
            if (union.same(edges[i][0], edges[i][1])) {
                // 构成有向环了，就是要删除的边
                return [edges[i][0], edges[i][1]];
            } else {
                union.join(edges[i][0], edges[i][1]);
            }
        }
    }

    if (tempArr.length > 0) {
        if (isTreeAfterRemoveEdge(tempArr[0])) {
            return [edges[tempArr[0]][0], edges[tempArr[0]][1]];
        } else {
            return [edges[tempArr[1]][0], edges[tempArr[1]][1]];
        }
    }

    return getRemoveEdge;
};
