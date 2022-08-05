//# 从暴力回溯可知, 当〖p1, p2, p3〗一定的情况下, 返回值一定, 由此我们可以将p1, p2, p3, 返回值用 memo[p1][p2][p3] 记录起来, 当回溯再次遇到此〖p1, p2, p3〗时, 直接返回。显然当〖p1, p2〗一定时, p3一定, 因为 p3 = p1 + p2, 因此, 可以将状态缩减成两维, 即 memo[p1][p2]。

/// 时间复杂度：O(n∗m)
/// 空间复杂度：O(n∗m)，n、m分别是s1、s2的长度

const isInterleave = (s1, s2, s3) => {
    //* 对于 s1 = a, s2 = b, s3 = a 这种情况应该返回false, 因为没有所谓的交替的情况
    if (s1.length + s2.length !== s3.length) return false;

    //* 创建 memo 数组, 用于记忆化递归, 多定义一位是因为下面进行记忆化递归的时候会出现 p1==s1.length 的情况，这时无法继续满足第一个判断条件，但如果满足第二个判定条件会进入第二个循环返回并访问对应的 memo cell
    let memo = new Array(s1.length + 1);
    for (let i = 0; i < memo.length; i++) {
        memo[i] = new Array(s2.length + 1).fill(null);
    }

    //* p1 是用于递归遍历 s1 的指针, p2 是用于递归遍历 s2 的指针, p3 是用于递归遍历 s3 的指针
    function backtracking(p1, p2, p3) {
        console.log(
            `p1 is ${p1}, p2 is ${p2}, p3 is ${p3}, memo is ${memo[p1][p2]}`
        );
        //* 如果已经求解过子问题, 则直接返回子问题的解
        if (memo[p1][p2] !== null) return memo[p1][p2];

        //* 递归终止条件, p3越界, 说明s3扫描完了, 返回true
        if (p3 === s3.length) {
            return true;
        }

        let isValid = false;
        //* 如果 p1 指针没有越界, 且 s1[p1] 和 s3[p3] 相同
        if (p1 < s1.length && s1[p1] === s3[p3]) {
            p1++;
            p3++;
            isValid = backtracking(p1, p2, p3);
            p1--;
            p3--;
        }
        //* 如果 p2 指针没有越界, 且 s2[p2] 和 s3[p3] 相同
        if (p2 < s2.length && s2[p2] === s3[p3]) {
            p2++;
            p3++;
            isValid = isValid || backtracking(p1, p2, p3);
            p2--;
            p3--;
        }
        //* 子问题求解完毕, 更新子问题的解
        memo[p1][p2] = isValid;
        return isValid;
    }
    let res = backtracking(0, 0, 0);
    return res;
};
