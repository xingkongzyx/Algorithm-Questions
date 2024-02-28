/**
https://leetcode.cn/problems/max-number-of-k-sum-pairs/?envType=study-plan-v2&envId=leetcode-75
 */
var maxOperations = function (nums, k) {
    let map = new Map(); // 创建一个Map来存储每个数字及其出现的次数

    // 遍历数组，统计每个数字出现的次数
    nums.forEach((num) => {
        let count = map.get(num) || 0; // 获取当前数字的计数，如果未定义则为0
        map.set(num, count + 1); // 更新这个数字的计数
    });

    let result = 0; // 初始化结果计数器

    // 再次遍历数组，寻找和为k的数对
    nums.forEach((num) => {
        let complement = k - num; // 计算当前数字的补数，使得num + complement = k
        let count = map.get(num); // 获取当前数字的计数

        // 如果当前数字的计数小于等于0，则跳过，因为它已经被配对
        if (count <= 0) return;

        //统计数量减一，先减去，防止两个相同的数据相加达到K，而只有一个数据，例如 nums=[2], k=2，此时的结果应该是 0 而不是 1
        map.set(num, count - 1); // 减少当前数字的计数，因为它已被配对

        // 如果补数存在于map中且其计数大于0
        if (map.has(complement) && map.get(complement) > 0) {
            result++; // 找到有效的数对，增加结果计数器
            map.set(complement, map.get(complement) - 1); // 减少补数的计数，因为它也被配对
        }
    });

    return result; // 返回找到的数对数量
};
