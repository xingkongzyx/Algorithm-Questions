/* 
这段代码实现的是 **快速幂（Exponentiation by Squaring）**，它通过把指数不断 **折半** 来减少计算次数。

我们重点看递归函数：

```js
function helper(num, pow)
```

每一次递归都会做一件事：

```
pow → pow / 2
```

例如：

```
pow = 16
→ 8
→ 4
→ 2
→ 1
→ 0
```

指数每次 **减半**，直到 0 或 1。

---

## 递归层数

假设 `n = pow`

递归深度为：

[
\log_2 n
]

例如：

| n    | 递归层数 |
| ---- | ---- |
| 16   | 4    |
| 32   | 5    |
| 1024 | 10   |

因为：

```
n → n/2 → n/4 → n/8 → ...
```

---

## 每一层的工作量

每一层只做 **常数操作**：

```js
halfPowRes * halfPowRes
```

或

```js
num * halfPowRes * halfPowRes
```

都是 **O(1)**。

---

## 总时间复杂度

递归层数 × 每层工作量

[
O(\log n) \times O(1) = O(\log n)
]

所以：

**时间复杂度**

```
O(log n)
```

---

## 空间复杂度

由于使用递归，调用栈深度是：

```
log n
```

因此：

```
空间复杂度 = O(log n)
```

如果改写成 **迭代版快速幂**，空间复杂度可以变成：

```
O(1)
```

---

## 为什么比普通方法快

普通方法：

```
x^n = x * x * x * ... (n 次)
```

时间复杂度：

```
O(n)
```

快速幂：

```
x^16
= (x^8)^2
= ((x^4)^2)^2
= ...
```

只需要：

```
log₂ n 次
```

例如：

| n    | 普通乘法   | 快速幂  |
| ---- | ------ | ---- |
| 1024 | 1024 次 | 10 次 |
| 1e9  | 1e9 次  | 30 次 |

---

✅ **总结**

| 项目    | 复杂度               |
| ----- | ----------------- |
| 时间复杂度 | **O(log n)**      |
| 空间复杂度 | **O(log n)**（递归栈） |

---

https://leetcode.cn/problems/powx-n/solutions/2858114/tu-jie-yi-zhang-tu-miao-dong-kuai-su-mi-ykp3i/
*/
var myPow = function (x, n) {
    if (n < 0) {
        x = 1 / x;
    }

    n = Math.abs(n);
    return helper(x, n);
};

function helper(num, pow) {
    if (pow === 0) return 1;
    if (pow === 1) return num;

    let halfPow = Math.floor(pow / 2);
    let halfPowRes = helper(num, halfPow);
    let res = 1;
    if (pow % 2 === 1) {
        res = num * halfPowRes * halfPowRes;
    } else {
        res = halfPowRes * halfPowRes;
    }
    return res;
}
