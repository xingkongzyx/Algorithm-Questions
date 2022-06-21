var replaceSpace = function (s) {
    let times = 0;
    for (let char of s) {
        if (char === " ") times++;
    }

    let res = new Array(s.length + 2 * times);
    let j = 0;
    for (let i = 0; i < s.length; i++) {
        if (s[i] !== " ") {
            res[j] = s[i];
            j++;
        } else {
            res[j] = "%";
            res[j + 1] = "2";
            res[j + 2] = "0";
            j += 3;
        }
    }
    // console.log(res.join(""));
    return res.join("");
};

let s = "We are happy.";
replaceSpace(s);
