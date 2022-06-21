var intersection = function (nums1, nums2) {
    nums1.sort((a, b) => a - b);
    nums2.sort((a, b) => a - b);
    let l = 0,
        r = 0,
        ans = [],
        pre = null;
    while (l < nums1.length && r < nums2.length) {
        if (nums1[l] === nums2[r] && pre !== nums1[l]) {
            ans.push(nums1[l]);
            pre = nums1[l];
            l++;
            r++;
        } else nums1[l] < nums2[r] ? l++ : r++;
    }
    // console.log(ans);
    return ans;
};
