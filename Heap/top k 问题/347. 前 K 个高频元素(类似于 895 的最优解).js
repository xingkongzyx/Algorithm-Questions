/**
 * 347. 前 K 个高频元素
 * https://leetcode.cn/problems/top-k-frequent-elements/
 *
 * 核心思路：桶排序（Bucket Sort）
 * --------------------------------
 * 与 895.最大频率栈 的最优解思路类似，都是将元素按频率分桶：
 *   - 895 中：用 stack[freq] 存储频率为 freq 的元素，支持 O(1) 的 push/pop
 *   - 347 中：用 buckets[freq] 存储出现次数为 freq 的所有元素，然后从高频桶向低频桶遍历取出前 K 个
 *
 * 时间复杂度：O(n)，其中 n 为 nums 的长度
 *   - 统计频率 O(n) + 填桶 O(n) + 收集结果 O(n) = O(n)
 * 空间复杂度：O(n)，频率桶最多 n+1 个槽位
 *
 * 步骤：
 *   1. 用 Map 统计每个元素的出现频率
 *   2. 创建长度为 n+1 的桶数组，索引 i 表示"出现 i 次的元素集合"
 *      （频率最大值不超过 n，所以桶的索引范围为 [0, n]）
 *   3. 将每个元素放入其频率对应的桶中
 *   4. 从高频桶向低频桶遍历，依次收集元素，直到收集满 K 个
 */

/**
 * @param {number[]} nums
 * @param {number} k
 * @return {number[]}
 */
var topKFrequent = function (nums, k) {
    // 第一步：统计每个元素的出现频率
    const freqMap = new Map();
    for (const num of nums) {
        freqMap.set(num, (freqMap.get(num) || 0) + 1);
    }

    // 第二步：创建频率桶，索引 i 代表出现次数为 i 的元素集合
    // 元素最多出现 nums.length 次，所以桶大小为 nums.length + 1（索引 0 ~ n）
    const buckets = new Array(nums.length + 1);
    for (let i = 0; i < buckets.length; i++) {
        buckets[i] = [];
    }

    // 第三步：将每个元素放入其频率对应的桶中
    for (const [num, freq] of freqMap.entries()) {
        buckets[freq].push(num);
    }

    // 第四步：从最高频率的桶开始向低频遍历，收集前 K 个高频元素
    const result = [];
    for (let freq = buckets.length - 1; freq > 0; freq--) {
        const currentBucket = buckets[freq];
        for (const num of currentBucket) {
            result.push(num);
            if (result.length === k) return result;
        }
    }

    return result;
};
