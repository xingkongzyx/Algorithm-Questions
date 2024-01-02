/* 
# 维护「已扫描的字符能去到的最远位置」，扫到这个位置就切割，切出的字符不会在之后出现。
* 在遍历的过程中相当于是要找每一个字母的边界，如果找到之前遍历过的所有字母的最远边界，说明这个边界就是分割点了。此时前面出现过所有字母，最远也就到这个边界了。
*/

var partitionLabels = function (s) {
    let map = {};
    //# 得到s中所有字符出现的最后位置
    for (let i = 0; i < s.length; i++) {
        map[s[i]] = i;
    }
    let result = [];

    //# 已扫描的字符中最远的位置
    let maxIdxInCurrentPartition = 0;
    //# 待切割的起始位置
    let startIdxInCurrentPartition = 0;
    for (let i = 0; i < s.length; i++) {
        //# 当前扫描的字符的最远位置
        let lastIdxOfCurrentChar = map[s[i]];
        //# 更新「已扫描的字符中最远的位置」
        maxIdxInCurrentPartition = Math.max(
            lastIdxOfCurrentChar,
            maxIdxInCurrentPartition
        );
        //# 说明到 maxIdxInCurrentPartition位置为止，前面的所有char的最后一个字符都出现在这个范围中
        if (i === maxIdxInCurrentPartition) {
            result.push(
                maxIdxInCurrentPartition -
                    startIdxInCurrentPartition +
                    1
            );
            //# 更新，下一个待切割的字符串的起始位置
            startIdxInCurrentPartition = maxIdxInCurrentPartition + 1;
        }
    }
    return result;
};
