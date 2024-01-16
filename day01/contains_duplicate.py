#
# Grokking the Coding Interview: Patterns for Coding Questions
# by Design Gurus.
#

# --------------
# Introduction
# --------------
# - Need basic understanding of data structures and algorithms.
# - You should be familiar with Big O notation.
# - There are ~200 problems mapped to 22 patterns that can be used to solve
# coding questions.
# - Various algo techniques:
#   - Trees and graphs: Breadth-first search, Depth-First Search
#   - Dynamic programming
#   - Backtracking
#   - Recursion
#   - Greedy algo
#   - Divide & conquer

# ------------------
# Warmup questions
# ------------------
# Take it slow at the beginning.

# Given an integer array nums, return true if any value appears at least
# twice in the array, and return false if every element is distinct.
#
# Example 1:
# Input: nums= [1, 2, 3, 4]
# Output: false
# Explanation: There are no duplicates in the given array.
#
# Example 2:
# Input: nums= [1, 2, 3, 1]
# Output: true
# Explanation: '1' is repeating.


class Solution:
    def contains_duplicate(self, nums):
        """
        Check for duplicated numbers.
        My solution.

        Time complexity: O(n) for number of elements

        Space complexity: O(n) for storing elements

        :param nums: array of numbers
        :return: true if there are duplicates, else false
        """
        arr = []
        for x in nums:
            if x in arr:
                return True
            arr.append(x)

        return False

    def contains_duplicate_official(self, nums) -> bool:
        """
        Check for duplicated numbers.
        One of the three official solutions.

        Time complexity: O(N*logN) due to sorting of an array.

        Space complexity: O(1) if it's in-place sort, or O(N) if creating new.

        :param nums: array of numbers
        :return: true if there are duplicates, else false
        """
        nums.sort()  # sort the array
        # use a loop to compare each element with its next element
        for i in range(len(nums) - 1):
            if nums[i] == nums[i + 1]:
                # if any two elements are the same return true
                return True
        return False  # if no duplicates are found, return false


if __name__ == '__main__':
    s = Solution()
    testcase = [1, 2, 3, 4]
    r = s.contains_duplicate(testcase)
    print(testcase, r)

    r = s.contains_duplicate_official(testcase)
    print(testcase, r)



