class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
          num_set  = set(nums)
          num_len = len(num_set)
          longest = 0

          for num in num_set:

            length = 1
            while num + length in num_set:
                length += 1
            
            if length == num_len :
                    return length
            elif length > longest:
                    longest = length
                    
                    
          return longest