class Solution(object):
    def compareVersion(self, version1, version2):
        """
        :type version1: str
        :type version2: str
        :rtype: int
        """
        s1 = version1.split('.')
        s2 = version2.split('.')
        n = max(len(s1),len(s2))
        for i in range(n):
            v1 = int(s1[i]) if i < len(s1) else 0
            v2 = int(s2[i]) if i < len(s2) else 0
            if v1 < v2:
                return -1
            elif v1 > v2:
                return 1
        return 0