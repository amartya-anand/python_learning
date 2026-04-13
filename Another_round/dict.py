# Use to store key value pairs

from typing import Dict, List


# def create_dict(name: str, age: int) -> Dict[str, int]:
#     my_dict = {name: age}
#     return my_dict


# def list_to_dict(words: List[str]) -> Dict[str, int]:
#     my_dict = {}
#     for i in range(len(words)):
#         w = words[i]
#         my_dict[w] = i
#     return my_dict


# print(create_dict("John", 30))
# print(create_dict("Jane", 25))
# print(list_to_dict(["apple", "banana", "cherry"]))
# print(list_to_dict(["dog", "cat", "mouse"]))

# Dictonaries cannot contain duplicate values

your_dict = {
    "a": 10,
    "b": 20,
    "c": 30,
}

print(your_dict)
print(your_dict["a"])
print("d" in your_dict)
your_dict["a"] = 100
print(your_dict)
