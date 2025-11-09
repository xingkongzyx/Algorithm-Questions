/* 
# 思想是什么

* 在先序序列里, ｢#｣ 表示空指针；而任何非 ｢#｣ 的结点一旦它的左右孩子都读到了（不管是值还是 ｢#｣）, 这个｢三件套｣模式：[node, "#", "#"] 就构成了一个完整子树, 整棵子树在更高层看来等价于一个 "已经填满的空位", 所以可以折叠为一个 ｢#｣。
* 反复折叠, 若最终能把整串序列折叠成唯一的一个 ｢#｣, 说明这是一棵合法的二叉树的序列化；否则就是非法。

* 规则为什么正确：局部正确 ⟶ 全局正确
* - 前序串里, # 表示空指针。
* - ｢非 # 节点 + 两个 #｣ 正对应着 ｢一棵叶子节点的完整前序序列｣：root, #, #。
* - 把  ｢root, #, #｣ 折叠为一个 #, 等价于“从父视角看, 这个位置已经被一棵完整子树填满了, 因此对更高层而言, 它就像一个占位完成的空位”。
* - 更一般地, ｢root, left-subtree, right-subtree｣ 只要左右子树最终都各自能折叠为 #, 就又能折叠成 #。于是自底向上不断折叠, 最后若是合法整棵树, 就会变成一个 #。

? 时间：每个元素最多进栈一次、出栈至多一次, O(n)。
? 空间：最坏情况下（例如全是数字还没等到 #）, 栈可达 O(n)；平均/常见情况会不断折叠而更小。
*/

var isValidSerialization = function (preorder) {
    const preArr = preorder.split(",");
    const stack = [];

    for (let i = 0; i < preArr.length; i++) {
        stack.push(preArr[i]);

        while (
            stack.length >= 3 &&
            stack[stack.length - 3] !== "#" &&
            stack[stack.length - 2] === "#" &&
            stack[stack.length - 1] === "#"
        ) {
            stack.pop();
            stack.pop();
            stack.pop();
            stack.push("#");
        }
    }

    return stack.length === 1 && stack[0] === "#";
};
