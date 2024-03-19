/* 
应该贪心地挑选按照投票顺序的下一名夜魇方的议员。这也是很容易形象化地证明的：既然只能挑选一名夜魇方的议员，那么就应该挑最早可以进行投票的那一名议员；如果挑选了其他较晚投票的议员，那么等到最早可以进行投票的那一名议员行使权利时，一名天辉方议员就会丧失权利，这样就得不偿失了。
例如 [R, D, R, D] 第一个 R 挑选最近的 D 罢免投票权可以避免第二个 R 的损失。

? 链接：https://leetcode.cn/problems/dota2-senate/solutions/517088/dota2-can-yi-yuan-by-leetcode-solution-jb7l/
? 视频: https://www.youtube.com/watch?v=zZA5KskfMuQ
*/
var predictPartyVictory = function (senate) {
    let rQueue = [];
    let dQueue = [];

    for (let i = 0; i < senate.length; i++) {
        if (senate[i] === "R") {
            rQueue.push(i);
        } else {
            dQueue.push(i);
        }
    }
    while (rQueue.length > 0 && dQueue.length > 0) {
        let topR = rQueue.shift();
        let topD = dQueue.shift();
        // +n的原因是可以保证当前轮次之后的轮次中议员投票的相对顺序保持不变，我们需要的只是议员的相对投票次序，而不需要绝对准确的投票时间； 因此，取+n和取+10n、+100n的结果都是正确的。 如果增加的时间小于n，可能会出现一个议员执行在一轮中执行多次权利或者本该后执行却先执行的情况。
        if (topR < topD) {
            rQueue.push(topR + senate.length);
        } else {
            dQueue.push(topD + senate.length);
        }
    }

    return dQueue.length > 0 ? "Dire" : "Radiant";
};
