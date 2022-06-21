var removeDuplicates = function (s) {
    let stack = [];
    for (let char of s) {
        if (stack[stack.length - 1] !== char) {
            stack.push(char);
        } else {
            stack.pop();
        }
    }
    return stack.join("");
};

let res = removeDuplicates("abbaca");
console.log(res);
