// https://leetcode-cn.com/problems/ti-huan-kong-ge-lcof/solution/tu-jie-guan-fang-tui-jian-ti-jie-ti-huan-3l74/

// ! 为什么要从后向前填充，从前向后填充不行么？
// ? 从前向后填充就是O(n^2)的算法了，因为每次添加元素都要将添加元素之后的所有元素向后移动。
// ?这么做有两个好处：
// ? 1) 不用申请新数组。像下面的代码我们依旧使用原数组，只是从right pointer 开始把 原来的元素复制过去。
// ? 2) 避免了从前向后填充元素时每次添加元素都要将添加元素之后的所有元素向后移动。

var replaceSpace = function (s) {
    let strInArr = s.split("");
    let oldLen = strInArr.length;
    let space = 0;
    for (let char of strInArr) {
        if (char == " ") space += 1;
    }
    if (space === 0) return s;

    let newLen = oldLen + space * 2;
    //* 因为index是从0起始的, 所以 left, right pointers 的起始位置都是 length-1
    //* right比left领先的几个spaces 都是每个 " " 替换为 "%20" 多出来的位置，当左右指针相遇则说明所有 spaces 已经处理完毕。
    let left = oldLen - 1;
    let right = newLen - 1;
    while (left < right) {
        if (strInArr[left] !== " ") {
            strInArr[right] = strInArr[left];
            left--;
            right--;
        } else {
            strInArr[right] = "0";
            strInArr[right - 1] = "2";
            strInArr[right - 2] = "%";
            left--;
            right -= 3;
        }
    }

    return strInArr.join("");
};

let s = "We are happy.";
console.log(replaceSpace(s));
