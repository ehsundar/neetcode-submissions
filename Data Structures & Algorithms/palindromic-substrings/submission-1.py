class Solution:
    def countSubstrings(self, s: str) -> int:
        res = 0

        for i in range(len(s)):
            res += self.palin_center(s, i)

        return res

    def palin_center(self, s, center):
        #res = []
        cnt = 0

        # odd
        max_r = min(center, len(s) - center - 1)
        for r in range(max_r + 1):
            if s[center - r] == s[center + r]:
                #res.append(s[center - r : center + r + 1])
                cnt += 1
            else:
                break

        # even
        max_r = min(center, len(s) - center - 2)
        for r in range(max_r + 1):
            if s[center - r] == s[center + r + 1]:
                #res.append(s[center - r : center + r + 2])
                cnt += 1
            else:
                break

        # return res
        return cnt
