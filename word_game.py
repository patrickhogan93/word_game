''' Really bad wordle clone. '''

import json
import random


class game():
    def __init__(self, word_list):
        self.word_list = word_list
        self.words = self.load_words()
        self.word = random.choice(self.words)
        self.wrd_len = len(self.word)
        self.guesses = 6

    def play(self):
        guess = input(f'{self.wrd_len} Letter word\nEnter your guess:\n')
        while self.guesses > 0:
            self.check_word(self.word, guess)
            if guess == self.word:
                break
            else:
                guess = input(f'Guesses remaining {self.guesses}\nGuess again:\n')
            self.guesses -= 1
        if guess == self.word:
            print('Welldone!')
        else:
            print(f'Game Over! The word was {self.word}')

    def load_words(self):
        with open(self.word_list,'r') as self.word_list:
            return json.load(self.word_list)

    def check_word(self, word, guess):
        word = word.lower()
        guess = guess.lower()
        result = ''

        for ltr in range(0,len(guess)):
            if self.chk_ltr_exists(guess[ltr], word):
                if self.chk_ltr_position(guess[ltr], word[ltr]):
                    result = result+(guess[ltr].upper())
                else:
                    result = result+(guess[ltr].lower())
            else:
                    result = result+('_')
        print(result)

    def chk_ltr_exists(self, letter, word):
        if letter in word:
            return True

    def chk_ltr_position(self, guess_ltr, word_ltr):
        if guess_ltr == word_ltr:
            return True


word_list = 'words.json'


new_game = game(word_list)
new_game.play()