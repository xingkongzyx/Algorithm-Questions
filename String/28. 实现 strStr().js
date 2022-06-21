/* 
* 直观的解法的是：枚举原串 haystack 中的每个字符作为「发起点」，每次从原串的「发起点」和匹配串的「首位」开始尝试匹配：
* 
* 匹配成功：返回本次匹配的原串「发起点」。
* 匹配失败：枚举原串的下一个「发起点」，重新尝试匹配。

? 时间复杂度：n 为原串的长度，m 为匹配串的长度。其中枚举的复杂度为 O(n - m)，构造和比较字符串的复杂度为 O(m)。整体复杂度为 O((n - m) * m)。
? 空间复杂度：O(1)。

链接：https://leetcode-cn.com/problems/implement-strstr/solution/shua-chuan-lc-shuang-bai-po-su-jie-fa-km-tb86/

*/

var strStr = function (haystack, needle) {
    //# 当 needle 是空字符串时我们应当返回 0 。
    if (needle.length === 0) return 0;
    //# 枚举原串 haystack 中的每个字符作为「发起点」
    for (let startIdx = 0; startIdx < haystack.length; startIdx++) {
        //# 使用两个指针进行匹配
        let p1 = startIdx;
        let p2 = 0;
        //# 只有当两个指针在各自字符串匹配的 character 一致时我们才能更新p1,p2
        while (p2 < needle.length && haystack[p1] === needle[p2]) {
            p1++;
            p2++;
        }
        //# 如果整个needle都是匹配的，那么最后 p2就是needle.length
        //# 如果中间有值不匹配，则p2不可能到达needle.length
        if (p2 === needle.length) return startIdx;
    }
    return -1;
};

const haystack = "mississippi";
const needle = "issip";
console.log(strStr(haystack, needle));
