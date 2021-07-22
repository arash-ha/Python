"""
Push Dominoes

There are n dominoes in a line, and we place each domino vertically upright. In the beginning, we simultaneously push some of the dominoes either to the left or to the right.
After each second, each domino that is falling to the left pushes the adjacent domino on the left. Similarly, the dominoes falling to the right push their adjacent dominoes standing on the right.
When a vertical domino has dominoes falling on it from both sides, it stays still due to the balance of the forces.
For the purposes of this question, we will consider that a falling domino expends no additional force to a falling or already fallen domino.
You are given a string dominoes representing the initial state where:
dominoes[i] = 'L', if the ith domino has been pushed to the left,
dominoes[i] = 'R', if the ith domino has been pushed to the right, and
dominoes[i] = '.', if the ith domino has not been pushed.
Return a string representing the final state.

Example 1:

Input: dominoes = "RR.L"
Output: "RR.L"
Explanation: The first domino expends no additional force on the second domino.

Example 2:

Input: dominoes = ".L.R...LR..L.."
Output: "LL.RR.LLRRLL.."
 
Constraints:

n == dominoes.length
1 <= n <= 10^5
dominoes[i] is either 'L', 'R', or '.'.
"""

class Solution:
    def pushDominoes(self, dominoes: str) -> str:
        d = 'L' + dominoes + 'R'
        res = ""
        l, r, m = 0, 1, len(d)
        while r < m:
            if d[r] == '.':
                r += 1
                continue;
            if l > 0:
                res += d[l]
            mid = r - l - 1
            if d[r] == d[l]:
                res += d[l] * mid
            elif d[r] == 'R':
                res += '.' * mid
            else:
                res += 'R' * (mid // 2) + '.' * (mid % 2) + 'L' * (mid // 2)
            l = r
            r += 1

        return res