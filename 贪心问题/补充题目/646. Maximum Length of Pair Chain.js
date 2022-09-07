/* 
> 原理同435.无重叠区间
* 步骤: 我们其实需要根据对数中的第二个值进行排序, 因为这个值越小, 就能够给其他对数腾出更多的空间. 
# 核心思想：尽可能多的有不重叠的区间, 所以取第二个数小的区间, 这样后边才有位置放其他的区间(其实也就是有更多的数对)
贪心的证明一般使用反证法, 所谓反证法, 即如果不是按照贪心的策略去做会怎么样。

证明: 如果我们不是优先选择第二个数较小的元素, 那么势必导致我们后面可选的元素数量减少, 最终导致选择的数对变少。比如给定数对为 [[1,2], [1,3], [3,4]], 假如我们先选择 [1,3], 那么, 我们就选择不了 [3,4] 这个元素了, 最终的数对链长度只能为 1；而我们优先选择 [1,2], 则可以再选择 [3,4], 使得选择的数对链长度为 2, 明显是最优解。

? https://leetcode.cn/problems/maximum-length-of-pair-chain/solution/by-tong-zhu-7em5/
? 形象讲解 https://leetcode.cn/problems/maximum-length-of-pair-chain/solution/by-muse-77-nyv6/

/ 时间复杂度：O(NlogN), 主要在于排序, 贪心遍历只需要O(N)。
*/
var findLongestChain = function (pairs) {
    pairs.sort((a, b) => a[1] - b[1]);
    // console.log(pairs)
    let prevRight = -Infinity;
    let res = 0;
    for (let i = 0; i < pairs.length; i++) {
        if (pairs[i][0] > prevRight) {
            res += 1;
            prevRight = pairs[i][1];
        }
    }
    return res;
};
