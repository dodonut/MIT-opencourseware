# Problem Set 2, hangman.py
# Name:
# Collaborators:
# Time spent:

# Hangman Game
# -----------------------------------
# Helper code
# You don't need to understand this helper code,
# but you will have to know how to use the functions
# (so be sure to read the docstrings!)
import random
import string

WORDLIST_FILENAME = "words.txt"


def load_words():
    """
    Returns a list of valid words. Words are strings of lowercase letters.

    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print("Loading word list from file...")
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r')
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = line.split()
    print("  ", len(wordlist), "words loaded.")
    return wordlist


def choose_word(wordlist):
    """
    wordlist (list): list of words (strings)

    Returns a word from wordlist at random
    """
    return random.choice(wordlist)

# end of helper code

# -----------------------------------


# Load the list of words into the variable wordlist
# so that it can be accessed from anywhere in the program
wordlist = load_words()


def is_word_guessed(secret_word, letters_guessed):
    '''
    secret_word: string, the word the user is guessing; assumes all letters are
      lowercase
    letters_guessed: list (of letters), which letters have been guessed so far;
      assumes that all letters are lowercase
    returns: boolean, True if all the letters of secret_word are in letters_guessed;
      False otherwise
    '''
    for c in secret_word:
        if c not in letters_guessed:
            return False
    return True


def get_guessed_word(secret_word, letters_guessed):
    '''
    secret_word: string, the word the user is guessing
    letters_guessed: list (of letters), which letters have been guessed so far
    returns: string, comprised of letters, underscores (_), and spaces that represents
      which letters in secret_word have been guessed so far.
    '''
    in_secret = []
    for c in secret_word:
        if c in letters_guessed:
            in_secret.append(c)
        else:
            in_secret.append('_ ')
    return "".join(in_secret)


def get_available_letters(letters_guessed):
    '''
    letters_guessed: list (of letters), which letters have been guessed so far
    returns: string (of letters), comprised of letters that represents which letters have not
      yet been guessed.
    '''
    alpha = string.ascii_lowercase
    not_in_letters_guessed = []
    for c in alpha:
        if c not in letters_guessed:
            not_in_letters_guessed.append(c)
    return not_in_letters_guessed


def get_total_score(secret_word, user_guesses):
    d = {}
    alpha = []
    for c in secret_word:
        if c in d:
            d[c] += 1
        else:
            d[c] = 0

    for k, v in d.items():
        if v == 0:
            alpha.append(k)

    return user_guesses * len(alpha)


def hangman(secret_word):
    '''
    secret_word: string, the secret word to guess.

    Starts up an interactive game of Hangman.

    * At the start of the game, let the user know how many
      letters the secret_word contains and how many guesses s/he starts with.

    * The user should start with 6 guesses

    * Before each round, you should display to the user how many guesses
      s/he has left and the letters that the user has not yet guessed.

    * Ask the user to supply one guess per round. Remember to make
      sure that the user puts in a letter!

    * The user should receive feedback immediately after each guess
      about whether their guess appears in the computer's word.

    * After each guess, you should display to the user the
      partially guessed word so far.

    Follows the other limitations detailed in the problem write-up.
    '''
    user_guesses = 6
    warnings = 3
    guesses = []
    print('I am thinking of a word that is ',
          len(secret_word), 'letters long.')
    print('---------------')
    while user_guesses and not is_word_guessed(secret_word, guesses):
        print('You have', warnings, ' warnings left')
        print('You have', user_guesses, ' guesses left')
        print('Available letters', get_available_letters(guesses))
        guess = (input('Please guess a letter: '))
        if not (guess.isalpha() and guess in get_available_letters(guesses)):
            if not guess.isalpha():
                print('Oops! That is not a valid letter.', end='')
            elif guess not in get_available_letters(guesses):
                print('Oops! You\'ve already guessed that letter.', end='')
            if warnings:
                warnings -= 1
                print('You have', warnings, 'warnings left: ',
                      get_guessed_word(secret_word, guesses))
            else:
                user_guesses -= 1
                print('You have no warning left, so you lose one guess: ',
                      get_guessed_word(secret_word, guesses))
        else:
            guess = guess.lower()
            guesses.append(guess)
            if guess in secret_word:
                print('Good guess: ', get_guessed_word(secret_word, guesses))
            else:
                print('Oops! That letter is not in my word:',
                      get_guessed_word(secret_word, guesses))
                if guess in 'aeiou':
                    user_guesses -= 2
                else:
                    user_guesses -= 1
        print('-----------')

    if is_word_guessed(secret_word, guesses):
        print('Congratulations, you won!')
        print('Your total score for this game is: ',
              get_total_score(secret_word, user_guesses))
    else:
        print('Sorry, you ran out of guesses. The word was', secret_word, '.')


# When you've completed your hangman function, scroll down to the bottom
# of the file and uncomment the first two lines to test
# (hint: you might want to pick your own
# secret_word while you're doing your own testing)


# -----------------------------------


def match_with_gaps(my_word, other_word):
    '''
    my_word: string with _ characters, current guess of secret word
    other_word: string, regular English word
    returns: boolean, True if all the actual letters of my_word match the
        corresponding letters of other_word, or the letter is the special symbol
        _ , and my_word and other_word are of the same length;
        False otherwise:
    '''
    my_word = my_word.split()
    my_word = "".join(my_word)
    if len(my_word) != len(other_word):
        return False
    for c in range(len(my_word)):
        if my_word[c] != '_' and my_word[c] != other_word[c]:
            return False
    return True


def show_possible_matches(my_word):
    '''
    my_word: string with _ characters, current guess of secret word
    returns: nothing, but should print out every word in wordlist that matches my_word
             Keep in mind that in hangman when a letter is guessed, all the positions
             at which that letter occurs in the secret word are revealed.
             Therefore, the hidden letter(_ ) cannot be one of the letters in the word
             that has already been revealed.

    '''
    all_matches = []
    for c in wordlist:
        if match_with_gaps(my_word, c):
            all_matches.append(c)
    if len(all_matches) == 0:
        return "No matches found!"
    return all_matches


def hangman_with_hints(secret_word):
    '''
    secret_word: string, the secret word to guess.

    Starts up an interactive game of Hangman.

    * At the start of the game, let the user know how many
      letters the secret_word contains and how many guesses s/he starts with.

    * The user should start with 6 guesses

    * Before each round, you should display to the user how many guesses
      s/he has left and the letters that the user has not yet guessed.

    * Ask the user to supply one guess per round. Make sure to check that the user guesses a letter

    * The user should receive feedback immediately after each guess
      about whether their guess appears in the computer's word.

    * After each guess, you should display to the user the
      partially guessed word so far.

    * If the guess is the symbol *, print out all words in wordlist that
      matches the current guessed word.

    Follows the other limitations detailed in the problem write-up.
    '''
    user_guesses = 6
    warnings = 3
    guesses = []
    print('I am thinking of a word that is ',
          len(secret_word), 'letters long.')
    print('---------------')
    while user_guesses and not is_word_guessed(secret_word, guesses):
        print('You have', warnings, ' warnings left')
        print('You have', user_guesses, ' guesses left')
        print('Available letters', get_available_letters(guesses))
        guess = (input('Please guess a letter: '))
        if guess == '*':
            print(show_possible_matches(get_guessed_word(
                secret_word, guesses)))
        elif not (guess.isalpha() and guess in get_available_letters(guesses)):
            if not guess.isalpha():
                print('Oops! That is not a valid letter.', end='')
            elif guess not in get_available_letters(guesses):
                print('Oops! You\'ve already guessed that letter.', end='')
            if warnings:
                warnings -= 1
                print('You have', warnings, 'warnings left: ',
                      get_guessed_word(secret_word, guesses))
            else:
                user_guesses -= 1
                print('You have no warning left, so you lose one guess: ',
                      get_guessed_word(secret_word, guesses))
        else:
            guess = guess.lower()
            guesses.append(guess)
            if guess in secret_word:
                print('Good guess: ', get_guessed_word(secret_word, guesses))
            else:
                print('Oops! That letter is not in my word:',
                      get_guessed_word(secret_word, guesses))
                if guess in 'aeiou':
                    user_guesses -= 2
                else:
                    user_guesses -= 1
        print('-----------')

    if is_word_guessed(secret_word, guesses):
        print('Congratulations, you won!')
        print('Your total score for this game is: ',
              get_total_score(secret_word, user_guesses))
    else:
        print('Sorry, you ran out of guesses. The word was', secret_word, '.')


# When you've completed your hangman_with_hint function, comment the two similar
# lines above that were used to run the hangman function, and then uncomment
# these two lines and run this file to test!
# Hint: You might want to pick your own secret_word while you're testing.


if __name__ == "__main__":
    # pass

    # To test part 2, comment out the pass line above and
    # uncomment the following two lines.

    # secret_word = choose_word(wordlist)
    # hangman(secret_word)

    ###############

    # To test part 3 re-comment out the above lines and
    # uncomment the following two lines.

    secret_word = choose_word(wordlist)
    hangman_with_hints(secret_word)
