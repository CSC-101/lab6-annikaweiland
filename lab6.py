import data
from typing import Optional
from typing import Dict

# Write your functions for each part in the space below.

# Part 0

# Finds the index of the smallest value in the list, if there are values,
#     starting from the provided index (if in bounds).
# input: a list of integers
# input: a starting index
# returns: index of smallest value as an int or None if no value is found
def index_smallest_from(values:list[int], start:int) -> Optional[int]:
    if start >= len(values) or start < 0:
        return None

    mindex = start
    for idx in range(start + 1, len(values)):
        if values[idx] < values[mindex]:
            mindex = idx

    return mindex


# Sorts, in place, the elements of a list using the selection sort algorithm.
# input: a list of integers
# returns: nothing is returned; the list is sorted in place
#    <This function modifies/mutates the input list. Though a traditional
#     approach, cloning the list sorting the clone is potentially less
#     surprising. Or even using a different sorting algorithm.>
def selection_sort(values:list[int]) -> None:
    for idx in range(len(values) - 1):
        mindex = index_smallest_from(values, idx)
        tmp = values[mindex]
        values[mindex] = values[idx]
        values[idx] = tmp


# Part 1
def alphabetical_swapping(values: list[data.Book], start: int) -> Optional:
    highest_book = start
    for idx in range(start+1, len(values)):
        if values[idx].title < values[highest_book].title:
            highest_book = idx
    return highest_book

def selection_sort_books(given: list[data.Book]) -> list[data.Book]:
    for idx in range(len(given)-1):
        alphabet = alphabetical_swapping(given, idx)
        temp = given[alphabet]
        given[alphabet] = given[idx]
        given[idx] = temp
    return given

# Part 2
def swap_case(input: str) -> str:
    new_letter_list = []
    if input.isupper():
        return input.lower()
    elif input.islower():
        return input.upper()
    else:
        char_list = list(input)
        for letter in char_list:
            if letter.islower():
                new_letter_list.append(letter.upper())
            elif letter.isupper():
                new_letter_list.append(letter.lower())
            else:
                new_letter_list.append(letter)
    return "".join(new_letter_list)

# Part 3
def str_translate(input: str, old: str, new: str) -> str:
    new_letter = []
    input_list = list(input)
    for char in input_list:
        if char ==old:
            new_letter.append(new)
        else:
            new_letter.append(char)

    return "".join(new_letter)

# Part 4
def histogram(word: str) -> dict:
    histogram = {}
    word_str = word.split()
    for word in word_str:
        if word not in histogram:
            histogram[word] = 1
        elif word in histogram:
            histogram[word] = histogram[word]+1
    return histogram


