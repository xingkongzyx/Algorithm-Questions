var isSubsequence = function (s, t) {
    if (s.length === 0) return true;
    let p1 = 0;
    let p2 = 0;
    while (p1 < s.length && p2 < t.length) {
        if (s[p1] === t[p2]) {
            p1++;
            p2++;
        } else {
            p2++;
        }
    }
    return p1 === s.length;
};
const s = "axc",
    t = "ahbgdc";
let res = isSubsequence(s, t);
console.log(res);
