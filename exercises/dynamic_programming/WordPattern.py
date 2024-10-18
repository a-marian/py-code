"""
290. Word Pattern
Given a pattern and a string s, find if s follows the same pattern.
Here follow means a full match, such that there is a bijection
between a letter in pattern and a non-empty word in s.
Example 1:
 Input: pattern = "abba", s = "dog cat cat dog"
 Output: true
https://leetcode.com/problems/word-pattern/description/
"""
class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        sarray = s.split()
        return (len(set(pattern)) == len(set(sarray)) == len(set(zip_longest(pattern, sarray))))
