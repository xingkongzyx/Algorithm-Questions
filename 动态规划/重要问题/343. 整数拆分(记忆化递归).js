/**
 * @param {number} n
 * @return {number}
 */

/*
 * 1. 递归参数和返回值
 * 参数就是当前要拆分的整数，返回值为当前整数拆分结果的最大积
 * 2. 递归终止条件
 * 当目前传入参数的最大积已经被记录在 memo 中，则直接返回 memo[n]
 * 当目前参数等于2，则直接返回1. 因为这是最下能拆分的数字
 * 3. 本层递归
 * 对于 n 计算 i * (n-i), i * helper(n - i)之间的最大值，并将结果储存在 memo 数组
 */

var integerBreak = function (n) {
    const memo = new Array(n + 1).fill(-1);

    function helper(n) {
        if (n == 2) return 1;
        if (memo[n] !== -1) return memo[n];

        let res = 0;
        for (let i = 1; i <= n - 1; i++) {
            res = Math.max(
                res,
                Math.max(i * (n - i), i * helper(n - i))
            );
        }
        memo[n] = res;
        return res;
    }

    return helper(n);
};

console.log(integerBreak(10));
