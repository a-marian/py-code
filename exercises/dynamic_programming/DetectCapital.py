"""
520. Detect Capital
We define the usage of capitals in a word to be right when one of the following cases holds:
All letters in this word are capitals, like "USA".
All letters in this word are not capitals, like "leetcode".
Only the first letter in this word is capital, like "Google".
Given a string word, return true if the usage of capitals in it is right.
Example 2:
    Input: word = "FlaG"
    Output: false
https://leetcode.com/problems/detect-capital/description/
"""
class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        if word[0].isupper() and word[1:len(word)].islower():
            return True
        if word.isupper():
            return True
        if word.islower():
            return True
        return False

    def detectCapitalUseV2(self, w: str) -> bool:
        return w.isupper() or w.islower() or w.istitle()
