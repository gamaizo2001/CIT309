class Solution(object):
    def singleNumber(self, nums: list[int])->int:
        count = Counter(nums)
        for i in count:
            if count[i]==1:
                return i

