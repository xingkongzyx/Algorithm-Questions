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
