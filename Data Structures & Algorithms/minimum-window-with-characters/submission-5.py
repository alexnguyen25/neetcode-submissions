class Solution:
    def minWindow(self, s: str, t: str) -> str:
        charsT = defaultdict(int)
        window = defaultdict(int)

        for i in t:
            charsT[i] += 1
        
        have = 0
        need = len(charsT)

        l = 0
        length = float("inf")
        lenarray = [-1, -1]
        for r in range(len(s)):
            window[s[r]] += 1
            
            if s[r] in charsT and window[s[r]] == charsT[s[r]]:
                have += 1
            
            while have == need:
                if (r - l + 1) < length:
                    length = r - l + 1
                    lenarray[0], lenarray[1] = l, r
                
                window[s[l]] -= 1
                
                if s[l] in charsT and window[s[l]] < charsT[s[l]]:
                    have -= 1
                
                l += 1
            
        l, r = lenarray
        return s[l:r+1] if length != float("inf") else ""

                    
        