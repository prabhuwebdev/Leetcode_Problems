class Solution:
    def targetIndices(self, nums: List[int], target: int) -> List[int]:
        Sort=sorted(nums)
        output=[]
        for i,j in enumerate(Sort):
            if j == target:
                output.append(i)
        return output

        