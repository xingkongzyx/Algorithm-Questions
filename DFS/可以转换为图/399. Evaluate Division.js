/* 
DFS 中的难题
思路讲解 https://leetcode.cn/problems/evaluate-division/solutions/512094/dfsxiang-jie-pou-xi-guo-cheng-qi-shi-hen-aqin
代码来自讲解下的评论区
*/
var calcEquation = function (equations, values, queries) {
    const record = {};

    for (let i = 0; i < equations.length; i++) {
        const [charA, charB] = equations[i];
        if (!(charA in record)) {
            record[charA] = [];
        }

        if (!(charB in record)) {
            record[charB] = [];
        }

        record[charA].push([charB, values[i]]);
        record[charB].push([charA, 1 / values[i]]);
    }

    // Initialize a set to keep track of visited variables during the DFS
    const visited = new Set();
    // Initialize a boolean flag to track if a path from query source to target is found
    let nonFound = true;
    // Initialize an array to store the results of the queries
    const result = [];
    // Iterate through each query

    for (let [val1, val2] of queries) {
        // If either val1 or val2 is not in the record, push -1.0 to result and continue to the next query
        if (!(val1 in record) || !(val2 in record)) {
            result.push(-1.0);
            continue;
        }

        visited.add(val1);
        // Start DFS from val1 to val2 with initial path result of 1
        dfs(val1, val2, 1);
        visited.delete(val1);

        // If no path from val1 to val2 is found, push -1.0 to result
        if (nonFound) {
            result.push(-1.0);
        }
        // Reset nonFound flag for the next query
        nonFound = true;
    }

    // Depth-first search function to find a path from source to target variable
    function dfs(curChar, target, curPathRes) {
        // If a path from source to target is already found, return
        if (!nonFound) {
            return;
        }

        // If the current character is the target, push the current path result to the result array
        if (curChar === target) {
            result.push(curPathRes);
            // Set nonFound to false since a path from source to target is found
            nonFound = false;
            return;
        }

        // Iterate through all variables connected to the current variable
        for (let [connectedChar, connectedCharWeight] of record[
            curChar
        ]) {
            // If the connected variable is not visited, visit it and continue DFS
            if (!visited.has(connectedChar)) {
                visited.add(connectedChar);
                dfs(
                    connectedChar,
                    target,
                    curPathRes * connectedCharWeight
                );
                visited.delete(connectedChar);
            }
        }
    }

    return result;
};
