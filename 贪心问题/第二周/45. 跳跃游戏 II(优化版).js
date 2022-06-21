var jump = function (nums) {
    if (nums.length <= 1) return 0;

    let maxCover = 0;
    let steps = 0;
    let end = 0;
    //* 这里有个小细节，因为是起跳的时候就 + 1 了，如果最后一次跳跃刚好到达了最后一个位置，那么遍历到最后一个位置的时候就会再次起跳，这是不允许的，因此不能遍历最后一个位置
    for (let i = 0; i < nums.length - 1; i++) {
        maxCover = Math.max(maxCover, i + nums[i]);
        //* 第一次起跳 或 到达跳跃的边界
        if (i === end) {
            //* 再次起跳
            steps++;
            //* 更新边界
            end = maxCover;
        }
    }

    return steps;
};
