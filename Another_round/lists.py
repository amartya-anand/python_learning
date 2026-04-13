# my_list = [1, 2, 4, 5, 7, 8, 10]
# # List are mutable,whereas strings are not
# my_list_2 = ["I", "Am", "A", "List"]

# print(my_list[2])
# print(my_list_2[1])

# if len(my_list) > 5:
#     print("The list is long")
# else:
#     print("The list is short")

# if "Am" in my_list_2:
#     print("Am is in the list")

# if 3 in my_list:
#     print("3 is in the list")
# else:
#     print("3 is not in the list")

# from typing import List


# def count_x(nums: List[int], x: int) -> int:
#     count = 0
#     for n in nums:
#         if n == x:
#             count += 1
#     return count

# print(count_x([1, 2, 3, 4, 5, 6, 7, 8, 9], 5))
# print(count_x([1, 2, 3, 4, 5, 6, 7, 8, 9], 10))

# from typing import List


# def get_sum(nums: List[int]) -> int:
#     total = 0
#     for n in nums:
#         total += n
#     return total


# def get_min(nums: List[int]) -> int:
#     current_min = nums[0]
#     for n in nums:
#         if n < current_min:
#             current_min = n
#     return current_min


# def get_max(nums: List[int]) -> int:
#     current_max = nums[0]
#     for n in nums:
#         if n > current_max:
#             current_max = n
#     return current_max


# print(get_sum([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))
# print(get_min([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))
# print(get_max([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))

# When we call a function on a varibale itself, it is called a method


# from typing import List


# def append_to_list(my_list: List[int], elements: List[int]) -> List[int]:

#     for n in elements:
#         my_list.append(n)
#     return my_list


# print(append_to_list([1, 2, 3, 4, 5], [6, 7, 8, 9, 10]))


# def remove_from_list(my_list: List[int], index: List[int]) -> List[int]:
#     my_list.pop(index)
#     return my_list


# def pop_n_list(my_list: List[int], n: int) -> List[int]:
#     while n > 0:
#         my_list.pop()
#         n -= 1
#     return my_list


# print(pop_n_list([1, 2, 3, 4, 5], 2))
# print(remove_from_list([1, 2, 3, 4, 5], 3))


from typing import List


# def find_index(nums: List[int], target: int) -> int:
#     # return nums.index(target)
#     for i in range(len(nums)):
#         n = nums[i]
#         if n == target:
#             return i


# print(find_index([1, 2, 3, 4, 5], 3))

# List slicing

def get_last_three_elements(my_list: List[int], n: int) -> List[int]:
    return my_list[len(my_list) - 3:]


print(get_last_three_elements([1, 2, 3, 4, 5], 3))
