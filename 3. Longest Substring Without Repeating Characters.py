class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        i,j=0,0
        char_index_map={}
        max_len=0
        while i<len(s) and j<len(s):
            if s[j] in char_index_map.keys():
                if i<=char_index_map[s[j]]:
                    i=char_index_map[s[j]]+1
            char_index_map[s[j]]=j
            j+=1

            current_len=j-i
            if current_len>max_len:
                max_len=current_len

        return max_len

solution=Solution()
print(solution.lengthOfLongestSubstring('tmmzuxttmmzuxtat'))