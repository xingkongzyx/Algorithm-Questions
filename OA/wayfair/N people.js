function solution(str, A) {
    let res = [];
    let strIdx = 0,
        peopleIdx = 0;
    while (true) {
        res.push(str[strIdx]);
        let nextPeopleIdx = A[peopleIdx];
        if (nextPeopleIdx === 0) {
            return res.join("");
        }
        peopleIdx = nextPeopleIdx;
        strIdx = peopleIdx;
    }
}
console.log(solution("cdeo", [3, 2, 0, 1]));
console.log(solution("cdeenetpi", [5, 2, 0, 1, 6, 4, 8, 3, 7]));
console.log(solution("bytdag", [4, 3, 0, 1, 2, 5]));
