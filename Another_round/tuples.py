# Tuples are immutable

from typing import Tuple


def cretae_pair(name: str, age: int) -> Tuple[str, int]:
    return (name, age)


print(cretae_pair("John", 25))
print(cretae_pair("Jane", 30))
