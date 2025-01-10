class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        This class reverse inplace the input array recursively. 
        """
        def helper(input_array, start, end):
            if start == len(input_array) // 2:
                return
            else:
                tmp = input_array[start]
                input_array[start] = input_array[end]
                input_array[end] = tmp
                start += 1
                end -= 1
                return helper(input_array,start, end)
        helper(s, 0, len(s) - 1)
