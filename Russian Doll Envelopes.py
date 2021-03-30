"""
Russian Doll Envelopes

You are given a 2D array of integers envelopes where envelopes[i] = [wi, hi] represents the width and the height of an envelope.
One envelope can fit into another if and only if both the width and height of one envelope is greater than the width and height of the other envelope.
Return the maximum number of envelopes can you Russian doll (i.e., put one inside the other).
Note: You cannot rotate an envelope.

Example 1:

Input: envelopes = [[5,4],[6,4],[6,7],[2,3]]
Output: 3
Explanation: The maximum number of envelopes you can Russian doll is 3 ([2,3] => [5,4] => [6,7]).

Example 2:

Input: envelopes = [[1,1],[1,1],[1,1]]
Output: 1

Constraints:

1 <= envelopes.length <= 5000
envelopes[i].length == 2
1 <= wi, hi <= 10^4
"""

class Solution:
    def maxEnvelopes(self, envelopes: List[List[int]]) -> int:
        if not envelopes:
            return 0
        envelopes.sort(key=lambda x:(x[0], -x[1]))
        vec = [1] * len(envelopes)
        c = 0
        for e in envelopes:
            i, j = 0, c
            while i != j:
                m = (i + j) // 2
                if vec[m] < e[1]:
                    i = m + 1
                else:
                    j = m
            vec[i] = e[1]
            c = max(c, i + 1)
        return c