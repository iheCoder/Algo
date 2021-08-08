from typing import List


class Solution:
    def rob(self, nums: List[int]) -> int:
        if not nums:
            return 0
        # 1. 定义初始状态
        size=len(nums)
        first=nums[0]
        second=max(nums[0],nums[1])
        # 2. 状态转移\
        for i in range(2,size):
            first,second=second,max(first+nums[i],second)
        return second

if __name__ == '__main__':
    s=Solution()
    l=list()
    h1=[2,7,9,3,1]
    h2=[1,2,3,1]
    l.append(h1)
    l.append(h2)
    for li in l:
        print(s.rob(li))