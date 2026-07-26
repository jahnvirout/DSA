class Solution:
    def compress(self, chars: List[str]) -> int:
        left = 0
        ans = ""
        for right in range(len(chars)):
            count = 0
            if chars[right]== chars[left]:
                count+=1
                count = str(count)
                ans += chars[right] + count
            else:
                left = right
        return len(ans)