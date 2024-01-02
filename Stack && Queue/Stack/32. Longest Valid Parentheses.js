/* 
始终保持栈底元素为当前已经遍历过的元素中「最后一个没有被匹配的右括号的下标」，这样的做法主要是考虑了边界条件的处理，栈里其他元素维护左括号的下标
1. 对于遇到的每个 ( ，我们将它的下标放入栈中
2. 对于遇到的每个 ) ，我们先弹出栈顶元素表示匹配了当前右括号：
    如果栈为空，说明当前的右括号为没有被匹配的右括号，我们将其下标放入栈中来更新我们之前提到的「最后一个没有被匹配的右括号的下标」
    如果栈不为空，当前右括号的下标减去栈顶元素即为「以该右括号为结尾的最长有效括号的长度」

需要注意的是，如果一开始栈为空，第一个字符为左括号的时候我们会将其放入栈中，这样就不满足提及的「最后一个没有被匹配的右括号的下标」，为了保持统一，我们在一开始的时候往栈中放入一个值为 −1-1−1 的元素。

? 官方 https://leetcode.cn/problems/longest-valid-parentheses/solutions/314683/zui-chang-you-xiao-gua-hao-by-leetcode-solution/
? 笨猪 https://leetcode.cn/problems/longest-valid-parentheses/solutions/314827/shou-hua-tu-jie-zhan-de-xiang-xi-si-lu-by-hyj8/
*/

const longestValidParentheses = (s) => {
    let maxLen = 0;
    const stack = [];
    stack.push(-1);
    for (let i = 0; i < s.length; i++) {
        const c = s[i];
        if (c == "(") {
            // 左括号的索引，入栈
            stack.push(i);
        } else {
            // 遍历到右括号
            stack.pop(); // 栈顶的左括号被匹配，出栈
            if (stack.length) {
                // 栈未空
                const curMaxLen = i - stack[stack.length - 1]; // 计算有效连续长度
                maxLen = Math.max(maxLen, curMaxLen); // 挑战最大值
            } else {
                // 栈空了
                stack.push(i); // 入栈充当参照
            }
        }
    }
    return maxLen;
};
