var twoSum = function (nums, target) {
    let record = {};
    for (let i = 0; i < nums.length; i++) {
        let num = nums[i];
        let remain = target - num;
        if (record.hasOwnProperty(remain)) {
            let remainNumIdx = record[remain];
            return [i, remainNumIdx];
        } else {
            record[num] = i;
        }
    }
    return [-1, -1];
};
console.log(twoSum([2, 7, 11, 15], 9));
console.log(twoSum([3, 2, 4], 6));
console.log(twoSum([3, 3], 6));
