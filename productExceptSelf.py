class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        arr = nums
        # Aim
        # Multiply everything to the left of a number and store
        result = [1] * len(arr)
        left_product = 1 #Initial value of left_product is 1 because there is nothing to the left of the first number
        # Start a loop to iterate through the list and multiply everything to the left of a number
        # Store the left_products in the results array
        # and update the value of the left_product variable to include the product of every number to the left of the new number
        for i in range (len(arr)):
            result[i] = left_product
            left_product = left_product * arr[i] # this becomes the left product to the next number 
        # Now we find everything to the right of a number
        right_product = 1
        for i in range(len(arr) -1, -1, -1):
            # result = [1,1,2,6] arr=[1,2,3,4]
            result[i] = result[i] * right_product
            right_product = right_product * arr[i]
        return result
            
