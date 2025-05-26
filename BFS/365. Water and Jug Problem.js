/*
* 这道题由于就是要找到一个符合题意的状态，我们用广搜就好了。这是因为广搜有个性质，一层一层像水波纹一样扩散，路径最短。所谓「状态」，就是指当前的任务进行到哪个阶段了，可以用变量来表示，怎么定义状态有的时候需要一定技巧，这道题不难。这里分别定义两个水壶为 A 和 B，定义有序整数对 (a, b) 表示当前 A 和 B 两个水壶的水量，它就是一个状态。

? https://leetcode.cn/problems/water-and-jug-problem/solutions/161837/tu-de-yan-du-you-xian-bian-li-by-liweiwei1419/

* 每次操作不外乎6种情况，y加满水 / y排空水 / x加满水 / x排空水 / y倒入x中 / x倒入y中：
* 所以使用bfs模拟6种倒水的操作: 
* 将水壶1的水倒满；
* 将水壶1的水清空；
* 将水壶2的水倒满；
* 将水壶2的水清空；
* 将水壶1的水倒入水壶2中，知道水壶2满了或者水壶1没水了就停止倒；
* 将水壶2的水倒入水壶1中，知道水壶1满了或者水壶2没水了就停止倒；


? https://leetcode.cn/problems/water-and-jug-problem/solutions/161623/tu-jie-bfs-c-jie-zhu-unordered_set-queue-shi-xian-/
? https://leetcode.cn/problems/water-and-jug-problem/solutions/162004/365shui-hu-wen-ti-bfsdfsdi-gui-dfszhan-bei-zu-ding
 * 
/ 状态空间大小为 (x + 1) * (y + 1)（因为两个水壶的水量范围是 0 ~ x / 0 ~ y）
/ 每个状态最多尝试 6 种操作。
/ BFS 最多遍历 (x + 1)(y + 1) 个状态。
/ 时间复杂度： O(x * y)
/ 空间复杂度： O(x * y)（visited 集合最多存储这么多状态
 */
var canMeasureWater = function (x, y, target) {
    // 使用 Set 存储已经访问过的状态，避免重复计算（状态为 "x,y" 字符串）
    let visited = new Set();

    // 初始化队列，起始状态为两个水壶都为空
    const queue = [[0, 0]];
    visited.add([0, 0].join(",")); // 初始状态加入 visited

    // 判断当前水量是否满足目标
    function meetRequirement(curX, curY) {
        // 只要两个水壶中任意组合的水量等于目标即可
        return curX + curY === target;
    }

    // BFS 主循环
    while (queue.length) {
        let queueLen = queue.length;

        // 遍历当前层的所有状态
        for (let index = 0; index < queueLen; index++) {
            let [curX, curY] = queue.shift(); // 当前状态

            // 以下是所有可能的操作：

            // 1. 把水壶1灌满
            let [newX, newY] = [x, curY];
            if (meetRequirement(newX, newY)) return true;
            let newCapStr = [newX, newY].join(",");
            if (!visited.has(newCapStr)) {
                visited.add(newCapStr);
                queue.push([newX, newY]);
            }

            // 2. 把水壶2灌满
            [newX, newY] = [curX, y];
            if (meetRequirement(newX, newY)) return true;
            newCapStr = [newX, newY].join(",");
            if (!visited.has(newCapStr)) {
                visited.add(newCapStr);
                queue.push([newX, newY]);
            }

            // 3. 把水壶1倒空
            [newX, newY] = [0, curY];
            if (meetRequirement(newX, newY)) return true;
            newCapStr = [newX, newY].join(",");
            if (!visited.has(newCapStr)) {
                visited.add(newCapStr);
                queue.push([newX, newY]);
            }

            // 4. 把水壶2倒空
            [newX, newY] = [curX, 0];
            if (meetRequirement(newX, newY)) return true;
            newCapStr = [newX, newY].join(",");
            if (!visited.has(newCapStr)) {
                visited.add(newCapStr);
                queue.push([newX, newY]);
            }

            // 5. 把水壶1的水倒入水壶2（直到水壶1空或水壶2满）
            newX = curX;
            newY = curY;
            while (newX > 0 && newY < y) {
                newX--;
                newY++;
            }
            if (meetRequirement(newX, newY)) return true;
            newCapStr = [newX, newY].join(",");
            if (!visited.has(newCapStr)) {
                visited.add(newCapStr);
                queue.push([newX, newY]);
            }

            // 6. 把水壶2的水倒入水壶1（直到水壶2空或水壶1满）
            newX = curX;
            newY = curY;
            while (newX < x && newY > 0) {
                newX++;
                newY--;
            }
            if (meetRequirement(newX, newY)) return true;
            newCapStr = [newX, newY].join(",");
            if (!visited.has(newCapStr)) {
                visited.add(newCapStr);
                queue.push([newX, newY]);
            }
        }
    }

    // 所有状态遍历完仍未找到解，返回 false
    return false;
};

let res = canMeasureWater(1, 2, 3);

console.log("🚀 ~ res:", res);
