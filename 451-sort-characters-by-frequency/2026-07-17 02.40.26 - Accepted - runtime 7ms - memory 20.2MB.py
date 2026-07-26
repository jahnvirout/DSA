class Solution:
    def frequencySort(self, s: str) -> str:
        freq = Counter(s)
        ans = ''
        freq = sorted(freq.items(), key = lambda x:x[1], reverse = True )
        for key,value in freq:
            ans += key*value
        return ans

