class Solution:
    def compress(self, chars: List[str]) -> int:
        left = 0
        ans = ""
        count = 0

        for right in range(len(chars)):

            count += 1

            # Group ends here
            if right == len(chars)-1 or chars[right] != chars[right+1]:

                ans += chars[left]

                if count > 1:
                    ans += str(count)

                left = right + 1
                count = 0

        return len(ans)