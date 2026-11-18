class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
          num_set  = set(nums)
          longest = 0
          visited = set()
          for num in num_set:

            if num in visited:
                continue
            
            step = 1
            while num - step in num_set and num - step not in visited:
                visited.add(num  - step)
                step += 1
            
            length  = step 
            step = 1
            while num + step in num_set and num + step not in visited:
                visited.add(num  + step)
                step += 1

            length  = length + step  - 1
            
            if length == len(num_set) :
                    return length
            elif length > longest:
                    longest = length
                    
                    
          return longest