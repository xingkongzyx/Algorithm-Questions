/* 
https://leetcode.cn/problems/reverse-nodes-in-k-group/solutions/10416/tu-jie-kge-yi-zu-fan-zhuan-lian-biao-by-user7208t/

下面用一个**完整的指针移动图**来一步一步解释 `reverseKGroup` 的过程。看懂这张流程图，这题基本就完全掌握了。🙂

示例：

```
1 → 2 → 3 → 4 → 5 → 6
k = 3
```

---

# 一、初始化

创建一个 **dummy 虚拟头节点**：

```
dummy → 1 → 2 → 3 → 4 → 5 → 6
```

指针：

```
pre  = dummy
end  = dummy
```

图示：

```
pre,end
   ↓
dummy → 1 → 2 → 3 → 4 → 5 → 6
```

---

# 二、寻找第一组 k 个节点

循环移动 `end` **k 次**

```
for i < k
end = end.next
```

移动过程：

```
step1
dummy → 1 → 2 → 3 → 4 → 5 → 6
        ↑
       end

step2
dummy → 1 → 2 → 3 → 4 → 5 → 6
            ↑
           end

step3
dummy → 1 → 2 → 3 → 4 → 5 → 6
                ↑
               end
```

此时：

```
start = pre.next = 1
end = 3
next = end.next = 4
```

结构：

```
dummy → 1 → 2 → 3 → 4 → 5 → 6
        ↑       ↑
      start     end
```

---

# 三、断开当前这一组

执行

```
end.next = null
```

链表变成：

```
dummy → 1 → 2 → 3      4 → 5 → 6
        ↑
      start
```

第一段独立出来：

```
1 → 2 → 3
```

---

# 四、翻转这一段

调用

```
reverse(start)
```

翻转：

```
1 → 2 → 3
```

变成

```
3 → 2 → 1
```

返回 `3`

---

# 五、重新接回原链表

### 第一步

```
pre.next = reversedHead
```

变成：

```
dummy → 3 → 2 → 1
```

### 第二步

```
start.next = next
```

因为 `start` 已经变成尾节点

```
dummy → 3 → 2 → 1 → 4 → 5 → 6
```

---

# 六、移动指针准备下一组

```
pre = start
end = pre
```

状态：

```
dummy → 3 → 2 → 1 → 4 → 5 → 6
                    ↑
                   pre,end
```

---

# 七、处理第二组

再次寻找 k 个节点：

```
4 → 5 → 6
```

翻转：

```
6 → 5 → 4
```

接回：

```
dummy → 3 → 2 → 1 → 6 → 5 → 4
```

---

# 八、最终结果

```
3 → 2 → 1 → 6 → 5 → 4
```

---

# 九、核心指针作用总结

| 指针    | 作用           |
| ----- | ------------ |
| dummy | 防止头节点被翻转后丢失  |
| pre   | 每一组翻转前的前一个节点 |
| end   | 找到每一组的尾节点    |
| start | 当前组的头节点      |
| next  | 下一组的起点       |

---

# 十、整题最关键的 5 行

真正的核心逻辑只有这几行：

```javascript
end.next = null;          // 断开
pre.next = reverse(start) // 翻转并接回
start.next = next         // 接回后半部分
pre = start               // 移动 pre
end = pre                 // 重置 end
```

---

如果你愿意，我可以再给你讲一个 **90% 面试者都没真正理解的关键技巧：为什么一定要 `end.next = null` 才能反转成功**。
这个点其实是这题最容易卡住的地方。



*/

/**
 * Definition for singly-linked list.
 * function ListNode(val, next) {
 *     this.val = (val === undefined ? 0 : val);
 *     this.next = (next === undefined ? null : next);
 * }
 */

/**
 * 每 k 个节点翻转一次链表
 * @param {ListNode} head
 * @param {number} k
 * @return {ListNode}
 */
var reverseKGroup = function (head, k) {
    // 创建虚拟头节点，方便处理头节点被翻转的情况
    let dummy = new ListNode(0);
    dummy.next = head;

    // pre 指向每一组翻转前的前一个节点
    let pre = dummy;

    // end 用来寻找每一组的尾节点
    let end = dummy;

    while (end.next !== null) {
        // 移动 end 指针，找到当前这组的第 k 个节点
        for (let i = 0; i < k && end !== null; i++) {
            end = end.next;
        }

        // 如果不足 k 个节点，直接结束
        if (end === null) break;

        // 当前这一组的开始节点
        let start = pre.next;

        // 下一组的起点
        let next = end.next;

        // 先断开当前这一组，方便单独反转
        end.next = null;

        // pre -> 反转后的头节点
        pre.next = reverse(start);

        // 反转后 start 变成尾节点
        // 把尾节点接回下一组
        start.next = next;

        // pre 移动到当前组的尾节点（也就是 start）
        pre = start;

        // end 重新回到 pre，准备找下一组
        end = pre;
    }

    return dummy.next;
};

/**
 * 反转链表
 * @param {ListNode} head
 * @return {ListNode}
 */
function reverse(head) {
    let pre = null;
    let curr = head;

    while (curr !== null) {
        let next = curr.next; // 暂存下一个节点
        curr.next = pre; // 反转指针
        pre = curr; // pre 向前移动
        curr = next; // curr 向前移动
    }

    // 返回新的头节点
    return pre;
}
