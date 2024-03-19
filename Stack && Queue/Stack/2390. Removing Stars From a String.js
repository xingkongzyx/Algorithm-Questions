var removeStars = function (s) {
    let stack = [];

    for (let char of s) {
        if (char !== "*") {
            stack.push(char);
        } else {
            if (stack.length === 0) continue;
            stack.pop();
        }
    }
    return stack.join("");
};
