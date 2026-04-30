class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        freq_s = defaultdict(lambda: 0)
        for ch in s:
            freq_s[ch] += 1
        
        for ch in t:
            freq_s[ch] -= 1
            if freq_s[ch] < 0:
                return False
        
        for f in freq_s.values():
            if f != 0:
                return False
        
        return True
        