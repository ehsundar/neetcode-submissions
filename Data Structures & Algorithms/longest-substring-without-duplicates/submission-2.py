class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) == 0:
            return 0
        if len(s) == 1:
            return 1

        max_len = 0

        l = 0
        m = {s[0]: 0}

        for i in range(1, len(s)):
            ch = s[i]
            print(ch, m)
            if ch in m:
                max_len = max(max_len, len(m))

                while s[l] != ch:
                    del m[s[l]]
                    l += 1

                l += 1

            m[ch] = i

        return max(max_len, len(m))
