/* 
* 跳几步无所谓, 关键在于可跳到的覆盖范围！
* 不一定非要明确一次究竟跳几步, 每次取最大的跳跃步数, 这个就是可以跳跃的覆盖范围。
* 这个范围内, 别管是怎么跳的, 反正一定可以跳过来。 
? https://leetcode.cn/problems/jump-game/solution/55-by-ikaruga/
* 这个问题就转化为跳跃覆盖范围究竟可不可以覆盖到终点！
# 贪心算法局部最优解: 每次取最大跳跃步数(取最大覆盖范围), 整体最优解: 最后得到整体最大覆盖范围, 看是否能到终点。
*/
var canJump = function (nums) {
    if (nums === null || nums.length == 0) {
        return true;
    }
    let maxCover = 0;
    for (let i = 0; i < nums.length; i++) {
        //* i 最多到达数组尾部, 如果我们「最远可覆盖的范围」比 i 小, 那么肯定到达不了数组尾部, 停止traverse, 返回false
        if (maxCover < i) return false;
        //* 获取从这个index出发可以覆盖的范围
        let currentCover = i + nums[i];
        //* 与 maxCover 比较并更新
        maxCover = Math.max(currentCover, maxCover);
    }
    // * 只要出了循环, 说明终点 len(nums)-1 位置是属于「跳跃达到的最远覆盖范围内」的, 所以一定可以跳跃到终点, 返回 True
    return true;
};
