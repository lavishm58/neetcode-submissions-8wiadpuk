class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        

        dp = [0]*(target+1)

        # 1
        dp[0]=1


        # 1,2,3

        # c = 0
        # if dp[t-n]>0 or t-n==0:
        #     c += dp[t-n] + 1

        for n in nums:
            if n<=target:
                dp[n]=1 

        for t in range(1,target+1):
            c = 0
            for n in nums:
                if t-n>=0:
                    c+=dp[t-n] 
            dp[t] = c 
        # print(dp)
        return dp[target]

