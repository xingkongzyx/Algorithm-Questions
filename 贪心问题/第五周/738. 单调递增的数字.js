/* 
* 贪心思路
* ①．要使目标数字和 N 最接近，则需要尽可能保持高位数字不动
* ②．若某高位数字减 1，则后续所有低位数字都可直接更改为 9，可保持最接近(例如100)
* ③．若低位数字更改为 9，则前一高位数字至少得减 1，可保持最接近

* 解题步骤
* 因此，首先从高位开始找到第一个非升序的位，将 numArr[i-1] 减 1，并标记从第i位开始后面的统一改成9(也就是下面代码记录的 idxNeedsToChange)；然后继续往前判断看更改后是否满足升序要求，若不满足要求则把idxNeedsToChange 更改到本位，前一位 (numArr[i-1]) 继续减 1，直到满足升序。

* 最后从idxNeedsToChange这一位置开始将后续的 numArr位置赋值为9
* 遇到了3425正确的结果是 3399. 如果不记录 idxNeedsToChange，而只是把numArr[i] 赋值为9 则会得到结果 3395

*/

var monotoneIncreasingDigits = function (n) {
    let numArr = String(n).split("");
    let idxNeedsToChange = numArr.length;
    for (let i = numArr.length - 1; i > 0; i--) {
        if (numArr[i - 1] > numArr[i]) {
            numArr[i - 1]--;
            idxNeedsToChange = i;
        }
    }
    for (let i = idxNeedsToChange; i < numArr.length; i++) {
        numArr[i] = 9;
    }
    return parseInt(numArr.join(""));
};
let res = monotoneIncreasingDigits(23425);
console.log(res);
