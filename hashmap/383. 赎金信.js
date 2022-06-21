// 与242类似
/* 
用一个长度为26的数组还记录magazine里字母出现的次数，然后再用ransomNote去验证这个数组是否包含了ransomNote所需要的所有字母。

*/

// 时间复杂度: O(n)
// 空间复杂度：O(1)
var canConstruct = function (ransomNote, magazine) {
    let record = new Array(26).fill(0);
    let baseUnicode = "a".charCodeAt(0);
    for (let i = 0; i < magazine.length; i++) {
        let currentCharUnicode = magazine[i].charCodeAt(0);
        record[currentCharUnicode - baseUnicode] += 1;
    }

    for (let i = 0; i < ransomNote.length; i++) {
        // 遍历ransomNote，在record里对应的字符个数做--操作
        let currentCharUnicode = ransomNote[i].charCodeAt(0);
        record[currentCharUnicode - baseUnicode] -= 1;
    }

    for (let j = 0; j < record.length; j++) {
        // 如果小于零说明 magazine里出现的字符，ransomNote没有
        if (record[j] < 0) return false;
    }
    return true;
};
