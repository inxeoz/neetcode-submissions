class Solution:
    def isPalindrome(self, s: str) -> bool:
        import re

        arr = list(re.sub(r'[^a-zA-Z0-9]', '', s).lower())
        n = len(arr)
        for i in range(n):

            pi = n - i - 1

            if not pi >= i:
                break

            if arr[i] != arr[pi]:
                return False

        return True
