#!/bin/python3

import copy


def word_ladder(start_word, end_word, dictionary_file='words5.dict'):
    '''
    Returns a list satisfying the following properties:

    1. the first element is `start_word`
    2. the last element is `end_word`
    3. elements at index i and i+1 are `_adjacent`
    4. all elements are entries in the `dictionary_file` file

    For example, running the command
    ```
    word_ladder('stone','money')
    ```
    may give the output
    ```
    ['stone', 'shone', 'phone', 'phony', 'peony', 'penny',
    'benny', 'bonny', 'boney', 'money']
    ```
    but the possible outputs are not unique,
    so you may also get the output
    ```
    ['stone', 'shone', 'shote', 'shots', 'soots', 'hoots',
    'hooty', 'hooey', 'honey', 'money']
    ```
    (We cannot use doctests here because the outputs are not unique.)

    Whenever it is impossible to generate a word ladder between the two words,
    the function returns `None`.
    '''

    stack = []
    stack.append(start_word)
    queue = []
    queue.append(stack)
    while len(queue) > 0:
        queue.popleft(stack)
        for word in dictionary_file:
            if _adjacent(word, stack[-1]) is True:
                if word == end_word:
                    return stack
                    break
                new_stack = copy.copy(stack)
                new_stack.append(word)
                queue.append(new_stack)
                dictionary_file.remove(word)


def verify_word_ladder(ladder):
    '''
    Returns True if each entry of the input list is adjacent to its neighbors;
    otherwise returns False.

    >>> verify_word_ladder(['stone', 'shone', 'phone', 'phony'])
    True
    >>> verify_word_ladder(['stone', 'shone', 'phony'])
    False
    '''

    ladder = word_ladder(start_word, end_word)

    verify = 0
    for i, word in enumerate(ladder):
        if word != ladder[0]:
            if _adjacent(word, ladder[i-1]) is True:
                verify += 1
            else:
                verify -= 1
    if verify == len(ladder)-1:
        return True
    else:
        return False


def _adjacent(word1, word2):
    '''
    Returns True if the input words differ by only a single character;
    returns False otherwise.

    >>> _adjacent('phone','phony')
    True
    >>> _adjacent('stone','money')
    False
    '''

    diffs = 0
    for a, b in zip(word1, word2):
        if a != b:
            diffs += 1
    if diffs == 1:
        return True
    else:
        return False
