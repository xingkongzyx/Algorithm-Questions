var fib = function (n) {
    const dp = new Array(n + 1);
    dp[0] = 0;
    dp[1] = 1;

    for (let i = 2; i <= n; i++) {
        dp[i] = dp[i - 1] + dp[i - 2];
    }

    return dp[n];
};

var fib_solution2 = function (n) {
    if (n <= 1) return n;
    const dp = new Array(2);
    dp[0] = 0;
    dp[1] = 1;

    for (let i = 2; i <= n; i++) {
        let sum = dp[0] + dp[1];
        dp[0] = dp[1];
        dp[1] = sum;
    }

    return dp[1];
};

console.log(fib_solution2(4));
