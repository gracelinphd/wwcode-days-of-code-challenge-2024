"""
Given two strings s and t, return true if t is an anagram of s, and false otherwise.

An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.

Example 1:

Input: s = "listen", t = "silent"
Output: true
Example 2:

Input: s = "rat", t = "car"
Output: false
Example 3:

Input: s = "hello", t = "world"
Output: false
"""


class Solution:
    def is_anagram(self, s, t):
        """
        Given two strings s and t, return true if t is an anagram of s,
        and false otherwise.

        An Anagram is a word or phrase formed by rearranging the letters of
        a different word or phrase, typically using all the original letters exactly once.

        Time complexity: O(n)
        Space complexity: O(1) - because the size of the hash table is at
        most 26 characters.

        :param s: string 1
        :param t: string 2
        :return: true if t is an anagram of s, and false otherwise.
        """
        if set(s) != set(t):
            return False
        else:
            c1 = {}
            for char in s:
                if char not in c1:
                    c1[char] = 1
                else:
                    c1[char] += 1

            c2 = {}
            for char in t:
                if char not in c2:
                    c2[char] = 1
                else:
                    c2[char] += 1

            if c1 == c2:
                return True
            else:
                return False

    def is_anagram_official(self, s, t):
        # Check if the lengths of both strings are equal. If not, return false.
        if len(s) != len(t):
          return False

        # Create a hash map to store the frequency of characters in both strings.
        freq_map = {}
        for i in range(len(s)):
          # Increment the frequency of the character in string s.
          if s[i] in freq_map:
            freq_map[s[i]] += 1
          else:
            freq_map[s[i]] = 1

          # Decrement the frequency of the character in string t.
          if t[i] in freq_map:
            freq_map[t[i]] -= 1
          else:
            freq_map[t[i]] = -1

        # Check if the frequency of all characters is 0.
        for char in freq_map:
          if freq_map[char] != 0:
            return False

        # If all characters have a frequency of 0, this means that 't' is an anagram of 's'.
        return True


if __name__ == '__main__':
    solution = Solution()
    sents = [("listen", "silent")]
    for sent in sents:
        r = solution.is_anagram(sent[0], sent[1])
        print(sent, r)

    # official solution

    # Test case 1
    s1 = "listen"
    t1 = "silent"
    print(solution.is_anagram_official(s1, t1) == True)  # Expected output: True

    # Test case 2
    s2 = "hello"
    t2 = "world"
    print(solution.is_anagram_official(s2, t2) == False)  # Expected output:
    # False

    # Test case 3
    s3 = "anagram"
    t3 = "nagaram"
    print(solution.is_anagram_official(s3, t3) == True)  # Expected output: True

    # Test case 4
    s4 = "rat"
    t4 = "car"
    print(solution.is_anagram_official(s4, t4) == False)  # Expected output:
    # False

    # Test case 5
    s5 = ""
    t5 = ""
    print(solution.is_anagram_official(s5, t5) == True)  # Expected output: True
