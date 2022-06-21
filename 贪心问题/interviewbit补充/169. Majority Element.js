let majorityElement = function (A) {
    let map = {};

    for (let i = 0; i < A.length; i++) {
        if (A[i] in map) {
            map[A[i]] += 1;
        } else {
            map[A[i]] = 1;
        }
    }
    let requiredTimes = Math.floor(A.length / 2);
    for (let key in map) {
        if (map[key] > requiredTimes) return key;
    }
};

console.log(majorityElement([2, 1, 2]));
