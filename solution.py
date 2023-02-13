def print_indices_and_elements(elements) -> None:
    count = 0
    indices = 0
    for count, indices in enumerate(elements): #https://realpython.com/python-enumerate/
        print(count, indices)
    
def get_even_numbers_between(start: int, end: int) -> list[int]:
    #https://python-3-patterns-idioms-test.readthedocs.io/en/latest/Comprehensions.html
    end += 1
    sequence = list(range(start, end)) #https://stackoverflow.com/questions/18265935/how-do-i-create-a-list-with-numbers-between-two-values
    even = [n for n in sequence if n%2 == 0]
    return even


def get_char_set_from(s: str) -> set[str]:
    ___set___ = set()
    ___set___ = {c for c in s}
    return ___set___


def get_perfect_squares_between(start: int, end: int) -> dict[int,int]:
    return {}


def filter_even_from(numbers: list[int]) -> list[int]:
    return []


def get_number_or_minus_one(n: int) -> int:
    return n


def transform_multiples_of_5(numbers: list[int]) -> list[int]:
    return []


def str_lengths(strings: list[str]) -> list[int]:
    return []


def get_fibonacci_type(version: int) -> str:
    return ''


def difference_between_fibonacci1_and_fibonacci2() -> str:
    return ''


class SkipIterator:
    def __init__(self, elements):
        self.elements = elements
        # You can add more code here if you need


def my_avg(e1: float, e2: float, *others: tuple[float]) -> float:
    return -1


def keys_with_different_value() -> list[int]:
    return []


def print_out_in(*numbers) -> None:
    while len(numbers) > 1:
        # You should add code here and remove the break
        break

    if numbers:
        # You should add code here
        pass


def append_range(start: int, end: int, step: int=1, to: list[int]=[]):
    # You may add code here

    # Don't change the code below
    for i in range(start, end, step):
        to.append(i)
    return to


global_var = 10

def global_var_func1(n: int):
    for i in range(n):
        print(global_var)


def global_var_func2(n: int):
    for i in range(n):
        global_var += i
        print(global_var)


def value_is_None(value):
    return value == None
