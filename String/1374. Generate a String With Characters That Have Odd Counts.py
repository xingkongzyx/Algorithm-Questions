""" 
* If n is odd, return a string of "a.....a" of length n.
* If n is even, return a string on 「(n-1) * a」 and 「(1) * b」. result string 应该是: "a.....ab"
* RUNTIME COMPLEXITY: O(N)
* SPACE COMPLEXITY: O(N)
"""


class Solution:
    def generateTheString(self, n: int) -> str:
        if n % 2 == 1:
            return "a" * n
        else:
            return "a" * (n - 1) + "b"
