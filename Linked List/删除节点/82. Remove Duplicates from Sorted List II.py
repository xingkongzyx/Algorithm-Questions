""" 
**核心思路**

因为链表是有序的，所以重复值一定是连续出现的。

代码使用三个指针：

```text
dummy -> 虚拟头节点，方便删除真正头节点
pre   -> 已确认保留下来的链表尾部
cur   -> 当前正在检查的节点
```

初始状态：

```text
dummy -> head
pre = dummy
cur = head
```

遍历时分两种情况：

1. `cur.val != cur.next.val`

说明当前节点没有和下一个节点重复，可以保留。

```python
pre = cur
cur = cur.next
```

2. `cur.val == cur.next.val`

说明遇到重复段，需要一直跳过所有相同值。

```python
while cur and cur.next and cur.val == cur.next.val:
    cur = cur.next
```

循环结束后，`cur` 停在重复段的最后一个节点。

然后让：

```python
pre.next = cur.next
cur = cur.next
```

这样整段重复节点就被跳过了。

---

**流程图**

```mermaid
flowchart TD
    A["开始"] --> B["创建 dummy，dummy.next = head"]
    B --> C["pre = dummy，cur = head"]
    C --> D{"cur 和 cur.next 是否存在？"}

    D -- 否 --> Z["返回 dummy.next"]
    D -- 是 --> E{"cur.val 是否等于 cur.next.val？"}

    E -- 否 --> F["当前节点不重复，可以保留"]
    F --> G["pre = cur"]
    G --> H["cur = cur.next"]
    H --> D

    E -- 是 --> I["发现重复值"]
    I --> J{"cur、cur.next 存在且值相等？"}
    J -- 是 --> K["cur = cur.next，继续跳过重复节点"]
    K --> J

    J -- 否 --> L["cur 停在重复段最后一个节点"]
    L --> M["pre.next = cur.next，删除整段重复节点"]
    M --> N["cur = cur.next，继续遍历"]
    N --> D
```

---

**举例走一遍**

链表：

```text
1 -> 2 -> 3 -> 3 -> 4 -> 4 -> 5
```

初始：

```text
dummy -> 1 -> 2 -> 3 -> 3 -> 4 -> 4 -> 5
pre = dummy
cur = 1
```

`1` 和 `2` 不同，保留 `1`：

```text
pre = 1
cur = 2
```

`2` 和 `3` 不同，保留 `2`：

```text
pre = 2
cur = 3
```

`3` 和下一个 `3` 相同，进入跳过重复段：

```text
cur 从第一个 3 移动到第二个 3
```

此时 `cur.next` 是 `4`，值不同，说明所有 `3` 已经跳完。

执行：

```python
pre.next = cur.next
```

也就是：

```text
2.next = 4
```

链表变成：

```text
dummy -> 1 -> 2 -> 4 -> 4 -> 5
```

继续检查 `4`，发现重复，同理删除整段 `4`：

```text
dummy -> 1 -> 2 -> 5
```

最后返回：

```python
dummy.next
```

结果是：

```text
1 -> 2 -> 5
```

---

**为什么需要 dummy？**

如果重复节点出现在链表开头，比如：

```text
1 -> 1 -> 2 -> 3
```

真正的头节点 `1` 需要被删除。

如果没有 `dummy`，删除头节点会比较麻烦；有了虚拟头节点，就可以统一使用：

```python
pre.next = cur.next
```

不管重复段在开头、中间还是结尾，都能用同一种方式处理。

---


复杂度分析

- 时间复杂度: O(n), 其中 n 是链表的长度, 只对链表进行了一次遍历。
- 空间复杂度: O(1), 只使用了常数级别的额外空间（`dummy`, `pre`, `cur` 等指针变量）。
"""
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # 创建虚拟头结点, 其 next 指向真正的头结点
        dummy = ListNode(0, head)

        # pre 指针指向当前已处理链表的最后一个结点
        pre = dummy

        # cur 指针用于遍历
        cur = head

        while cur and cur.next:
            # 如果当前结点和下一个结点值不同, pre 和 cur 都可以后移
            if cur.val != cur.next.val:
                pre = cur
                cur = cur.next
            else:
                # 如果相同, 需要找到下一个不同值的结点
                # 用循环跳过所有重复的结点
                while cur and cur.next and cur.val == cur.next.val:
                    cur = cur.next

                # 此时 cur 是重复段的最后一个结点, cur.next 是下一个不同值的结点
                # 让 pre 的 next 直接指向下一个不同值的结点, 完成对整段重复结点的删除
                pre.next = cur.next

                # cur 指针后移, 继续遍历
                cur = cur.next

        # 返回虚拟头结点的 next, 即新链表的头
        return dummy.next