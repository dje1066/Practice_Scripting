
import random
import time
import UnitTest


def create_rand_list(size, min_val, max_val):
    rand_list = []
    if size == 0:
        return rand_list
    if max_val <= min_val:
        return rand_list

    random.seed()
    for idx in range(size):
        rand_list.append(random.randrange(min_val, max_val))
    return rand_list


def get_olist(size, min_val, max_val):
    rand_list = []
    if size == 0:
        return rand_list
    if max_val <= min_val:
        return rand_list

    prev_value = min_val
    for idx in range(size):
        curr_val = random.randint(prev_value, max_val)
        rand_list.append(curr_val)
        prev_value = curr_val

    return rand_list


def is_in_order(to_test):
    # if list is empty or not even a list, it's considered sorted
    if to_test is None:
        return True
    elif (not isinstance(to_test, list)) and (not isinstance(to_test, tuple)):
        return True
    elif len(to_test) < 2:
        return True
    else:
        # get the index number
        counter = 0
        prev = to_test[0]
        for elem in to_test:
            if prev > elem:
                return "idx:", counter
            else:
                counter += 1
                prev = elem
        return True


def default_sort_time(to_sort):
    start_time = float(time.time_ns())
    mySorted = to_sort.sort
    end_time = float(time.time_ns())
    return end_time - start_time


# take min val of orig list and place in new list, remove old val
def my_sort(to_sort):
    # assert(isinstance(to_sort, list))
    # returns empty lists and non-lists
    # returns orig list when all numbers are identical
    sorting_list = []
    # use 'is' instead of '==' for None values
    if to_sort is None:
        return to_sort
    elif len(to_sort) <= 1:
        return to_sort
    for elem in range(len(to_sort)):
        sorting_list.append(min(to_sort))
        to_sort.remove(min(to_sort))
    return sorting_list

def my_sort_time(to_sort):
    start_time = float(time.time_ns())
    mySorted = my_sort(to_sort)
    end_time = float(time.time_ns())
    return end_time - start_time

# default_sort_time took 0.0 nanoseconds
# my_sort_time took 4543423232.0 nanoseconds


# PRINT STATEMENTS
# massive random list
unsorted_list = create_rand_list(20000, -200, 300)
unsorted_copy = unsorted_list.copy()

print(unsorted_list)
print(unsorted_copy)

# now sort it
unsorted_copy.sort()
print(unsorted_copy, "\n")

# time it takes to sort list
print("sorting time of unsorted_list is:", default_sort_time(unsorted_list))
print("sorting time of unsorted_list is:", my_sort_time(unsorted_list), "\n")

# small sorting tests for my_sort
basic_list = [200, 15, -99, 34, 2, -6]
list_identical_nums = [12, 12, 12, 12, 12]
empty_list = []
not_even_list = None

# is it in order?
print("Is basic_list in order:", is_in_order(basic_list))
print("Is list_identical_nums in order:", is_in_order(list_identical_nums))
print("Is empty_list in order:", is_in_order(empty_list))
print("Is not_even_list in order:", is_in_order(not_even_list), "\n")

# then sort it
print("ordered basic_list:", my_sort(basic_list))
print("ordered list_identical_nums:", my_sort(list_identical_nums))
print("ordered empty_list:", my_sort(empty_list))
print("ordered not_even_list:", my_sort(not_even_list))
