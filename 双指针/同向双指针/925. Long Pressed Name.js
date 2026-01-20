/* 
第一个解法必须在循环后处理 `typed` 剩余字符的原因：

## 循环条件决定了退出时机

**第一个解法的循环条件**（第5行）：`while (namePointer < name.length)`
- 当 `namePointer === name.length` 时循环就结束了
- 此时 `name` 已经完全匹配，但 **`typed` 可能还有剩余字符**

## 为什么会有剩余字符？

假设 `name = "alex"`, `typed = "aaleexx"`：

1. 循环过程：
   - `a` 匹配 `a`：`namePointer = 1`, `typedPointer = 1`
   - `a`（重复）：`typedPointer = 2`
   - `l` 匹配 `l`：`namePointer = 2`, `typedPointer = 3`
   - `e` 匹配 `e`：`namePointer = 3`, `typedPointer = 4`
   - `e`（重复）：`typedPointer = 5`
   - `x` 匹配 `x`：`namePointer = 4`, `typedPointer = 6`

2. **循环结束**：`namePointer === 4`（等于 `name.length`）
   - 此时 `typedPointer = 6`，但 `typed.length = 7`
   - 还剩一个字符 `x`（第7个字符，索引6）

## 剩余字符只能是最后一个字符的重复

第21-26行的处理：
```javascript
while (
    typedPointer < typed.length &&
    typed[typedPointer] === name[name.length - 1]
) {
    typedPointer++;
}
```

- **允许**：剩余字符是 `name` 最后一个字符的重复（长按）
- **不允许**：剩余字符是其他字符

## 举例对比

**场景1：`name = "alex"`, `typed = "aaleexx"` ✓**
- 循环结束：`namePointer = 4`, `typedPointer = 6`
- 剩余：`typed[6] = 'x'` 等于 `name[3] = 'x'`（最后一个字符）
- 第21-26行处理后：`typedPointer = 7`
- 返回：`7 === 7` → `true`

**场景2：`name = "alex"`, `typed = "aaleexb"` ✗**
- 循环结束：`namePointer = 4`, `typedPointer = 6`
- 剩余：`typed[6] = 'b'` 不等于 `name[3] = 'x'`
- 第21-26行循环不执行
- 返回：`6 === 7` → `false`

## 为什么第二个解法不需要？

[`isLongPressedName2()`](925.\ Long\ Pressed\ Name.js:31) 循环条件是 `while (typedPointer < typed.length)`：
- 循环会**处理完所有 `typed` 字符**
- 不会留下剩余字符需要额外处理
- 直接用 `namePointer === name.length` 验证即可

## 总结

第一个解法以 `name` 为主循环，循环退出时只保证了 `name` 遍历完，但 `typed` 可能还有剩余字符。这些剩余字符只有是最后一个字符的长按重复才合法，所以必须用第21-26行额外验证。
*/
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
在 [`isLongPressedName2()`](925.\ Long\ Pressed\ Name.js:31) 解法中，遍历 `typed` 不用额外考虑 `namePointer` 是否遍历完的原因：

## 核心设计思路

**以 `typed` 为主循环**，循环保证了处理完所有输入字符，而 `name` 是否完全匹配则通过**最后的检查**来验证。

## 为什么不需要在循环中检查？

1. **循环条件**（第35行）：`while (typedPointer < typed.length)`
   - 只要 `typed` 有字符就继续处理
   - `namePointer` 会在匹配时自然推进（第36-41行）

2. **三种情况覆盖所有场景**：
   - **字符匹配**（第36-41行）：两个指针都前进
   - **长按重复**（第42-46行）：当前 `typed` 字符与前一个相同，允许重复
   - **其他情况**（第48行）：非法输入，直接返回 `false`

3. **最后统一验证**（第52行）：`return namePointer === name.length`
   - 如果 `namePointer < name.length`：说明 `name` 还有字符未匹配，返回 `false`
   - 如果 `namePointer === name.length`：说明 `name` 完全匹配，返回 `true`

## 举例说明

**场景1：`name = "alex"`, `typed = "al"`**
- 循环结束时：`namePointer = 2`，`typedPointer = 2`
- 返回：`2 === 4` → `false` ✓（`name` 未完全匹配）

**场景2：`name = "alex"`, `typed = "aaleex"`**
- 循环结束时：`namePointer = 4`，`typedPointer = 6`
- 返回：`4 === 4` → `true` ✓（`name` 完全匹配）

## 与第一个解法的对比

[`isLongPressedName()`](925.\ Long\ Pressed\ Name.js:1) 以 `name` 为主循环，必须：
- 在循环内检查 `typedPointer >= typed.length`（第7行）
- 循环后处理 `typed` 剩余字符（第21-26行）

[`isLongPressedName2()`](925.\ Long\ Pressed\ Name.js:31) 以 `typed` 为主循环，逻辑更简洁：
- 无需在循环内检查 `namePointer` 边界
- 用最后一行代码统一验证 `name` 是否完全匹配

这种设计将"name 是否遍历完"的检查推迟到循环结束后，避免了边界条件的重复判断。
*/
var isLongPressedName2 = function (name, typed) {
    let namePointer = 0,
        typedPointer = 0;

    while (typedPointer < typed.length) {
        if (
            namePointer < name.length &&
            name[namePointer] === typed[typedPointer]
        ) {
            namePointer++;
            typedPointer++;
        } else if (
            typedPointer > 0 &&
            typed[typedPointer] === typed[typedPointer - 1]
        ) {
            typedPointer++; // 长按：重复上一个 typed 字符
        } else {
            return false;
        }
    }

    return namePointer === name.length;
};
