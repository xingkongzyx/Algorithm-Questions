/* 
* 不能忘了扫描过的左括号，它们等着被匹配，用一个容器暂存——为什么是栈？
* 
* 当遇到右括号时，我们期待它匹配「最近出现的左括号」，于是容器中的「最近出现的左括号」不用等待匹配了，可以离开容器。它是「后进」的，现在「先出」，所以是栈。
* 像“对对碰”，匹配了就拿掉，如果最后清空了栈，则有效。如果栈中还剩左括号未匹配，则无效
/ 时间复杂度：O(n)，因为我们一次只遍历给定的字符串中的一个字符并在栈上进行 O(1) 的推入和弹出操作。
/ 空间复杂度：O(n)，当我们将所有的开括号都推到栈上时以及在最糟糕的情况下，我们最终要把所有括号推到栈上。
? https://leetcode.cn/problems/valid-parentheses/solution/wei-shi-yao-xu-yao-zhan-er-bu-shi-qi-ta-by-hyj8/
*/
const isValid = (s) => {
    const stack = [];

    for (let i = 0; i < s.length; i++) {
        const c = s[i];
        if (c == "{" || c == "[" || c == "(") {
            //* 若为左括号，则往栈中存放
            stack.push(c);
        } else {
            //* 若为右括号，如果 栈为空 或者 该右括号与取出的栈顶元素不一样，则返回false
            if (stack.length == 0) {
                //* 此时栈空，无法匹配，返回 false
                return false;
            }

            const top = stack[stack.length - 1];

            //* 如果栈顶是对应的左括号，被匹配，出栈
            if (
                (top == "(" && c == ")") ||
                (top == "[" && c == "]") ||
                (top == "{" && c == "}")
            ) {
                stack.pop();
            } else {
                //* 不是对应的左括号，无法匹配，返回 false
                return false;
            }
        }
    }
    return stack.length == 0; // 栈空，则所有左括号找到匹配；栈中还剩有左括号，则没被匹配
};
