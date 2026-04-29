class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        dict1 = {}
        dict2 = {}

        for c in s:
            if c in dict1:
                dict1[c] += 1
            else:
                dict1[c] = 1
        for c in t:
            if c in dict2:
                dict2[c] += 1
            else:
                dict2[c] = 1
        print(dict1)
        print(dict2)
        for e in dict1:
            if e in dict2:
                if not dict1[e] == dict2[e]:
                    return False
            else:
                return False
        for e in dict2:
            if e in dict1:
                if not dict1[e] == dict2[e]:
                    return False
            else:
                return False
        return True
        

        