class Solution(object):
    def singleNumber(self, nums: list[int])->int:
        count = Counter(nums)

