// ? https://leetcode.cn/problems/single-number/solutions/10261/hua-jie-suan-fa-136-zhi-chu-xian-yi-ci-de-shu-zi-b/?envType=study-plan-v2&envId=top-100-liked
var singleNumber = function (nums) {
    let res = 0;
    for (let num of nums) {
        res ^= num;
    }

    return res;
};
