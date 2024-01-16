

"""
A pangram is a sentence where every letter of the English alphabet appears at
least once.

Given a string sentence containing English letters (lower or upper-case),
return true if sentence is a pangram, or false otherwise.

Note: The given sentence might contain other characters like digits or spaces,
your solution should handle these too.

Example 1:
Input: sentence = "TheQuickBrownFoxJumpsOverTheLazyDog"
Output: true
Explanation: The sentence contains at least one occurrence of every letter of
the English alphabet either in lower or upper case.

Example 2:
Input: sentence = "This is not a pangram"
Output: false
Explanation: The sentence doesn't contain at least one occurrence of every
letter of the English alphabet.
"""

class Solution:
    def check_if_pangram(self, sentence):
        """
        Check if the sentence is a pangram.
        My solution.

        Time complexity: O(n)
        Space complexity: O(1) since it's maximum 26 characters

        :param sentence: A string that may contain English letters or other
        characters like digits or spaces,
        :return:
        """
        lo = [x.lower() for x in sentence if x.isalpha()]
        lo_set = set(lo)
        if len(lo_set) == 26:
            return True
        return False

    def check_if_pangram_official(self, sentence):
        seen = set() # Create a set to store unique characters

        # Convert sentence to lowercase and iterate over each character
        for currChar in sentence.lower():
            if currChar.isalpha():
                seen.add(currChar) # Add the character to set

        # Return true if set size is 26 (total number of alphabets)
        return len(seen) == 26


if __name__ == '__main__':
    s = Solution()
    sents = ['TheQuickBrownFoxJumpsOverTheLazyDog',
             'This is not a pangram']
    for sent in sents:
        r = s.check_if_pangram(sent)
        print(sent, r)


    # Official test cases
    sol = Solution()
    # Test case 1: "TheQuickBrownFoxJumpsOverTheLazyDog"
    # Expected output: True
    print(sol.check_if_pangram_official("TheQuickBrownFoxJumpsOverTheLazyDog"))

    # Test case 2: "This is not a pangram"
    # Expected output: False
    print(sol.check_if_pangram_official("This is not a pangram"))

    # Test case 3: "abcdef ghijkl mnopqr stuvwxyz"
    # Expected output: True
    print(sol.check_if_pangram_official("abcdef ghijkl mnopqr stuvwxyz"))

    # Test case 4: ""
    # Expected output: False
    print(sol.check_if_pangram_official(""))

    # Test case 5: "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
    # Expected output: True
    print(sol.check_if_pangram_official("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"))


