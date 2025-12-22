class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        count=0
        count_map={0:1}
        prefix_sum=0

        for i in range(len(nums)):
            prefix_sum+=nums[i]
            curr_sum=prefix_sum-k
            if curr_sum in count_map:
                count+=count_map[curr_sum]
            count_map[prefix_sum]=count_map.get(prefix_sum,0)+1
        return count


        