var canAttendMeetings = function (intervals) {
    if (intervals.length == 0) return true;
    //* 将区间按照会议开始时间实现升序排序
    intervals.sort((a, b) => a[0] - b[0]);
    let endTime = intervals[0][1];
    //* 遍历会议，如果下一个会议在前一个会议结束之前就开始了，返回 false。
    for (let i = 1; i < intervals.length; i++) {
        if (intervals[i][0] < endTime) {
            return false;
        } else {
            endTime = intervals[i][1];
        }
    }
    return true;
};
