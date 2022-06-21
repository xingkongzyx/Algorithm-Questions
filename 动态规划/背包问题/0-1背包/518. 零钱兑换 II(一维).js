var change = function (amount, coins) {
    let dp = new Array(amount + 1).fill(0);
    dp[0] = 1;

    for (let i = 0; i < coins.length; i++) {
        for (let j = coins[i]; j <= amount; j++) {
            dp[j] += dp[j - coins[i]];
        }
    }
    
    return dp[amount];
};
const amount = 5;
const coins = [1, 2, 5];
change(amount, coins);
