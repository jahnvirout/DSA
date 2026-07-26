class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        n = len(s)
        ans = 0

        for i in range(n):
            counter = Counter()
            for j in range(i,n):
                counter[s[j]] +=1
                window_length = j - i + 1
                max_freq = max(counter.values())

                if window_length - max_freq <= k:
                    ans = max(ans, window_length)
        return ans