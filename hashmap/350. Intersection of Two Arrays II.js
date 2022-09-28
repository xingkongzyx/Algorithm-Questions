/* 
* 思路：此题可以看成是一道传统的映射题（map映射），为什么可以这样看呢，因为我们需找出两个数组的交集元素，同时应与两个数组中出现的次数一致。这样就导致了我们需要知道每个值出现的次数，所以映射关系就成了<元素,出现次数>,所以我们可以首先统计数组1中所有元素的出现次数。然后再遍历数组2，如果数组2中的元素在map中存在（出现次数大于0），该元素就是一个交集元素，我们就将其存入返回数组中并且将map中该元素的出现次数减一即可.

? https://leetcode.cn/problems/intersection-of-two-arrays-ii/solution/wei-shi-yao-yong-map-by-vailing-2/
*/
var intersect = function (nums1, nums2) {
    let map1 = new Map();
    for (let ele of nums1) {
        if (!map1.has(ele)) map1.set(ele, 0);
        map1.set(ele, map1.get(ele) + 1);
    }
    let res = [];
    for (let ele of nums2) {
        if (map1.has(ele)) {
            res.push(ele);
            let times = map1.get(ele);
            if (times === 1) map1.delete(ele);
            else map1.set(ele, times - 1);
        }
    }

    return res;
};

let nums1 = [1, 2, 2, 1];
let nums2 = [2, 2];
intersect(nums1, nums2);
