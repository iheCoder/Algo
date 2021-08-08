from typing import List


class Solution:
    def rob(self, nums: List[int]) -> int:
        if not nums:
            return 0
        size=len(nums)
        if size==1:
            return nums[0]
        if size==2:
            return max(nums[0],nums[1])

        # 1. 定义初始状态
        first=nums[0]
        second=max(nums[0],nums[1])
        # 2. 状态转移
        for i in range(2,size-1):
            first,second=second,max(first+nums[i],second)

        f2=nums[1]
        s2=max(nums[1],nums[2])
        for j in range(3,size):
            f2,s2=s2,max(f2+nums[j],s2)
        return max(second,s2)

if __name__ == '__main__':
    s=Solution()
    l=list()
    h1=[2,7,9,3,1]
    h2=[1,2,3,1]
    l.append(h1)
    l.append(h2)
    for li in l:
        print(s.rob(li))