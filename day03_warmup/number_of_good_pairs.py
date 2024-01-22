"""
Given an array of integers nums, return the number of good pairs.

A pair (i, j) is called good if nums[i] == nums[j] and i < j.

Example 1:

Input: nums = [1,2,3,1,1,3]
Output: 4
Explanation: There are 4 good pairs, here are the indices: (0,3), (0,4), (3,4), (2,5).
Example 2:

Input: nums = [1,1,1,1]
Output: 6
Explanation: Each pair in the array is a 'good pair'.
Example 3:

Input: words = nums = [1,2,3]
Output: 0
Explanation: No number is repeating.
"""

class Solution:

    def num_good_pairs(self, nums):
        """
        A pair (i, j) is called good if nums[i] == nums[j] and i < j.

        Every new occurrence of a number can be paired with every previous
        occurrence of the same number. This means if a number has already
        appeared p times, we will have p-1 new pairs.
        :param nums: list of numbers
        :return: number of good pairs.
        """
        pairCount = 0

        # first try
        # time complexity: O(n^2) -> can be better
        # space complexity: O(1)
        #
        # for i in range(len(nums)-1):
        #   for j in range(i+1, len(nums), 1):
        #     if nums[i] == nums[j] and i < j:
        #       pairCount += 1

        # use a counter to cut down time complexity
        # time complexity: O(n)
        # space complexity: O(n) for the hashmap
        cnt = {}
        for n in nums:
            if n not in cnt:
                cnt[n] = 1
            else:
                cnt[n] += 1
            # number of pairs is count - 1 because it can be paired with
            # every occurrence before
            pairCount += cnt[n] - 1
        return pairCount

    def num_good_pairs_official(self, nums):
        pairCount = 0
        map = {}
        for n in nums:
            map[n] = map.get(n, 0) + 1 # increment the count of 'n' in the map
            # every new occurrence of a number can be paired with every previous occurrence
            # so if a number has already appeared 'p' times, we will have 'p-1' new pairs
            pairCount += map[n] - 1
        return pairCount


if __name__ == '__main__':
    solution = Solution()
    nums_list = [([1,2,3,1,1,3], 4),
                ([1,1,1,1], 6),
                ([1,2,3], 0)]

    for nums in nums_list:
        r = solution.num_good_pairs(nums[0])
        print(nums[0], r, r == nums[1])

    # official solution
    print('-----')
    for nums in nums_list:
        r = solution.num_good_pairs_official(nums[0])
        print(nums[0], r, r == nums[1])
