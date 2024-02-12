// Description : 
//Given an integer numRows, return the first numRows of Pascal's triangle.
//Example 1:

//Input: numRows = 5
//Output: [[1],[1,1],[1,2,1],[1,3,3,1],[1,4,6,4,1]]
//solution link : https://leetcode.com/submissions/detail/1173358035/

class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        gen_arr = []
        for i in range(numRows):
            new_list = []
            new_list.append(1)
            
            j = 1
            if i > 0:
                while j in range(i):
                    new_list.append(gen_arr[i-1][j-1] + gen_arr[i-1][j])
                    j = j + 1
            
                new_list.append(1)
            gen_arr.append(new_list)
        return (gen_arr)
