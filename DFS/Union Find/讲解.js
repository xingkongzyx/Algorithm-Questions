// ? https://leetcode.cn/problems/number-of-provinces/solution/python-duo-tu-xiang-jie-bing-cha-ji-by-m-vjdr/
// ? https://programmercarl.com/kamacoder/%E5%9B%BE%E8%AE%BA%E5%B9%B6%E6%9F%A5%E9%9B%86%E7%90%86%E8%AE%BA%E5%9F%BA%E7%A1%80.html#%E8%83%8C%E6%99%AF

class DisjointSetUnion {
    constructor(n) {
        this.fathers = new Array(n);
        for (let i = 0; i < n; i++) {
            this.fathers[i] = i;
        }
    }

    // Function to find the representative (or root) of the set containing element 'u'
    // This implementation uses path compression to speed up future queries
    find(u) {
        if (u == this.fathers[u]) {
            // If 'u' is the root of its set (i.e., 'u' is its own parent), return 'u'
            return u;
        } else {
            // Recursively find the root of 'u's parent and compress the path
            // by making 'u' directly point to the root
            this.fathers[u] = this.find(this.fathers[u]);
            // Return the root of the set containing 'u'
            return this.fathers[u];
        }
    }

    join(u, v) {
        // This line uses the find method to determine the representative (or root) of the set containing element u.
        // The find method also performs path compression, making future queries faster.
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
