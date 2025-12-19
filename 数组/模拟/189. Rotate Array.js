/* 
* 引用了美服翻转做法下面的评论(第一条) 希望能帮到大家
* nums = "----->-->"; k =3
* result = "-->----->";
* reverse "----->-->" we can get "<--<-----"
* reverse "<--" we can get "--><-----"
* reverse "<-----" we can get "-->----->"
* this visualization help me figure it out :)

? https://leetcode.cn/problems/rotate-array/solutions/551039/xuan-zhuan-shu-zu-by-leetcode-solution-nipk/
*/
const reverse = (nums, start, end) => {
    while (start < end) {
        const temp = nums[start];
        nums[start] = nums[end];
        nums[end] = temp;
        start += 1;
        end -= 1;
    }
};

var rotate = function (nums, k) {
    k %= nums.length;
    reverse(nums, 0, nums.length - 1);
    reverse(nums, 0, k - 1);
    reverse(nums, k, nums.length - 1);
};
