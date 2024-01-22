"""
Given a string s, reverse only all the vowels in the string and return it.

The vowels are 'a', 'e', 'i', 'o', and 'u', and they can appear in both lower
and upper cases, more than once.

Example 1:

Input: s= "hello"
Output: "holle"
Example 2:

Input: s= "AEIOU"
Output: "UOIEA"
Example 3:

Input: s= "DesignGUrus"
Output: "DusUgnGires"
"""

class Solution:
    def reverse_vowels(self, s: str) -> str:
        """
        Reverse vowels. My solution.

        Time complexity: O(n)
        Space complexity: O(n)

        :param s:
        :return:
        """
        vowels = ['a', 'e', 'i', 'o', 'u']
        found = [x for x in s if x.lower() in vowels]
        vindex = -1
        s2 = ''
        for index, c in enumerate(s):
            if c.lower() in vowels:
                s2 += found[vindex]
                vindex -= 1
            else:
                s2 += c
        return s2

    vowels = "aeiouAEIOU"

    def reverse_vowels_official(self, s: str) -> str:
        """
        Reverse vowels. Official solution.
        Use the two-pointer technique to traverse the string from both ends
        simultaneously.

        Time complexity: O(n)
        Space complexity: O(n) for created array

        :return:
        """
        # initialize pointers for start and end of the string
        first, last = 0, len(s) - 1
        array = list(s)
        while first < last:
            # increment the start pointer until a vowel is found
            while first < last and self.vowels.find(array[first]) == -1:
                first += 1
            # decrement the end pointer until a vowel is found
            while first < last and self.vowels.find(array[last]) == -1:
                last -= 1
            # swap the values of first and last if both are vowels
            array[first], array[last] = array[last], array[first]
            # move the pointers towards the center
            first += 1
            last -= 1

        # return the modified string
        return "".join(array)


if __name__ == '__main__':
    solution = Solution()
    sents = ['hello',
             'AEIOU',
             'DesignGUrus']
    for sent in sents:
        r = solution.reverse_vowels(sent)
        print(sent, r)

    # official tests
    s1 = "hello"
    expected_output1 = "holle"
    actual_output1 = solution.reverse_vowels_official(s1)
    print("Test Case 1: ", expected_output1 == actual_output1)

    s2 = "DesignGUrus"
    expected_output2 = "DusUgnGires"
    actual_output2 = solution.reverse_vowels_official(s2)
    print("Test Case 2: ", expected_output2 == actual_output2)

    s3 = "AEIOU"
    expected_output3 = "UOIEA"
    actual_output3 = solution.reverse_vowels_official(s3)
    print("Test Case 3: ", expected_output3 == actual_output3)

    s4 = "aA"
    expected_output4 = "Aa"
    actual_output4 = solution.reverse_vowels_official(s4)
    print("Test Case 4: ", expected_output4 == actual_output4)

    s5 = ""
    expected_output5 = ""
    actual_output5 = solution.reverse_vowels_official(s5)
    print("Test Case 5: ", expected_output5 == actual_output5)
