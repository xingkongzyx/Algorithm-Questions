/*
 * 定义一个数组叫做 hash 用来记录字符串s里字符出现的次数。
 *
 * 需要把字符映射到数组也就是哈希表的索引下标上, 因为字符a到字符 z 的 ASCII 是 26 个连续的数值, 所以字符 a 映射为下标0, 相应的字符z映射为下标 25。
 *
 * 再遍历 字符串s的时候, 只需要将 s[i] - "a" 所在的元素做 +1 操作即可, 并不需要记住字符a的ASCII, 只要求出一个相对数值就可以了。 这样就将字符串s中字符出现的次数, 统计出来了。
 *
 * 那看一下如何检查字符串t中是否出现了这些字符, 同样在遍历字符串t的时候, 对t中出现的字符映射哈希表索引上的数值再做 -1 的操作。
 *
 * 那么最后检查一下, record数组如果有的元素不为零0, 说明字符串s和t一定是谁多了字符或者谁少了字符, return false。
 */

var isAnagram = function (s, t) {
    let hash = new Array(26).fill(0);
    // This method returns a number indicating the Unicode value of the character at the given index.
    let baseUnicode = "a".charCodeAt(0);
    for (let i = 0; i < s.length; i++) {
        let currentCharUnicode = s[i].charCodeAt(0);
        hash[currentCharUnicode - baseUnicode] += 1;
    }

    for (let j = 0; j < t.length; j++) {
        let currentCharUnicode = t[j].charCodeAt(0);
        hash[currentCharUnicode - baseUnicode] -= 1;
    }
    // 如果有一个index不为0, 则说明s和t所含有的字符数量或者种类不一样, 直接返回false
    for (let i = 0; i < hash.length; i++) {
        if (hash[i] !== 0) return false;
    }
    return true;
};
