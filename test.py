from word_list import WORDS

test_list = WORDS[:]

for w in test_list:
    if 'n' in w and 'i' in w:
        if w.index('n') != 2:
            if w.index('i') != 3:
                if 't' not in w and 'e' not in w and 's' not in w:
                    print(w)