/* 
* 我们先对数组进行排序。
* 
* 由于每两个数，我们只能选择当前小的一个进行累加。
* 
* 因此我们猜想应该从第一个位置进行选择，然后隔一步选择下一个数。这样形成的序列的求和值最大。

? https://leetcode.cn/problems/array-partition/solution/jue-dui-neng-kan-dong-de-zheng-ming-fan-f7trz/

*/
var arrayPairSum = function (nums) {
    nums.sort((a, b) => a - b);
    // console.log(nums)
    let res = 0;
    for (let i = 0; i < nums.length; i += 2) {
        let firstNum = nums[i];
        let secondNum = nums[i + 1];
        res += Math.min(firstNum, secondNum);
    }
    return res;
};
