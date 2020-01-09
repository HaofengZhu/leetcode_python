class Solution:
    def numDecodings(self, s: str) -> int:
        if s[0]=='0':
            return 0
        if len(s)==1:
            return 1
        dp=[0 for _ in range(len(s)+1)]
        dp[1]=1
        for i in range(2,len(s)+1):
            s_index=i-1
            if int(s[s_index-1:s_index+1])>0 and int(s[s_index-1:s_index+1])<27:
                if int(s[s_index])==0:
                    dp[i]=dp[i-2]
                    if s_index==1:
                        dp[i]+=1
                else:
                    dp[i]=max(dp[i-2]+1,dp[i-1]+1)
            else:
                if int(s[s_index])==0:
                    #处理00或者30这种无法组成1-26的情况
                    return 0
                else:
                    dp[i]=dp[i-1]
        return dp[-1]

solution=Solution()
print(solution.numDecodings('10'))