/**
 * @param {number[]} g
 * @param {number[]} s
 * @return {number}
 */
var findContentChildren = function (g, s) {
    g.sort((a, b) => a - b);
    s.sort((a, b) => a - b);
    let result = 0;
    let childIdx = g.length - 1;
    let cookieIdx = s.length - 1;
    while (cookieIdx >= 0) {
        if (s[cookieIdx] >= g[childIdx]) {
            result++;
            childIdx--;
            cookieIdx--;
        } else {
            childIdx--;
        }

        if (childIdx < 0) return result;
    }

    return result;
};
