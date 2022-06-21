// 计算 mid 时需要防止溢出，代码中left + (right - left) / 2就和(left + right) / 2的结果相同，但是有效防止了left和right太大直接相加导致溢出。
function binarySearch(nums, target) {
    let left = 0;
    let right = nums.length - 1; // 注意
/* 
while(left <= right)的终止条件是left == right + 1，写成区间的形式就是[right + 1, right]，或者带个具体的数字进去[3, 2]，可见这时候区间为空，因为没有数字既大于等于 3 又小于等于 2 的吧。所以这时候 while 循环终止是正确的，直接返回 -1 即可。
*/
    while (left <= right) {
        let mid = left + Math.floor((right - left) / 2);
        if (nums[mid] === target) return mid;
        else if (nums[mid] < target) left = mid + 1;
        else if (nums[mid] > target) right = mid - 1;
    }
    return -1;
}
