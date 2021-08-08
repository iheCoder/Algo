from typing import List


class Solution:
    def rob(self, nums: List[int]) -> int:
        # 1. 定义初始状态
        size=len(nums)
        dp=[0]*size
        dp[0]=nums[0]
        # 2. 状态转移
        for i in range(1,size):
            dp[i]=max(dp[i-1],dp[i-2]+nums[i])
        return dp[-1]

if __name__ == '__main__':
    s=Solution()
    l=list()
    h1=[2,7,9,3,1]
    h2=[1,2,3,1]
    l.append(h1)
    l.append(h2)
    for li in l:
        print(s.rob(li))