// 与242类似 algoexpert 有这道题 使用hashmap解决
// space O(WN)
// time O(WNlog(N)) ->  we have w words, and for each word, we sort it with a length of at most n(n是指最长的单词长度是n)
var groupAnagrams = function (strs) {
    let records = new Map();
    for (let str of strs) {
        let key = str.split("").sort().join("");
        if (records.has(key)) {
            let val = records.get(key);
            val.push(str);
            records.set(key, val);
        } else {
            records.set(key, [str]);
        }
    }
    return Array.from(records.values());
};
let strs = ["eat", "tea", "tan", "ate", "nat", "bat"];
groupAnagrams(strs);
