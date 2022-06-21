'''
## 我们可以先采用暴力搜索的办法找到目标字符串 word 中的第一个字符, 找到之后按照深度优先搜索的顺序寻找是否有和 word 匹配的字符串，如果找到直接返回 True; 如果没有，我们继续寻找下一个字符

链接：https://leetcode.cn/problems/ju-zhen-zhong-de-lu-jing-lcof/solution/mian-shi-ti-12-ju-zhen-zhong-de-lu-jing-shen-du-yo/

'''

class Solution(object):
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        totalRows = len(board)
        totalCols = len(board[0])
        def helper(currentX, currentY, wordIdx):
            #/ 递归终止条件: 行或列索引越界、当前矩阵元素与目标字符不同
            if currentX < 0 or currentX >= totalRows or \
                currentY >= totalCols or currentY < 0:
                return False

            if word[wordIdx] != board[currentX][currentY]:
                return False
            
            #/ 递归终止条件:  当前矩阵元素已访问过
            if board[currentX][currentY] == "":
                return False
            
            
            if wordIdx == len(word) - 1:
                return True
            #/ 为了同一个单元格内的字母不允许被重复使用，遍历到某字符后，将当前字符设置为''，防止四个方向dfs再次遍历到这里。最后四个方向遍历完毕后，再恢复这个字符
            tempChar = board[currentX][currentY]
            board[currentX][currentY] = ""

            # 向上进行回溯
            wordIdx += 1
            topCheck = helper(currentX - 1, currentY, wordIdx)
            wordIdx -= 1

            if topCheck == True:
                return True
            
            # 向下进行回溯
            wordIdx += 1
            bottomCheck = helper(currentX + 1, currentY, wordIdx)
            wordIdx -= 1

            if bottomCheck == True:
                return True

            # 向左进行回溯
            wordIdx += 1
            leftCheck = helper(currentX, currentY - 1, wordIdx)
            wordIdx -= 1

            if leftCheck == True:
                return True

            # 向右进行回溯
            wordIdx += 1
            rightCheck = helper(currentX, currentY + 1, wordIdx)
            wordIdx -= 1

            if rightCheck == True:
                return True

            board[currentX][currentY] = tempChar

            return False
        
        for i in range(totalRows):
            for j in range(totalCols):
                totalCheck = helper(i, j, 0)
                if totalCheck == True:
                    return True
        
        return False

board = [["a","a","a","a"],["a","a","a","a"],["a","a","a","a"]]
word = "aaaaaaaaaaaa"
s = Solution()
res = s.exist(board, word)
print(res)