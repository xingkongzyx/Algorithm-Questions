// 时间复杂度：遍历所有节点，最坏的情况去到 O(4^n)，n 为数字串的长度。
// 空间复杂度：O(n)，递归栈调用的深度。
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

    //* 参数index是记录遍历到digits中第几个数字了，同时index也表示树的深度。
    function helper(numMap, digits, index) {
        //! 当指针越界时，此时生成了一个解，加入解集，结束当前递归，去别的分支，找齐所有的解。
        if (index === digits.length) {
            results.push(currentPath.join(""));
            return;
        }

        let digitNum = digits[index];
        let digitChars = numMap[digitNum];

        for (let i = 0; i < digitChars.length; i++) {
            currentPath.push(digitChars[i]);
            helper(numMap, digits, index + 1); //* 递归，注意index+1，代表要处理下一个数字了
            currentPath.pop();
        }
    }
    helper(numMap, digits, 0);
    return results;
};

let digits = "23";
console.log(letterCombinations(digits));
