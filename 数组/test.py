class Solution:
    def spiralOrder(self, matrix):
        top = 0
        left = 0
        right = len(matrix[0]) - 1
        bottom = len(matrix) - 1

        result = []

        while True:
            for i in range(left, right + 1):
                # print(matrix[top][i])
                result.append(matrix[top][i])
            top += 1
            if top > bottom:
                break
            
            for j in range(top, bottom + 1):
                # print(matrix[j][right])
                result.append(matrix[j][right])
            right -= 1
            
            if left > right:
                break

            for k in range(right, left - 1, -1):
                # print(matrix[bottom][k])
                result.append(matrix[bottom][k])
            bottom -= 1

            if top > bottom:
                break

            for l in range(bottom, top - 1, -1):
                # print(matrix[l][left])
                result.append(matrix[l][left])
            left += 1

            if left > right:
                break
        # print(result)
        return  result

Solution().spiralOrder([[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]])
matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]]
print(matrix[0],"\n", matrix[1], "\n",matrix[2],"\n", matrix[3])
