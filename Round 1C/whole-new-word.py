# Codejam 2018, Round 1C: A Whole New Word

import itertools

def find_new_word(word_list, word_length):
    """Finds new word given list of words."""
    letter_positions = [set(word[i] for word in word_list)
                        for i in range(word_length)]

    for try_word in itertools.product(*letter_positions):
        new_word = ''.join(try_word)
        if new_word not in word_list:
            return new_word
    return None

# I/O Code
num_cases = int(input())

for case in range(1, num_cases + 1):
    num_words, word_length = map(int, input().split())

    word_list = set()
    for _ in range(num_words):
        word_list.add(input())

    new_word = find_new_word(word_list, word_length)
    if new_word is None:
        new_word = '-'
    print('Case #{}: {}'.format(case, new_word))
