"""
Given an array of strings words and two different strings that already exist in the array word1 and word2, return the shortest distance between these two words in the list.

Example 1:

Input: words = ["the", "quick", "brown", "fox", "jumps", "over", "the", "lazy", "dog"], word1 = "fox", word2 = "dog"
Output: 5
Explanation: The distance between "fox" and "dog" is 5 words.
Example 2:

Input: words = ["a", "c", "d", "b", "a"], word1 = "a", word2 = "b"
Output: 1
Explanation: The shortest distance between "a" and "b" is 1 word. Please note that "a" appeared twice.
Example 3:

Input: words = ["a", "b", "c", "d", "e"], word1 = "a", word2 = "e"
Output: 4
Explanation: The distance between "a" and "e" is 4 words.

"""


class Solution:
    def shortest_distance_v1(self, words, word1, word2):
        """"
        Time complexity: O(n^2) from nested for loop -> can be better
        Space complexity: O(n) for the indices
        """
        # get all indices for each word
        word1_indices = [i for i in range(len(words)) if words[i] == word1]
        word2_indices = [i for i in range(len(words)) if words[i] == word2]
        # go through each indices
        shortest = len(words)
        for i1 in word1_indices:
          for i2 in word2_indices:
            # keep shortest distance
            d = abs(i1-i2)
            if d < shortest:
              shortest = d
        return shortest

    def shortest_distance(self, words, word1, word2):
        """
        Given an array of strings words and two different strings that
        already exist in the array word1 and word2, return the shortest
        distance between these two words in the list.

        Time complexity: O(n) for the words list
        Space complexity: O(1)

        :param words: array of strings words
        :param word1: string 1
        :param word2: string 2
        :return: shortest distance between these two words in the list.
        """
        # loop through words list using a 2-pointer system
        p1, p2 = -1, -1
        shortest = len(words)
        for i, w in enumerate(words):
            updated = False
            if w == word1:
                p1 = i
                updated = True
            elif w == word2:
                p2 = i
                updated = True

            if p1 != 1 and p2 != -1 and updated:
                d = abs(p1-p2)
                if d < shortest:
                    shortest = d

        return shortest

    def shortest_distance_official(self, words, word1, word2):
        """
        Time complexity: O(n) for the words list
        Space complexity: O(1)
        """
        shortestDistance = len(words)  # Initialize the shortest distance with the length of the words list
        position1, position2 = -1, -1  # Initialize the positions of word1 and word2 with -1
        for i, word in enumerate(words):
            if word == word1:  # If the current word is word1, update the position1
                position1 = i
            elif word == word2:  # If the current word is word2, update the position2
                position2 = i
            # If both the positions are updated, update the shortest distance
            if position1 != -1 and position2 != -1:
                shortestDistance = min(shortestDistance,
                                       abs(position1 - position2))

        return shortestDistance


if __name__ == '__main__':
    solution = Solution()
    sents = [(["the","quick","brown","fox","jumps","over","the","lazy",
               "dog"], "fox", "dog", 5),
             (["a","b","c","d","a","b"], "a", "b", 1),
             (["a","c","d","b","a"], "a", "b", 1)]

    for sent in sents:
        r = solution.shortest_distance(sent[0], sent[1], sent[2])
        print(sent, r, r == sent[3])

    # official solution
    for sent in sents:
        r = solution.shortest_distance_official(sent[0], sent[1], sent[2])
        print(sent, r, r == sent[3])
