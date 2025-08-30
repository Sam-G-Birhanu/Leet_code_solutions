class Solution(object):
    def increasingTriplet(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        i = nums[0]
        j = float('inf')
        k = float('inf')

        for num in nums:
            if num < i:
                i = num
            elif num > i:
                if num > j:
                    k = num
                    return True
                    break
                else:
                    j = num
        return False
                
