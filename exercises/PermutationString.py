class Solution:
    def checkInclusion(self, s1:str, s2:str)-> bool:
        len1 = len(s1)
        len2 = len(s2)
        if(len1 > len2):
            return False
        arr1 = [0]*26
        arr2 = [0]* 26
        for ch in s1:
            arr1[ord(ch)-ord('a')] += 1
        for i in range(len2):
            arr2[ord(s2[i]) - ord('a')] += 1
            if i >= len1:
                arr2[ord(s2[i-n1]) - ord('a')] -= 1
            if arr1 == arr2:
                return True
        return False
