from word_list import WORDS
import random
playing = True
attempts = 6
possible_words = WORDS[:]
result = ''
print('Welcome to the wordle solver!')
print('I will provide the words to guess the word of the day.')
print('Please enter the result using G if the square is green, Y if yellow, and N if grey.')
print('The format will be GGGGG if all correct, otherwise GYNNN, YYNNN, etc.')
print('You can quit at any time by typing exit.')

while playing and attempts > 0:
    print(f'You have {attempts} attempts left.')
    guess = random.choice(possible_words)
    feedback = input(f'My guess is: {guess.upper()}. What is the result?\n').upper()

    if feedback == 'EXIT':
        print('Thanks for playing!')
        result = 'exit'
        break
    if len(feedback) != 5:
        print('Please enter a 5 letter feedback.')
        attempts += 1
        continue
    if feedback == 'GGGGG':
        print(f'Yay! The word was {guess.upper()}, we did it!')
        result = 'win'
        break
    else:
        if 'G' in feedback:
            correct_indexes = [i for i, letter in enumerate(feedback) if letter == 'G']
            for i in correct_indexes:
                possible_words = [word for word in possible_words if word[i] == guess[i]]
        if 'Y' in feedback:
            for i in range(len(feedback)):
                if feedback[i] == 'Y':
                    possible_words = [word for word in possible_words if guess[i] in word and word[i] != guess[i]]
        if 'N' in feedback:
            present_letters = [guess[i] for i in range(len(feedback)) if feedback[i] == 'Y' or feedback[i] == 'G']
            for i in range(len(feedback)):
                if feedback[i] == 'N' and guess[i] not in present_letters:
                    possible_words = [word for word in possible_words if guess[i] not in word]
    print('Oops! I will try again.')
    attempts -= 1

if attempts == 0:
    print(f'Sorry! we run out of attempts...')
if result == 'exit':
    print('Come back soon!')
if result == 'win':
    print('Thanks for trying me out!')