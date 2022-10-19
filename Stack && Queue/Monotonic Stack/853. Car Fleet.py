""" 
* 我们首先对这些车辆按照它们的「起始位置」『升序』排序, 并且用 "(target - position) / speed" 计算出每辆车在不受其余车的影响时, 行驶到终点需要的时间。对于相邻的两辆车 S 和 F, F 的起始位置大于 S, 如果 S 行驶到终点需要的时间「小于等于」 F, 那么 S 一定会在终点前追上 F 并形成车队。这是因为在追上 F 之前, S 的行驶速度并不会减小, 而 F 却有可能因为追上前面的车辆而速度减小, 因此 S 总能在终点前追上 F。
# 排序之后这道题就变成了寻找「下一个更大的元素」, 只不过不是记录更大的元素是哪个, 而是与更大的元素形成车队
* 排序之后使用「单调递减栈」存储各个车辆到达终点的所需的时间, 我们顺序扫描这些车辆(此时的车辆是根据其起始位置升序排序的)。如果相邻的两辆车, 前者(位置更远离终点的车辆)「行驶到终点需要的时间」「小于等于」后者(位置更靠近终点的车辆), 那么前者可以追上后者, 他们组成一个车队, 此时从栈中弹出前者到达终点的时间, 因为前者后者在追上后可以一起到达终点, 记录一个即可。并继续检查栈中更靠前的车辆到达终点所需的时间, 看其是否能继续与刚才的后者继续组成车队。最后栈中剩余元素的数量就是车队的数量
! 使用单调栈的关键原因: If a car is slower then previous, all the previous faster car will bump into this car and become a fleet.

/ time complexity: O(NlogN +N) Time, Sort + Mono Stack
? 非常好的解释: https://leetcode.com/problems/car-fleet/discuss/1108723/C%2B%2B-Detailed-Explained!-Sort-%2B-Monotonic-Stack.
"""


class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        import math
        numCars = len(position)
        cars = []
        for i in range(numCars):
            curPosition = position[i]
            curSpeed = speed[i]
            timeToTarget = math.ceil(target - curPosition) / curSpeed
            cars.append([curPosition, timeToTarget])

        cars.sort()
        stack = []

        for pos, time in cars:
            # * 注意: 前后两辆车到达终点的时间相同也能合并成一个车队.
            while stack and stack[-1] <= time:
                stack.pop()
            stack.append(time)

        return len(stack)
