"""
Given a non-negative integer x, return the square root of x rounded down to
the nearest integer. The returned integer should be non-negative as well.

You must not use any built-in exponent function or operator.

For example, do not use pow(x, 0.5) in c++ or x ** 0.5 in python.

Example 1:

Input: x = 8
Output: 2
Explanation: The square root of 8 is 2.8284, and since we need to return
the floor of the square root (integer), hence we returned 2.
Example 2:

Input: x = 4
Output: 2
Explanation: The square root of 4 is 2.
Example 3:

Input: x = 2
Output: 1
Explanation: The square root of 2 is 1.414, and since we need to return the
floor of the square root (integer), hence we returned 1.
"""

class Solution:
  def mySqrt(self, x: int) -> int:
    """
    Given a non-negative integer x, return the square root of x rounded
    down to the nearest integer. The returned integer should be non-negative
    as well.

    time complexity: O(log(n/2)) for binary search of n/2 items
    space complexity: O(1) for 2 variables

    :param x: non-negative integer x
    :return: return the square root of x rounded down to the nearest integer
    """
    if x <= 1:
      return x

    i, j = 2, int(x/2)
    while i <= j:
      mid = i + int((j-i)/2)
      n = mid * mid
      if n < x:
        i = mid + 1
      elif n > x:
        j = mid - 1
      else: # exact
        return mid
    return j

  def mySqrt_official(self, x: int) -> int:
    if x < 2:
      return x # return x if it is 0 or 1

    left, right = 2, x // 2 # initialize left and right pointers
    pivot = 0
    num = 0 # use int to store result of pivot * pivot to prevent overflow
    while left <= right: # binary search for the square root
      pivot = left + (right - left) // 2 # find the middle element
      num = pivot * pivot
      if num > x:
        right = pivot - 1 # if pivot * pivot is greater than x, set right to pivot - 1
      elif num < x:
        left = pivot + 1 # if pivot * pivot is less than x, set left to pivot + 1
      else:
        return pivot # if pivot * pivot is equal to x, return pivot
    return right # return right after the loop


if __name__ == '__main__':
    solution = Solution()
    nums_list = [(27, 5), (4, 2), (8, 2), (15, 3)]

    for nums in nums_list:
        r = solution.mySqrt(nums[0])
        print(nums[0], r, r == nums[1])

    # official
    print('-----')
    for nums in nums_list:
        r = solution.mySqrt_official(nums[0])
        print(nums[0], r, r == nums[1])