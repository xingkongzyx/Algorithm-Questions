/* 
* https://leetcode.cn/problems/palindromic-substrings/solution/shou-hua-tu-jie-dong-tai-gui-hua-si-lu-by-hyj8/

! 我觉得有必要解释一下为什么从右下角遍历：因为在填dp表时，(i, j) 位置的值依赖于（i+1,j-1），也就是当前位置的左下方。显然如果从上往下遍历，左下方的值就完全没有初始化，当然当前位置也会是错误的。但是从右下角遍历就保证了左下方的所有值都已经计算好了。
*/

https: var countSubstrings = function (s) {
    let s_len = s.length;
    let dp = new Array(s_len);
    for (let i = 0; i < dp.length; i++) {
        dp[i] = new Array(s_len).fill(false);
    }
    let result = 0;
    //* 从下到上，从左到右去遍历
    for (let i = dp.length; i >= 0; i--) {
        for (let j = i; j < dp.length; j++) {
            if (s[i] === s[j]) {
                if (j - i <= 1) {
                    dp[i][j] = true;
                    result += 1;
                } else if (j - i > 1) {
                    dp[i][j] = dp[i + 1][j - 1];
                    if (dp[i][j] === true) result += 1;
                }
            } else dp[i][j] = false;
        }
    }
    // console.log(dp);
    // console.log(result);
    return result;
};
countSubstrings("aaaaa");
