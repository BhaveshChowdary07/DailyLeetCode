class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if len(s)!=len(t):
            return False
        # for i in s:
        #     if i not in t:
        #         return False
        # return True
        c1 = Counter(s)
        c2 = Counter(t)
        for i in s:
            if c1[i] != c2[i]:
                return False
        return True