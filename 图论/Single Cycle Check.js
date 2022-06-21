function hasSingleCycle(array) {
    let numElementsVisited = 0;

    let currentIdx = 0;
    while (numElementsVisited < array.length) {
        if (numElementsVisited > 0 && currentIdx === 0) return false;

        numElementsVisited++;

        currentIdx = getNextIdx(currentIdx, array);
    }

    return currentIdx === 0;
}
function getNextIdx(currentIdx, array) {
    const jump = array[currentIdx];

    const nextIdx = (currentIdx + jump) % array.length;
    //! 注意这里与python解法的区别. python中，mod操作的结果跟随除数一个符号，在这里由于除数是正数，python code中计算的nextIdx无论如何都会是正数. python中 -26 % 5 = 4，用的公式是 -x % y == -(x % y) + y
    //! 相当于计算的nextIdx 我们可以直接返回，而不用再加上 array.length 了
    //! 而javasvript 不同，-26 % 5 =-1。-1 + 5(5是除数) 才能得到与 python中一样的结果
    return nextIdx >= 0 ? nextIdx : nextIdx + array.length;
}
