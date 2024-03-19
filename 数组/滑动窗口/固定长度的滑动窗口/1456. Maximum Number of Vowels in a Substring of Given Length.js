/* 
? https://leetcode.cn/problems/maximum-number-of-vowels-in-a-substring-of-given-length/solutions/259591/hua-dong-chuang-kou-chao-hao-li-jie-de-ti-jie-ding/?envType=study-plan-v2&envId=leetcode-75
*/
var maxVowels = function (s, k) {
    let result = 0;
    let vowelSet = new Set(["a", "e", "i", "o", "u"]);

    let left = 0;
    let right = 0;
    let curLen = 0;

    while (right < s.length) {
        let rightChar = s[right];

        if (vowelSet.has(rightChar)) {
            curLen++;
        }

        if (right - left + 1 === k) {
            let leftChar = s[left];
            result = Math.max(curLen, result);
            if (vowelSet.has(leftChar)) {
                curLen--;
            }
            left++;
        }

        right++;
    }
    return result;
};
