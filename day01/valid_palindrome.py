"""
A phrase is a palindrome if, after converting all uppercase letters into
lowercase letters and removing all non-alphanumeric characters,
it reads the same forward and backward. Alphanumeric characters include
letters and numbers.

Given a string s, return true if it is a palindrome, or false otherwise.

Example 1:

Input: sentence = "A man, a plan, a canal, Panama!"
Output: true
Explanation: "amanaplanacanalpanama" is a palindrome.
Example 2:

Input: sentence = "Was it a car or a cat I saw?"
Output: true
Explanation: Explanation: "wasitacaroracatisaw" is a palindrome.
"""


class Solution:

    def is_palindrome(self, s: str) -> bool:
        """
        Check if the sentence is a palindrome, after removing non-alpha-numeric.
        My solution.

        Time complexity: O(n)
        Space complexity: O(n) due to new string

        :param s: sentence
        :return: true if the sentence is a palindrome, otherwise false
        """
        # alpha-numberic only; conver to lowercase
        s2 = [c.lower() for c in s if c.isalpha() or c.isdigit()]
        # 1 index but point to both ends of the string
        index = 0
        while index < len(s2)/2:
            if s2[index] != s2[-index-1]:
                return False
            index += 1
        return True

    def is_palindrome_official(self, s: str) -> bool:
        #  initialize two pointers, one at the start and one at the end of
        #  the string
        i, j = 0, len(s) - 1

        while i < j:  # continue until the two pointers cross over
            while i < j and not s[i].isalnum():
                # move i forward until a letter or digit is found
                i += 1
            while i < j and not s[j].isalnum():
                # move j backward until a letter or digit is found
                j -= 1

            # compare the characters at i and j after converting them to
            # lowercase
            if s[i].lower() != s[j].lower():
                # if they are not equal, the string is not a palindrome
                return False
            i += 1  # move i forward
            j -= 1  # move j backwards

        # if the two pointers have crossed over, the string is a palindrome
        return True


if __name__ == '__main__':
    solution = Solution()
    sents = ["A man, a plan, a canal, Panama!",
             "race a car",
             "Was it a car or a cat I saw?"]
    for sent in sents:
        r = solution.is_palindrome(sent)
        print(sent, r)