class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        if len(s) <= 1:
            return len(s)

        l = 0
        r = 0
        freq = defaultdict(lambda: 0)
        freq[s[0]] += 1
        ath = 1

        for r in range(1, len(s)):
            freq[s[r]] += 1

            mv, total = self.get_counts(freq)
            diff = total - mv
            if diff > k:
                freq[s[l]] -= 1
                l += 1

            ath = max(ath, r - l + 1)

        return ath

    def get_counts(self, freq):
        max_val = 0
        total = 0

        for k, v in freq.items():
            total += v

            if v > max_val:
                max_val = v

        return max_val, total
