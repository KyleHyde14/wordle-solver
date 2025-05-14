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
    allowed = ['G', 'Y', 'N']
    correct = []
    change = []
    print(f'You have {attempts} attempts left.')
    guess = random.choice(possible_words)
    feedback = input(f'My guess is: {guess.upper()}. What is the result?\n').upper()
    
    if feedback == 'EXIT':
        print('Thanks for playing!')
        result = 'exit'
        playing = False
        break
    
    while any(char not in allowed for char in feedback):
        print('Please enter a valid feedback. Only G, Y and N can be valid feedback letters.')
        feedback = input(f'My guess is: {guess.upper()}. What is the result?\n').upper()
        if feedback == 'EXIT':
            print('Thanks for playing!')
            result = 'exit'
            playing = False
            break

    if len(feedback) != 5 and playing:
        print('Please enter a 5 letter feedback.')
        attempts += 1
        continue
    if feedback == 'GGGGG':
        print(f'Yay! The word was {guess.upper()}, we did it!')
        result = 'win'
        break
    else:
        if 'G' in feedback:
            for i in range(5):
                if feedback[i] == 'G':
                    correct.append(guess[i])
                    possible_words = [word for word in possible_words if word[i] == guess[i]]
        if 'Y' in feedback:
            for i in range(5):
                if feedback[i] == 'Y':
                    change.append(guess[i])
                    possible_words = [word for word in possible_words if guess[i] in word and word[i] != guess[i]]
        if 'N' in feedback:
            for i in range(5):
                if feedback[i] == 'N':
                    if guess[i] not in change and guess[i] not in correct:
                        possible_words = [word for word in possible_words if guess[i] not in word]
                    else:
                        if guess[i] in change or guess[i] in correct:
                            count = max(change.count(guess[i]), correct.count(guess[i]))
                            possible_words = [word for word in possible_words if word.count(guess[i]) >= count]

    attempts -= 1                        
    print('Oops! I will try again.')

if attempts == 0:
    print(f'Sorry! we run out of attempts...')
if result == 'exit':
    print('Come back soon!')
if result == 'win':
    print('Thanks for trying me out!')