/* 
为了降低时间复杂度，需要考虑其他的做法。从左到右遍历数组 wordsDict，当遍历到 word1 时，如果已经遍历的单词中存在 word2，为了计算最短距离，应该取最后一个已经遍历到的 word2 所在的下标，计算和当前下标的距离。同理，当遍历到 word2 时，应该取最后一个已经遍历到的 word 1所在的下标，计算和当前下标的距离。

/ 时间复杂度：O(n)，其中 n 是数组 wordsDict 的长度。需要遍历数组一次计算 word1和 word2 的最短距离，每次更新下标和更新最短距离的时间都是 O(1)。这里将字符串的长度视为常数。
/ 空间复杂度：O(1)。

? 链接：https://leetcode.cn/problems/shortest-word-distance/solutions/1501482/zui-duan-dan-ci-ju-chi-by-leetcode-solut-86bt/
*/
var shortestDistance = function (wordsDict, word1, word2) {
    let word1Idx = -1;
    let word2Idx = -1;
    let minDis = Infinity;
    for (let i = 0; i < wordsDict.length; i++) {
        if (wordsDict[i] === word1) {
            word1Idx = i;
        }
        if (wordsDict[i] === word2) {
            word2Idx = i;
        }

        if (word1Idx !== -1 && word2Idx !== -1) {
            minDis = Math.min(minDis, Math.abs(word2Idx - word1Idx));
        }
    }

    return minDis;
};
