class Solution(object):
    def hammingDistance(self, x, y):
        """
        :type x: int
        :type y: int
        :rtype: int
        """
        xor_result = x ^ y
        
        # Convert the result to binary and count the number of '1's
        distance = bin(xor_result).count('1')
        
        return distance

# Example usage
solution = Solution()
print(solution.hammingDistance(1, 4))  # Output: 2
print(solution.hammingDistance(3, 1))  # Output: 1