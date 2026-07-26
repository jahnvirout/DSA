class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ans = []
        visited = [False] * len(strs)

        for i in range(len(strs)):

            if visited[i]:
                continue

            group = []
            group.append(strs[i])
            visited[i] = True

            for j in range(i+1,len(strs)):
                if sorted(strs[i]) == sorted(strs[j]):
                    group.append(strs[j])
                    visited[j] = True
            ans.append(group)
        return ans

                    