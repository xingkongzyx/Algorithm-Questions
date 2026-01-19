/* 
? https://leetcode.cn/problems/backspace-string-compare/solutions/683776/shuang-zhi-zhen-bi-jiao-han-tui-ge-de-zi-8fn8/
*/
var backspaceCompare = function (S, T) {
    // 设置两个指针的位置，分别指向字符串的末尾
    // skipS、skipT 用来记录还需要跳过（删除）的字符次数
    let sPointer = S.length - 1;
    let tPointer = T.length - 1;
    let skipS = 0;
    let skipT = 0;

    // 进入主循环
    // 只要任意一个字符串还没遍历完，就继续比较
    while (sPointer >= 0 || tPointer >= 0) {
        // =====================
        // 处理字符串 S
        // =====================
        // i 从后向前寻找下一个「有效字符」
        while (sPointer >= 0) {
            // 如果遇到 '#'
            // 说明后面的一个字符需要被删除，跳过次数 +1
            if (S[sPointer] === "#") {
                skipS++;
                sPointer--;
            }
            // 如果当前字符不是 '#'
            // 但仍然有跳过次数，说明该字符会被之前的 '#' 删除
            else if (skipS > 0) {
                skipS--;
                sPointer--;
            }
            // 当前字符是可以参与比较的有效字符
            else {
                break;
            }
        }

        // =====================
        // 处理字符串 T
        // =====================
        // j 从后向前寻找下一个「有效字符」
        while (tPointer >= 0) {
            if (T[tPointer] === "#") {
                skipT++;
                tPointer--;
            } else if (skipT > 0) {
                skipT--;
                tPointer--;
            } else {
                break;
            }
        }

        // =====================
        // 比较当前找到的有效字符
        // =====================
        // 如果 i 和 j 都没有越界，直接比较字符是否相等
        if (sPointer >= 0 && tPointer >= 0) {
            // 若不相等，说明两个字符串最终结果不同
            if (S[sPointer] !== T[tPointer]) {
                return false;
            }
        }
        // 走到这里说明：
        // 要么 i 越界了，要么 j 越界了，或者两个都越界了
        else {
            // 如果只有一个越界，另一个还存在有效字符
            // 说明长度或内容不一致
            if (sPointer >= 0 || tPointer >= 0) {
                return false;
            }
        }

        // 当前字符已经比较完成，指针继续向前移动
        sPointer--;
        tPointer--;
    }

    // 所有有效字符都比较完，且全部相等
    return true;
};
