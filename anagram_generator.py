"""
This program represents is an anagram generator. A user is asked for an input file
and then the program prints all the possible anagrams containing a number of words
<= the specified max.

Mark Guan
2/17/17
"""

from letter_inventory import LetterInventory
import os.path

"""
Class AnagramSolver allows one to generate anagrams, based off a given
input and dictionary. An anagram solver is constructed using a dictionary
of words. An anagram solver can also generate and print anagrams based
of a given input, by scrambling all the letters in the input and making
combinations of words (an anagram) from them using the dictionary of words.
One can also specify the max number of words they want the anagrams to be.
"""


class AnagramGenerator:

    # pre  : dictionary is not empty and contains no duplicates
    # post : constructs an anagram solver with given list of words and
        # stores he words, representing the dictionary of words the anagrams
        # are going to be generated from, a corresponding letter inventory
        # for each words is also created and stored
    def __init__(self, dictionary):
        self.words_to_inventories = dict()
        self.dictionary_of_words = dictionary
        for word in dictionary:
            self.words_to_inventories.update({word: LetterInventory(word)})

    # pre: max >= 0 (raises ValueError if not)
    # post : prints to System.out all the possible anagrams (combinations of
        # words with the same letters as the given input) that can been created using
        # the stored dictionary of words, anagrams must contain less words or have
        # an equal number of words to the given max, however, max of 0 represents
        # no maximum number of words in the anagram.
    def print(self, string, max_words_in_anagram):
        if max_words_in_anagram < 0:
            raise ValueError("max_words_in_anagram must be >= 0")
        short_dictionary = list()
        string_letters = LetterInventory(string)
        anagram = list()
        for word in self.dictionary_of_words:
            if string_letters.subtract(self.words_to_inventories.get(word)) is not None:
                short_dictionary.append(word)
        self.generate_anagrams(string_letters, max_words_in_anagram, short_dictionary, anagram)

    # post : finishes generating and prints all the possible anagrams that can be
        # created based on the letters remaining and the given dictionary of words,
        # by searching for and adding new the words to the word in the anagram so
        # far. Anagrams must contain less words or have an equal number of words to
        # the given max, however, max of 0 means that there is no maximum number of
        # words in the anagram.
    def generate_anagrams(self, remaining_letters, max_words_in_anagram, dictionary, anagram):
        if remaining_letters.is_empty():
            print(anagram)
        elif max_words_in_anagram == 0 or len(anagram) < max_words_in_anagram:
            for word in dictionary:
                difference = remaining_letters.subtract(self.words_to_inventories.get(word))
                if difference is not None:
                    anagram.append(word)
                    self.generate_anagrams(difference, max_words_in_anagram, dictionary, anagram)
                    anagram.remove(word)


# main prompts a user for a file and then creates an anagram generator to generate
# anagrams
def main():
    print("Welcome to the anagram generator.")
    print("Enter the name of the dictionary file: ", end="")
    filename = input()
    while not os.path.isfile(filename):
        print("File Not Found. Enter the name of the dictionary file: ", end="")
        filename = input()
    with open(filename):
        dictionary = [line.rstrip('\n') for line in open(filename)]
    solver = AnagramGenerator(dictionary)

    while True:
        print()
        print("phrase to scramble (return to quit): ", end="")
        phrase = input()
        if len(phrase) == 0:
            break
        print("max words in anagram words to include (0 for no max): ", end="")
        max_words_in_anagram = input()
        solver.print(phrase, int(max_words_in_anagram))

if __name__ == "__main__":
    main()