var mySqrt = function (x) {
    let left = 0;
    let right = x;
    while (left <= right) {
        let mid = left + Math.floor((right - left) / 2);
        let square = mid * mid;
        if (square === x) return mid;
        else if (square < x) left = mid + 1;
        else if (square > x) right = mid - 1;
    }
    return right;
};

console.log(mySqrt(4));
