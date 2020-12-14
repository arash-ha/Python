"""
Palindrome Partitioning

Given a string s, partition s such that every substring of the partition is a palindrome. Return all possible palindrome partitioning of s.

A palindrome string is a string that reads the same backward as forward.

 

Example 1:

Input: s = "aab"
Output: [["a","a","b"],["aa","b"]]
Example 2:

Input: s = "a"
Output: [["a"]]
 

Constraints:

1 <= s.length <= 16
s contains only lowercase English letters.
"""

class Solution:
    def partition(self, s: str) -> List[List[str]]:
        def backtrack(start, end, temp):
            if start == end:
                res.append(temp[:])
            for i in range(start, end):
                cur = s[start: i+1]
                if cur == cur[::-1]:
                    temp.append(cur)
                    backtrack(i+1, end, temp)
                    temp.pop()
        res = []
        backtrack(0, len(s), [])
        return res