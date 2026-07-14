class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # time complexity : O(nlogn)

        # if sorted(list(s)) == sorted(list(t)):
        #     return True
        # else:
        #     return False

        # time complexity : O(n)

        # edge case
        if len(s) != len(t):
            return False

        # count number of characters in s
        dict_s = {}
        for c in s:
            if c in dict_s:
                dict_s[c] += 1
            else:
                dict_s[c] = 1
        
        # count number of characters in t
        dict_t = {}
        for c in t:
            if c in dict_t:
                dict_t[c] += 1
            else:
                dict_t[c] = 1
        
        # compare the characters and count in both the dictionaries

        for key,value in dict_s.items():
            if key not in dict_t:
                return False
            if dict_s[key] != dict_t[key]:
                return False
        
        return True







        