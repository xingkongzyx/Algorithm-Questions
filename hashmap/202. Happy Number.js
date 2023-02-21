/* 
* 如果输入为19的话结果为
* 82, 68, 100, 1

* 如果输入为2的话则会无限循环，循环为
* 4, 16, 37, 58, 89, 145, 42, 20, 
* 4, 16, 37, 58, 89, 145, 42, 20
!所以如果是无限循环则一定会出现重复数，我们使用set辅助判断  
! 所以这道题目使用哈希法，来判断这个 sum 是否重复出现，如果重复了就是 return false， 否则一直找到sum为1为止。
*/

var getSum = function (n) {
    let sum = 0;
    while (n) {
        sum += (n % 10) ** 2;
        n = Math.floor(n / 10);
    }
    return sum;
};

var isHappy = function (n) {
    let set = new Set();
    let num = n;
    while (true) {
        sum = getSum(num);
        if (set.has(sum)) return false;
        set.add(sum);
        if (sum === 1) return true;
        num = sum;
    }
};

console.log(isHappy(19));
