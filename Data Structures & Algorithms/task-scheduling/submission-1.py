class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        freq = defaultdict(lambda: 0)
        for t in tasks:
            freq[t] += 1

        max_freq = 0
        max_freq_count = 0
        for t, f in freq.items():
            if f == max_freq:
                max_freq_count += 1
            elif f > max_freq:
                max_freq = f
                max_freq_count = 1

        return max((n + 1) * (max_freq - 1) + max_freq_count, len(tasks))
