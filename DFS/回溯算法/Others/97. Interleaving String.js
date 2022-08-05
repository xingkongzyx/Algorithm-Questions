/* 
? https://leetcode.cn/problems/interleaving-string/solution/shou-hua-tu-jie-dfshui-su-dfsji-yi-hua-by-hyj8/
? https://leetcode.cn/problems/interleaving-string/solution/cong-san-zhi-zhen-hui-su-dao-ji-yi-hua-di-gui-zai-/

/ 时间复杂度：O(2^k)，k为s3的长度
/ 空间复杂度：O(1)，暂不考虑递归栈使用的空间
 */
const isInterleave = (s1, s2, s3) => {
    //* 对于 s1 = a, s2 = b, s3 = a 这种情况应该返回false, 因为没有所谓的交替的情况
    if (s1.length + s2.length !== s3.length) return false;

    //* p1 是用于递归遍历 s1 的指针, p2 是用于递归遍历 s2 的指针, p3 是用于递归遍历 s3 的指针
    function backtracking(p1, p2, p3) {
        //* 递归终止条件, p3越界, 说明s3扫描完了, 返回true
        if (p3 === s3.length) {
            return true;
        }
        let isValid = false;
        //* 如果 p1 指针没有越界, 且 s1[p1] 和 s3[p3] 相同
        if (p1 < s1.length && s1[p1] === s3[p3]) {
            p1++;
            p3++;
            isValid = backtracking(p1, p2, p3);
            p1--;
            p3--;
        }
        //* 如果 p2 指针没有越界, 且 s2[p2] 和 s3[p3] 相同
        if (p2 < s2.length && s2[p2] === s3[p3]) {
            p2++;
            p3++;
            /* 
            # 为什么这里使用 "isValid || backtracking()"?
            * 如果 p1, p2, p3 指向相同的字符, 在第一个判断中, 也是满足条件的, 所以会先经历上面的递归以及递归后的回溯操作, 此时 isValid 「可能」已经是 true。如果它已经为 true, 说明已经找到了一条满足题目的路线, 就不用再检查 p2, p3 右移的递归结果, 如果是false, 则执行递归, 检查这条路线
            */
            isValid = isValid || backtracking(p1, p2, p3);
            p2--;
            p3--;
        }
        return isValid;
    }
    return backtracking(0, 0, 0);
};
