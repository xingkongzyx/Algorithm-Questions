//* https://leetcode-cn.com/problems/the-number-of-full-rounds-you-have-played/solution/ni-wan-cheng-de-wan-zheng-dui-ju-shu-by-df44r/
var numberOfRounds = function (loginTime, logoutTime) {
    let loginTimeInMinutes = convertToMinutes(loginTime);
    let logoutTimeInMinutes = convertToMinutes(logoutTime);
    /// 如果转换后的 loginTimeInMinutes > logoutTimeInMinutes, 这说明finishTime 在第二天(通宵的情况)，此时我们需要将 logoutTimeInMinutes​ 加上一天对应的分钟数，即 24*60
    if (loginTimeInMinutes > logoutTimeInMinutes) {
        logoutTimeInMinutes += 24 * 60;
    }
    /// 为了计算区间内完整对局的个数，我们将结束时间转为结束时间之前最近的一个时间
    /// 例如 12:01 - 12:14 这里就变成了 12:01 - 12:00 或者 12:01-12:31 - 12:01-12:30
    logoutTimeInMinutes = Math.floor(logoutTimeInMinutes / 15) * 15;
    /// 12:01 - 12:00 这种情况下 logoutTimeInMinutes < loginTimeInMinutes, 也就是说没有对局，直接返回0
    if (logoutTimeInMinutes <= loginTimeInMinutes) return 0;
    /// 12:01-12:30 的情况下 30-1 = 29，29/15 再向下取整则能得到正确的对局数
    return Math.floor(
        (logoutTimeInMinutes - loginTimeInMinutes) / 15
    );
};

function convertToMinutes(time) {
    let hour = parseInt(time.split(":")[0]);
    let minute = parseInt(time.split(":")[1]);

    return hour * 60 + minute;
}

console.log(numberOfRounds("20:00", "06:00"));
