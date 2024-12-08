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

var validPath = function (n, edges, source, destination) {
    // ! 这里传递是 n，而不能是 edges.length，否则如果 edges.length 小但是edges里面包含的数值大，使用 edges.length init fathers length 会出现报错
    const union = new DisjointSetUnion(n);
    for (let [s, e] of edges) {
        union.join(s, e);
    }

    return union.isSame(source, destination);
};
