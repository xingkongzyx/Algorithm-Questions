/* 
* 在 10 个灯中选 turnedOn 个灯点亮, 如果选择的灯所组成的时间已不合理(小时超过 11 或者 分钟超过59), 就进行剪枝
* 也就是从 0 到 10 先选一个灯亮, 再选当前灯的后面的灯亮, 再选后面的灯的后面的灯亮, 一直到num个灯点满
//! 这道题可以抽象成「组合」问题
* 题目可以转化为在 [1, 2, 4, 8, 1, 2, 4, 8, 16, 32] 中任意取 n 个数值, 有几种「组合」? 「组合」可以使用「回溯法」求解得到。
? 思路来源: https://leetcode.cn/problems/binary-watch/solution/czong-jie-liao-hui-su-wen-ti-lei-xing-dai-ni-gao-d/
*/

var readBinaryWatch = function (turnedOn) {
    let candidates = [1, 2, 4, 8, 1, 2, 4, 8, 16, 32];
    let cutIdx = 3;

    let result = [];
    let currentTime = [0, 0];

    //* count 代表已经点亮的灯的数量，startIdx 代表哪一个位置开始点亮灯
    function backtracking(count, startIdx) {
        //* 每次进入递归后，先判断当前「小时数」和「分钟数」是否符合要求，不符合直接 return。因为当 hour>11 或 minute>59 的时候, 无论还有没有灯可以点亮, 都不用再继续递归下去
        if (currentTime[0] > 11 || currentTime[1] > 59) return;
        if (count === turnedOn) {
            let [hour, minute] = currentTime;
            let resStr = `${hour}:${
                minute < 10 ? "0" + minute : minute
            }`;
            result.push(resStr);
            return;
        }
        for (let i = startIdx; i < candidates.length; i++) {
            if (i > cutIdx) {
                //* 当前选取的灯属于 minutes 范围
                currentTime[1] += candidates[i];
                count += 1;
                backtracking(count, i + 1);
                count -= 1;
                currentTime[1] -= candidates[i];
            } else {
                //* 当前选取的灯属于 hours 范围
                currentTime[0] += candidates[i];
                count += 1;
                backtracking(count, i + 1);
                count -= 1;
                currentTime[0] -= candidates[i];
            }
        }
    }
    backtracking(0, 0);
    return result;
};

readBinaryWatch(2);
