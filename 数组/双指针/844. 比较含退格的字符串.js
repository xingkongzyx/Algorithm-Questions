// 可以理解的双指针
// https://leetcode-cn.com/problems/backspace-string-compare/solution/shuang-zhi-zhen-fa-si-lu-jian-dan-rong-y-bmn6/

var backspaceCompare = function (s, t) {
    const s_array = s.split("");
    // 其中的slow就代表即将插入正确字符的位置
    let slow = 0;
    let traversePointer = 0;
    // 之所以要有slow > 0就是为了处理backspaceCompare("y#fo##f", "y#f#o##f")的情况
    // 如果#数量过多slow回退到0后就不能继续回退了
    for (; traversePointer < s_array.length; traversePointer++) {
        if (s_array[traversePointer] !== "#") {
            s_array[slow] = s_array[traversePointer];
            slow++;
        } else if (s_array[traversePointer] === "#" && slow > 0) {
            // // 之所以要有slow > 0就是为了处理"y###f"的情况,如果有多个#,slow退到index 0就不能继续回退了
            slow -= 1;
        }
    }

    let sWithoutSymbol = s_array.slice(0, slow).join("");

    const t_array = t.split("");
    slow = 0;
    traversePointer = 0;
    for (; traversePointer < t_array.length; traversePointer++) {
        if (t_array[traversePointer] !== "#") {
            t_array[slow] = t_array[traversePointer];
            slow++;
        } else if (t_array[traversePointer] === "#" && slow > 0) {
            slow -= 1;
        }
    }

    let tWithoutSymbol = t_array.slice(0, slow).join("");
    return sWithoutSymbol === tWithoutSymbol;
};

let res = backspaceCompare("y#fo##f", "y#f#o##f");
console.log(res);
