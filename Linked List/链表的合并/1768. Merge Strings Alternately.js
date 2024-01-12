/* 
? https://leetcode.cn/problems/merge-strings-alternately/solutions/1913930/jiao-ti-he-bing-zi-fu-chuan-by-leetcode-ac4ih/?company_slug=microsoft
时间复杂度：O(n+m)
空间复杂度：O(n+m)
*/
var mergeAlternately = function (word1, word2) {
    let index1 = 0;
    let index2 = 0;
    let res = [];
    while (index1 < word1.length || index2 < word2.length) {
        if (index1 < word1.length) {
            res.push(word1[index1]);
            index1++;
        }
        if (index2 < word2.length) {
            res.push(word2[index2]);
            index2++;
        }
    }

    console.log(res);
    return res.join("");
};
