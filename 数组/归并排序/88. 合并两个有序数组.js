/* 
从前往后遍历导致原有数组元素被破坏掉:
nums1=[10, 20, 33, 0, 0, 0] nums2=[1, 2, 3], 从前往后遍历, nums1 的三个值会被 nums2 覆盖掉 

> 关键是要从后开始遍历
* 从后开始遍历的好处
* 先比较较大的数, 把大的数放到数组nums1的后面
* 如果先从较小的数比较, 则nums1的元素可能发生移位后挪, 时间复杂度高一些。

? https://leetcode.cn/problems/merge-sorted-array/solutions/701001/ni-xiang-shuang-zhi-zhen-he-bing-liang-g-ucgj/

 */

var merge = function (nums1, m, nums2, n) {
    let index1 = m - 1;
    let index2 = n - 1;
    let insert = m + n - 1;
    while (index1 >= 0 || index2 >= 0) {
        if (index1 < 0) {
            nums1[insert] = nums2[index2];
            index2--;
        } else if (index2 < 0) {
            nums1[insert] = nums1[index1];
            index1--;
        } else {
            // 这里能够确定 nums1[index1] 和 [index2]都是有确切的值的
            if (nums1[index1] >= nums2[index2]) {
                nums1[insert] = nums1[index1];
                index1--;
            } else {
                nums1[insert] = nums2[index2];
                index2--;
            }
        }

        insert--;
    }
};
