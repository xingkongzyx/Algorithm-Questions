class Solution:
    def maximumPopulation(self, logs) -> int:
        arr = []
        for birth, death in logs:
            arr.append((birth, 1))
            arr.append((death, -1))
        arr.sort()
        res = {"population": 0, "year": 0}
        cur = 0
        # print(arr)
        for time, val in arr:
            cur += val

            if cur > res["population"]:
                res["population"] = cur
                res["year"] = time

        return res["year"]
