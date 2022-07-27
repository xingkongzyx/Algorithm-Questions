//? 思路来源: https://leetcode.cn/problems/reconstruct-itinerary/solution/shou-hua-tu-jie-liang-chong-jie-fa-zui-ji-ben-de-h/
//? python 解法: https://leetcode.cn/problems/reconstruct-itinerary/solution/pythonhui-su-suan-fa-ji-bai-9523-by-yun-yi-hen/
//! 这道题中递归函数是「有返回值」的, 当找到一个「合理的行程」, 因为前面的sort 操作, 所以这个行程也是「按字典排序的最小的行程组合」, 此时我们就直接返回 true。这样下面递归的过程中避免在已经找到一条「合理的行程」的前提下仍旧继续进行 DFS 搜索, 造成对当前正确的 result 的修改
const findItinerary = (tickets) => {
    const result = ["JFK"]; // 初始放入起点'JFK'
    const map = {}; // 邻接表

    for (const ticket of tickets) {
        //* 遍历tickets, 建表
        const [fromCity, toCity] = ticket; // 每一张机票, 读出起点和终点
        if (!map[fromCity]) {
            map[fromCity] = []; // 初始化
        }
        map[fromCity].push(toCity); // 建立映射
    }

    for (const city in map) {
        //* 按照字母顺序, 小的在前
        map[city].sort();
    }

    function backtracking(startCity) {
        //# 重要的知识点: 如果有 n 张机票, 那么正确的路径的长度一定是 n+1。
        //* 搜索终止条件：回溯遍历的过程中, result 中储存的路径的个数, 如果达到了「机票数量 + 1」, 那么我们就找到了一个行程, 把所有航班串在一起了。

        if (result.length === tickets.length + 1) {
            //* 用光了所有机票, 路径找到了
            return true;
        }

        //* 获取下一站能去的城市list
        const nextCitiesList = map[startCity];
        //* ➀ startCity 没有对应的邻接城市 或者 ➁ 还没用光机票, startCity 就没有可以飞的下一站了; 这两种情况都直接返回false
        if (!nextCitiesList || !nextCitiesList.length) {
            return false;
        }
        for (let i = 0; i < nextCitiesList.length; i++) {
            const nextCity = nextCitiesList[i]; // 当前选择的下一站
            //! 再说一下为什么一定要增删元素呢? 因为「出发机场」和「到达机场」是会出现重复的, 搜索的过程没及时删除目的机场就会〖死循环〗。
            //* 飞出地的list中删掉这一站, 防止死循环
            nextCitiesList.splice(i, 1);
            //* 将该选择推入 result
            result.push(nextCity);
            //* 在该递归分支中能找到一个用完所有机票的路径
            if (backtracking(nextCity)) {
                return true;
            }
            //# 回溯过程: 将删掉的这一站重新插回去, 并且将推入res的选择也撤销
            result.pop();
            nextCitiesList.splice(i, 0, nextCity);
        }
    }
    backtracking("JFK");
    return result;
};
