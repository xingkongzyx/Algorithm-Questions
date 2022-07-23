/* 
! 本题每一个数字代表的是「不同集合」，也就是求「不同集合」之间的组合
/ 时间复杂度：遍历所有节点, 最坏的情况去到 O(4^n), n 为数字串的长度。
/ 空间复杂度：O(n), 递归栈调用的深度。
*/

var letterCombinations = function (digits) {
    let numMap = {
        2: "abc",
        3: "def",
        4: "ghi",
        5: "jkl",
        6: "mno",
        7: "pqrs",
        8: "tuv",
        9: "wxyz",
    };

    const results = [];
    let currentPath = [];

    //* 参数 index 是用于记录当前遍历到 digits 中的第几位数字, 代表的是树的深度。
    function helper(numMap, digits, index) {
        //! 当指针越界时, 此时生成了一个解, 加入解集, 结束当前递归, 去别的分支, 找齐所有的解。
        if (index === digits.length) {
            results.push(currentPath.join(""));
            return;
        }

        let digitNum = digits[index];
        let digitChars = numMap[digitNum];

        //! 这里的 for循环，不是从 startIdx 开始遍历的
        for (let i = 0; i < digitChars.length; i++) {
            currentPath.push(digitChars[i]);
            //* 递归, 注意这里传入的是「index + 1」而不是像一般组合问题中的「i + 1」, 「index + 1」代表要处理「下一个数字」而不是当前数字对应的「下一个letter」。这里的 index 代表的是遍历的深度
            helper(numMap, digits, index + 1);
            currentPath.pop();
        }
    }
    helper(numMap, digits, 0);
    return results;
};

let digits = "23";
console.log(letterCombinations(digits));
