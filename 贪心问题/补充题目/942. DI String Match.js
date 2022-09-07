/* 
* 考虑 perm[0] 的值, 根据题意：
* 
* 如果 s[0]='I', 那么令 perm[0]=0, 则无论 perm[1] 为何值都满足 perm[0] < perm[1]；
* 如果 s[0]='D', 那么令 perm[0]=n, 则无论 perm[1] 为何值都满足 perm[0] > perm[1]；
* 确定好 perm[0] 后, 剩余的 n-1 个字符和 n 个待确定的数就变成了一个和原问题相同, 但规模为 n-1 的问题
/ 总之，就是一个贪心策略，遇到 I就选剩余候选集的最小值，遇到 D就选剩余候选集的最大值。
? https://leetcode.cn/problems/di-string-match/solution/zeng-jian-zi-fu-chuan-pi-pei-by-leetcode-jzm2/
? 详细解释(必看): https://leetcode.cn/problems/di-string-match/solution/by-fuxuemingzhu-20do/
*/
var diStringMatch = function (s) {
    let n = s.length;
    let low = 0;
    let high = n;

    let perm = new Array(n + 1).fill(0);

    for (let i = 0; i < s.length; i++) {
        if (s[i] == "I") {
            perm[i] = low;
            low += 1;
        } else {
            perm[i] = high;
            high -= 1;
        }
    }
    // 最后 low 与 high 是重合的, low == high
    perm[n] = low;
    return perm;
};
