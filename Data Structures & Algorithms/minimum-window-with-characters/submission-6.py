class Solution:
    def minWindow(self, s: str, t: str) -> str:
        charsT = defaultdict(int)
        window = defaultdict(int)

        for i in t:
            charsT[i] += 1
        have = 0
        need = len(charsT)

        lenarray = [-1, -1]
        length = float('inf')
        
        l = 0
        for r in range(len(s)):
            window[s[r]] += 1

            if s[r] in charsT and window[s[r]] == charsT[s[r]]:
                have += 1
            
            while have == need:
                window[s[l]] -= 1

                if r - l + 1 < length:
                    length = r - l + 1
                    lenarray = [l, r]

                if s[l] in charsT and window[s[l]] < charsT[s[l]]:
                    have -= 1
                
                l += 1
        
        l, r = lenarray
        if length == float('inf'):
            return ""
        else:
            return s[l:r+1]


