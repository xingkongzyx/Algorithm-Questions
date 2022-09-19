// 属于左右指针题目
/* 
方法一：暴力解法
1. 根据回文子串的定义，枚举所有长度大于等于 2 的子串，依次判断它们是否是回文；
2. 可以只针对大于「当前得到的最长回文子串长度」的子串进行回文验证；
3. 当得到了一个更长的回文时，不需要真的做截取。只需要记录「当前子串的起始位置」和「子串长度」。

时间复杂度：O(N^3)
这里 N 是字符串的长度，枚举字符串的左边界、右边界，然后继续验证子串是否是回文子串，都与 N 相关；
空间复杂度：O(1)，只使用到常数个临时变量，与字符串长度无关。


链接：https://leetcode-cn.com/problems/longest-palindromic-substring/solution/zhong-xin-kuo-san-dong-tai-gui-hua-by-liweiwei1419/


*/

var longestPalindrome = function (s) {
    let maxLen = 1;
    let resultStartIdx = 0;
    for (let i = 0; i < s.length - 1; i++) {
        for (let j = i + 1; j < s.length; j++) {
            if (j - i + 1 > maxLen && checkPalindrome(s, i, j)) {
                maxLen = j - i + 1;
                resultStartIdx = i;
            }
        }
    }
    // console.log(maxLen, result);
    return s.slice(resultStartIdx, resultStartIdx + maxLen);
};

function checkPalindrome(str, l, r) {
    let left = l;
    let right = r;
    while (left < right) {
        if (str[left] !== str[right]) return false;
        left++;
        right--;
    }
    return true;
}

longestPalindrome("cbbd");
