/* 
* 1. 给一个孩子的饼干应当尽量小并且又能满足该孩子，这样大饼干才能拿来给满足度比较大的孩子。
* 2. 因为满足度最小的孩子最容易得到满足，所以先满足满足度最小的孩子。
? https://leetcode.cn/problems/assign-cookies/solution/tan-xin-jie-fa-by-cyc2018/
*/
var findContentChildren = function (g, s) {
    g.sort((a, b) => a - b);
    s.sort((a, b) => a - b);
    let result = 0;
    let childIdx = 0;
    let cookieIdx = 0;
    while (childIdx < g.length && cookieIdx < s.length) {
        if (s[cookieIdx] >= g[childIdx]) {
            result++;
            childIdx++;
            cookieIdx++;
        } else {
            cookieIdx++;
        }
    }

    return result;
};
