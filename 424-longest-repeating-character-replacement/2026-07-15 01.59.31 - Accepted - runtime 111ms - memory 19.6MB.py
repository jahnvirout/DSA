class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        left = 0
        max_substring = 0
        counter = defaultdict(int)

        for right in range(len(s)):
            counter[s[right]]+=1

            window_length = right - left+ 1
            if window_length - max(counter.values()) > k:
                counter[s[left]]-=1
                left+=1
            
            max_substring = max(max_substring, right-left+1)
        return max_substring
