/* 
把题目要求翻译成人话就是，
如果两个字符串：
* 包含的字符种类完全一样；
* 把各个字符的重复次数放在一个数组里，数组在排序后完全一样；
* 那么这两个字符串接近。

所以：

* 如果两个字符串长度不一样，那么直接返回false；
* 遍历两个字符串，用两个长度 262626 的数组存放次数；
* 同时遍历这两个数组，如果在某下标 iii 处出现一个是 000 一个不是 000（即异或结果是 111）的情况，那么直接返回false；
* 排序后如果数组不相同，也返回false；
* 否则返回true。

链接：https://leetcode.cn/problems/determine-if-two-strings-are-close/solutions/485374/tong-ji-zi-fu-de-chu-xian-ci-shu-jiu-hao-liao-by-p/

*/
var closeStrings = function (word1, word2) {
    if (word1.length !== word2.length) {
        return false;
    }

    let word1Arr = new Array(26).fill(0);
    let word2Arr = new Array(26).fill(0);
    let ASCII_A = "a".charCodeAt(0);
    for (let char of word1) {
        word1Arr[char.charCodeAt(0) - ASCII_A]++;
    }
    for (let char of word2) {
        word2Arr[char.charCodeAt(0) - ASCII_A]++;
    }

    for (let i = 0; i < 26; i++) {
        if ((word1Arr[i] === 0) !== (word2Arr[i] === 0)) return false;
    }

    word1Arr.sort((a, b) => b - a);
    word2Arr.sort((a, b) => b - a);

    for (let i = 0; i < 26; i++) {
        if (word1Arr[i] !== word2Arr[i]) return false;
    }

    return true;
};
