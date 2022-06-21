function solution(arr) {
    if (astheticTrees(arr)) return 0;
    let result = 0;
    //* 将每个元素都尝试从arr中移除，然后看剩下的元素是否满足 asthetic 的要求
    for (let i = 0; i < arr.length - 1; i++) {
        let tempArr = arr.slice();
        //* 移除下标为i的元素，看剩下的元素是否满足要求
        tempArr.splice(i, 1);
        if (astheticTrees(tempArr)) {
            result++;
        }
    }
    if (result === 0) return -1;
    return result;
}
function astheticTrees(arr) {
    for (let i = 1; i < arr.length - 1; i++) {
        if (arr[i] >= arr[i - 1] && arr[i] <= arr[i + 1])
            return false;
        if (arr[i] <= arr[i - 1] && arr[i] >= arr[i + 1])
            return false;
    }
    return true;
}

// console.log(solution([3, 4, 5, 3, 7]));
// console.log(solution([1, 2, 3, 4]));
console.log(solution([2, 4, 2, 2, 7, 6, 8]));
