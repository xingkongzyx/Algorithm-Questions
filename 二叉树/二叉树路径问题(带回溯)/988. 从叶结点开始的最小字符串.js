/**
 * @param {TreeNode} root
 * @return {string}
 */
var smallestFromLeaf = function (root) {
    const currentPath = [intToChar(root.val)];
    let result = "";
    function traverse(node) {
        if (!node.left && !node.right) {
            let currentStr = currentPath.slice().reverse().join("");
            if (result == "") {
                result = currentStr;
            } else if (currentStr.localeCompare(result) < 0) {
                //* 如果 currentStr 出现在 result 前面
                result = currentStr;
            }
            return;
        }

        if (node.left) {
            currentPath.push(intToChar(node.left.val));
            traverse(node.left);
            currentPath.pop();
        }

        if (node.right) {
            currentPath.push(intToChar(node.right.val));
            traverse(node.right);
            currentPath.pop();
        }
    }

    traverse(root);
    return result;
};

function intToChar(int) {
    const code = "a".charCodeAt(0);
    return String.fromCharCode(code + int);
}

/* 
let root = new TreeNode("a");
let n1 = new TreeNode("b");
let n2 = new TreeNode("c");
let n3 = new TreeNode("d");
let n4 = new TreeNode("e");
let n5 = new TreeNode("d");
let n6 = new TreeNode("e");

root.left = n1;
root.right = n2;
n1.left = n3;
n1.right = n4;
n2.left = n5;
n2.right = n6;

console.log(smallestFromLeaf(root));
 */
