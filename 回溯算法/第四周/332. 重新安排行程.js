const findItinerary = (tickets) => {
    const result = ["JFK"]; // 初始放入起点'JFK'
    const map = {}; // 邻接表

    for (const ticket of tickets) {
        // 遍历tickets，建表
        const [fromCity, toCity] = ticket; // 每一张机票，读出起点和终点
        if (!map[fromCity]) {
            map[fromCity] = []; // 初始化
        }
        map[fromCity].push(toCity); // 建立映射
    }

    for (const city in map) {
        // 按照字母顺序，小的在前
        map[city].sort();
    }

    function backtracking() {
        // * 我们回溯遍历的过程中，遇到的机场个数，如果达到了（航班数量+1），那么我们就找到了一个行程，把所有航班串在一起了。
        if (result.length === tickets.length + 1) {
            // 用光了所有机票，路径找到了
            return true;
        }

        // 获取下一站能去的城市list
        const nextCitiesList = map[result[result.length - 1]];
        // 没有邻接城市了
        if (!nextCitiesList || !nextCitiesList.length) {
            // 还没用光机票，就没有下一站了，返回false
            return false;
        }
        for (let i = 0; i < nextCitiesList.length; i++) {
            const nextCity = nextCitiesList[i]; // 当前选择的下一站
            //! 再说一下为什么一定要增删元素呢，出发机场和到达机场是会重复的，搜索的过程没及时删除目的机场就会死循环。
            // 飞出地的list中删掉这一站, 防止死循环
            nextCitiesList.splice(i, 1);
            // 将该选择推入res
            result.push(nextCity);
            // 在该递归分支中能找到一个用完所有机票的路径
            if (backtracking()) {
                return true;
            }
            // 回溯过程: 将删掉的这一站重新插回去, 并且将推入res的选择也撤销
            result.pop();
            nextCitiesList.splice(i, 0, nextCity);
        }
    }
    backtracking();
    return result;
};
