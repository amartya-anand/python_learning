# def get_longer_word(word1: str, word2: str) -> str:
#     if len(word1) > len(word2):
#         return word1
#     else:
#         return word2


# print(get_longer_word("hello", "world"))
# print(get_longer_word("Amartya", "Anand"))

# def print_first_letter(word: str) -> None:
#     print(word[0])


# def print_second_letter(word: str) -> None:
#     print(word[1])


# def print_last_letter(word: str) -> None:
#     last_index = len(word) - 1
#     print(word[last_index])


# print_first_letter("hello")
# print_second_letter("hello")
# print_last_letter("hello")

# def print_string_characters(word: str) -> None:
#     for index in range(len(word)):
#         print(word[index])


# print_string_characters("hello")

# def print_string_characters(word: str) -> None:
#     for character in word:
#         print(character)


# print_string_characters("hello")

# def concatenate(s1: str, s2: str) -> str:
#     s3 = s1 + s2
#     if len(s3) > 10:
#         print("too long")
#     else:
#         print(s3)


# concatenate("Amartya", "Anand")
# concatenate("hello", "world")

# my_string = "Amartya"

# print(my_string[:2])

# def first_n_charactes(s: str, n: int) -> str:
#     return s[:n]


# def last_n_characters(s: str, n: int) -> str:
#     index = len(s) - n
#     return s[index:]


# print(last_n_characters("Amartya", 3))
# print(first_n_charactes("Anand", 3))
# def reverse_string(input_string: str) -> str:
#     return input_string[::-1]


# print(reverse_string("hello"))

# msg = "I will never change"

# str1 = msg[:1]
# str2 = msg[2:]

# print(str1 + " " + str2)

# def remove_fourth_character(word: str) -> str:
#     first_part = word[:4]
#     second_part = word[5:]
#     return first_part + second_part


# print(remove_fourth_character("Neetcode"))
# print(remove_fourth_character("Hello"))

# name = "Amartya"
# item = "Sugar"

# # msg = "Hello,{}.Would you like to have some tea with {}".format(
# #     name, item)
# msg = f"Hello, {name}. Would you like to have some tea with {item}?"

# print(msg)

def say_goodbye(name: str, hour: int) -> str:
    msg = f"Goodbye, {name}. It is {hour} o'clock."

    return msg


print(say_goodbye("Amartya", 10))
