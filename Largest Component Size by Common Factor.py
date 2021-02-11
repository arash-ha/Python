"""
Largest Component Size by Common Factor
Given a non-empty array of unique positive integers A, consider the following graph:

There are A.length nodes, labelled A[0] to A[A.length - 1];
There is an edge between A[i] and A[j] if and only if A[i] and A[j] share a common factor greater than 1.
Return the size of the largest connected component in the graph.

 

Example 1:

Input: [4,6,15,35]
Output: 4

Example 2:

Input: [20,50,9,63]
Output: 2

Example 3:

Input: [2,3,6,7,4,12,21,39]
Output: 8

Note:

1 <= A.length <= 20000
1 <= A[i] <= 100000

"""


class Solution:
    def largestComponentSize(self, A: List[int]) -> int:
        parent = [-1]*100001
        def _find (x):
            if parent[x] == -1:
                return x
            parent[x] = _find(parent[x])
            return parent[x]

        def _union(x, y):
            xp = _find(x)
            yp = _find(y)
            if xp != yp:
                parent[yp] = xp
        for x in A:
            for i in range(2, int(sqrt(x)) + 1):
                if x % i == 0:
                    _union(i, x)
                    _union(x, x//i)

        count = 0;
        ump = {}
        for x in A:
            xp = _find(x)
            count = max(count, 1 + ump.get(xp, 0))
            ump[xp] = 1 + ump.get(xp, 0)
        return count