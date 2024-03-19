/* 
/ 判断1个数是否在一个集合中出现过最好的方式是哈希查找，此处数字比较多而且数字会很大，所以通过string方式来记录，保存为哈希表的key，此处构造的方式是每个数字中间加逗号分割，按行存一次，按列找一次即可。
/ 加逗号是为了避免 [[11,1],[1,11]] 这种数字相同的情况

? 时间复杂度：O(n^2)，将行放入哈希表中消耗 O(n^2)，读所有列的哈希表中的次数也消耗 O(n^2)。
*/
var equalPairs = function (grid) {
    let rowFrequency = {};
    let numRows = grid.length;
    let numCols = grid[0].length;

    // 统计每个行字符串的频率
    for (let i = 0; i < numRows; i++) {
        let currentRow = grid[i].join(",");
        rowFrequency[currentRow] =
            (rowFrequency[currentRow] || 0) + 1;
    }

    let equalPairsCount = 0;
    // 遍历列，寻找与行字符串匹配的列
    for (let col = 0; col < numCols; col++) {
        let colArr = [];
        for (let row = 0; row < numRows; row++) {
            colArr.push(grid[row][col]);
        }
        let columnRepresentation = colArr.join(",");
        equalPairsCount += rowFrequency[columnRepresentation] || 0;
    }

    return equalPairsCount;
};
