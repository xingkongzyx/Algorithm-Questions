""" 
* 当前行星是大于 0 的(代表向右移动), 无论栈顶元素是向左移动的还是向右移动的, 都不会相撞, 直接入栈
* 当前行星是小于 0 的(代表向左移动)
*     若栈为空, 直接入栈
*     若栈顶元素小于 0, 直接入栈
*     若栈顶元素大于 0:
*         若栈顶元素与当前行星绝对值相同, 全部爆炸；
*         若栈顶元素绝对值大于当前行星, 当前行星爆炸；
*         若栈顶元素绝对值小于当前行星, 栈顶元素爆炸, 接着判断下一个行星
? https://leetcode.cn/problems/asteroid-collision/solution/xingxing-by-jiang-hui-4-tepq/    
"""


class Solution:
    def asteroidCollision(self, asteroids):
        stack = []

        for aster in asteroids:
            if aster > 0:
                stack.append(aster)
            else:
                isAlive = True

                while isAlive == True and stack and stack[-1] > 0:
                    isAlive = stack[-1] < abs(aster)
                    if stack[-1] <= abs(aster):
                        stack.pop()

                if isAlive:
                    stack.append(aster)

        return stack


Solution().asteroidCollision([-2, -1, 1, 2])
