"""
Class LetterInventory can store an inventory of all
letters of the alphabet. A letter inventory is initially constructing using
a string and will store the counts of the letters of the given string. A letter
inventory allows one to get the count of a letter, set the count of a letter,
add another letter inventory to it, and subtract another letter inventory from it.

Mark Guan
1/8/17
"""


class LetterInventory:
    num_letters = 26  # number of letters in english alphabet

    # pre : String data is not None
    # post: constructs an letter inventory which stores the counts of the
    #       letters of the given string
    def __init__(self, data):
        self.size = 0
        self.counts = []
        i = 1
        while i <= 26:
            self.counts.append(0)
            i += 1
        for ch in data:
            ch = ch.lower()
            if LetterInventory.is_lowercase_letter(ch):
                self.counts[ord(ch) - ord('a')] += 1
                self.size += 1

    # post: returns True if the given character is an alphabetic lowercase letter,
    #      False otherwise
    @staticmethod
    def is_lowercase_letter(ch):
        return 0 <= ord(ch) - ord('a') < LetterInventory.num_letters

    # post: returns true if all the counts of the letters are zero,
    #       false otherwise
    def is_empty(self):
        return self.size == 0

    # pre : given letter is an alphabetic letter (raises
    #       ValueError if not)
    # post: returns the count of the given letter in the inventory
    def get(self, letter):
        letter = letter.lower()
        if not LetterInventory.is_lowercase_letter(letter):
            raise ValueError("letter must be an alphabetical letter")
        return self.counts[ord(letter) - ord('a')]

    # pre : letter is an alphabetic lowercase letter && value >= 0 (raises
    #       ValueError if not)
    # post: sets the count of the given letter to the given value
    def set(self, letter, value):
        letter = letter.lower()
        if not LetterInventory.is_lowercase_letter(letter) or value < 0:
            raise ValueError("letter must be an alphabetical letter and value must be >= 0")
        original_value = self.counts[ord(letter) - ord('a')]
        self.counts[ord(letter) - ord('a')] = value
        self.size += (value - original_value)

    # post: constructs and returns a new letter inventory that is the result
    #       of adding this letter inventory to another given letter inventory
    def add(self, other_letter_inventory):
        result = LetterInventory("")
        i = 0
        while i < LetterInventory.num_letters:
            letter = chr(i + ord('a'))
            together = self.get(letter) + other_letter_inventory.get(letter)
            result.set(letter, together)
            i += 1
        return result

    # post: constructs and returns a new letter inventory that is
    #       the result of subtracting another inventory from this inventory.
    #       If any of the resulting counts in the new letter inventory would
    #       be negative then null is returned.
    def subtract(self, other_letter_inventory):
        result = LetterInventory("")
        i = 0
        while i < LetterInventory.num_letters:
            letter = chr(i + ord('a'))
            difference = self.get(letter) - other_letter_inventory.get(letter)
            if difference < 0:
                return None
            result.set(letter, difference)
            i += 1
        return result

    # post: returns a String representation of the inventory with lowercase
    #       letters based of the count of each letter
    def __str__(self):
        result = "["
        i = 0
        for letter_count in self.counts:
            result += chr(i + ord('a')) * letter_count
            i += 1
        return result + "]"
