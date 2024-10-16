from typing import List


def twoSum(nums: List[int], target: int) -> List[int]:
    ans={}
    
    for i, num in enumerate(nums):
        tmp = target - num
        
        if tmp in ans:
            return [ans[tmp],i]
        
        ans[num] = i
        