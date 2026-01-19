var isLongPressedName = function (name, typed) {
    let namePointer = 0;
    let typedPointer = 0;

    while (namePointer < name.length) {
        // name 还没有遍历完成，但是 typedPointer 已经完成了，代表匹配失败
        if (typedPointer >= typed.length) return false;

        if (typed[typedPointer] === name[namePointer]) {
            typedPointer++;
            namePointer++;
        } else {
            if (namePointer === 0) return false;
            if (name[namePointer - 1] !== typed[typedPointer])
                return false;
            typedPointer++;
        }
    }

    // ⭐ 关键：name 匹配完后，typed 剩下的只能是 name 最后一个字符的重复
    while (
        typedPointer < typed.length &&
        typed[typedPointer] === name[name.length - 1]
    ) {
        typedPointer++;
    }

    return typedPointer === typed.length;
};
/* 
更稳的经典写法（推荐）- 这个写法天然覆盖“尾巴长按”的场景：
## 🔥 为什么你原来的写法必须“额外处理尾巴”？

你的循环是：

```js
while (namePointer < name.length) { ... }
```

这意味着：

* 一旦 `name` 用完
* **循环立刻结束**
* 根本不给 `typed` 机会继续“长按”

所以你只能在循环后**手动补一段逻辑**。

---

## 总结一句话（记住这个）

> **只要循环条件是 `typed` 驱动（`j < typed.length`），
> 尾巴长按就一定会被当成普通的“重复字符”自然吃掉。**

这就是为什么它“天然覆盖”。

---
*/
var isLongPressedName = function (name, typed) {
    let i = 0,
        j = 0;

    while (j < typed.length) {
        if (i < name.length && name[i] === typed[j]) {
            i++;
            j++;
        } else if (j > 0 && typed[j] === typed[j - 1]) {
            j++; // 长按：重复上一个 typed 字符
        } else {
            return false;
        }
    }

    return i === name.length;
};
