/**
 * @param {string} num
 * @return {boolean}
 */
var isAdditiveNumber = function (num) {
    let curPath = [];
    let total = false;
    function backtracking(num, startIdx) {
        if (startIdx === num.length) {
            console.log(curPath);
            if (curPath.length >= 3) {
                let sum = curPath[curPath.length - 1];
                let num1 = curPath[curPath.length - 2];
                let num2 = curPath[curPath.length - 3];
                if (sum === num1 + num2) {
                    total = true;
                    return;
                }
            }
        }

        for (let i = startIdx; i < num.length; i++) {
            let curNum = parseInt(num.substring(startIdx, i + 1));
            console.log("curnum", curNum);
            if (curPath.length < 2) {
                curPath.push(curNum);
                backtracking(num, i + 1);
                curPath.pop();
            } else {
                let firstNum = curPath[curPath.length - 1];
                let secondNum = curPath[curPath.length - 2];
                if (curNum != firstNum + secondNum) break;
                curPath.push(curNum);
                backtracking(num, i + 1);
                curPath.pop();
            }
        }
    }
    backtracking(num, 0);
    console.log("t is", total);
    return total;
};
isAdditiveNumber("199100199");
