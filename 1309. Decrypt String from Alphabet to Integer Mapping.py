class Solution:
    def freqAlphabets(self, s: str) -> str:
        out=''
        i=0
        while True:
            if i==len(s):
                break
            elif i==len(s)-1:
                out+=chr(ord('a')+int(s[i])-1)
                break
            elif i==len(s)-2:
                out+=chr(ord('a')+int(s[i])-1)
                out+=chr(ord('a')+int(s[i+1])-1)
                break
            else:
                if s[i+2]=='#':
                    out+=chr(ord('a')+int(s[i:i+2])-1)
                    i+=3
                else:
                    out+=chr(ord('a')+int(s[i])-1)
                    i+=1
        return out

solution = Solution()
s='10#11#12'
print(solution.freqAlphabets(s))



