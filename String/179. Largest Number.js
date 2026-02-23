/* 
https://leetcode.cn/problems/largest-number/solutions/2361893/179-zui-da-shu-tan-xin-qing-xi-tu-jie-by-wboz/
*/
var largestNumber = function (nums) {
    let numStrArr = [];
    for (let num of nums) {
        let numStr = String(num);
        numStrArr.push(numStr);
    }

    numStrArr.sort((a, b) => (b + a).localeCompare(a + b));
    if (numStrArr[0] === "0") return "0";
    return numStrArr.join("");
};
