class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
          num_set  = set(nums)
          longest = 0
          for num in num_set:
            if num - 1 not in num_set:
                length = 1;
                while (num + length ) in  num_set:
                    length +=1
                if length == len(num_set) :
                    return length
                elif length > longest:
                    longest = length
                    
                    
          return longest