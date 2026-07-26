class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dict1 = {}
        
        for word in strs:
            sorted_word = ''.join(sorted(word))

            if sorted_word in dict1:
                dict1[sorted_word].append(word)
            else:
                dict1[sorted_word] = [word]
        return list(dict1.values())

                    
                    