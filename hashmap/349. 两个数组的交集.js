// !注意题目特意说明：输出结果中的每个元素一定是唯一的，也就是说输出的结果的去重的， 同时可以不考虑输出结果的顺序
// * 先把num1中的所有元素全部添加到集合set1中，然后遍历nums2中的所有元素，判断在集合set1中是否存在，如果存在，说明有交集，就把他添加到集合result中，最后再把result转化为数组

var intersection = function (nums1, nums2) {
    let set1 = new Set(nums1);
    let result = new Set();
    for (let num of nums2) {
        if (set1.has(num)) result.add(num);
    }
    return Array.from(result);
};

console.log(intersection([1, 2, 2, 1], [2, 2]));
