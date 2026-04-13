# A set is unordered.
# A set is a collection of unique elements.
# We cannot add duplicate elements to a set.

# my_set = {1, 2, 3}
# print(my_set)

# my_set_2 = {3, 2, 1}
# print(my_set_2)

# set_1 = set()

# set_1.add(1)
# set_1.add(2)
# set_1.add(1)

# print(set_1)

from typing import List, Set


# def list_to_set(nums: List[int]) -> Set[int]:
#     my_set = set()
#     for n in nums:
#         my_set.add(n)
#     return my_set


# print(list_to_set([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))
# print(list_to_set([1, 1, 2, 2, 3, 3]))

# def count_unique_words(word: List[str]) -> int:
#     word_set = set(word)
#     return len(word_set)


# print(count_unique_words(["apple", "banana", "apple", "orange", "banana"]))

def contains_duplicate(words: List[str]) -> bool:
    my_set = set(words)
    return len(my_set) < len(words)


print(contains_duplicate(["apple", "banana", "apple", "orange", "banana"]))
print(contains_duplicate(["apple", "banana", "orange", "grape"]))
