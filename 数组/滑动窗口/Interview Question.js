function solution(s1, s2, delay) {
    let s1Length = s1.length;
    let s2Length = s2.length;
    let set = new Set();
    // # j 是用来遍历s1下标
    let j = 0;
    let result = [];

    // # i 是用来遍历s2下标
    for (let i = 0; i < s2Length; i++) {
        console.log(`当前遍历到的 s2 i ${i}, value is ${s2[i]}`);

        // # 下标大于d说明窗口已经满了，需要删除最老的一个数据
        if (i > delay) {
            console.log(
                `当前位置的 ${s1[i - 1 - delay]} 已超出目前 s2=${
                    s2[i]
                } 的delay 范围`
            );
            set.delete(s1[i - 1 - delay]);
        }

        while (Math.abs(i - j) <= delay && j < s1Length) {
            console.log(`s1 中的 j 在范围内, 添加 ${s1[j]}`);
            set.add(s1[j]);
            j++;
        }
        console.log(
            `当前遍历到的 s1 j index is ${j}, value is ${s1[j]}`
        );
        console.log("当前 set is ", set);
        // # 当前s2元素在滑动窗口内
        if (set.has(s2[i])) {
            console.log(
                `当前s2元素 ${s2[i]} 在滑动窗口内, 添加进最终结果`
            );
            result.push(s2[i]);
        }
        console.log("----------------\n");
    }

    return result;
}

// 测试代码
let s = solution([3, 5, 7, 1, 6, 2], [7, 1, 2, 6, 10, 11], 3);
console.log(s);
