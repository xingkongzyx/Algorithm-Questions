var lemonadeChange = function (bills) {
    let remaining = { 5: 0, 10: 0, 20: 0 };

    for (let bill of bills) {
        if (bill === 5) {
            remaining[bill] += 1;
        } else if (bill === 10) {
            remaining[bill]++;
            remaining[5]--;

            if (remaining[5] < 0) return false;
        } else {
            remaining[bill]++;

            if (remaining[10] > 0) {
                remaining[10]--;
                bill -= 10;
            }

            //# 前面有$10则还需要1张$5，前面没有$10找零则现在需要3张$5
            let numOfFiveDollars = (bill - 5) / 5;
            if (remaining[5] < numOfFiveDollars) return false;

            remaining[5] -= numOfFiveDollars;
        }
    }

    return true;
};
let res = lemonadeChange([5, 5, 5, 5, 10, 5, 10, 10, 10, 20]);
console.log(res);
