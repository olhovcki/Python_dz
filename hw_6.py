from itertools import count, cycle


def nums(start_from, limit=50):
    for i, v in enumerate(count(start_from)):
        if i > 50:
            break
        yield v


print(list(nums(10)))


def cycle_loop(list, limit=10):
    for i, v in enumerate(cycle(list)):
        if i > limit:
            break
        yield v


print(list(cycle_loop([1, 2, 3])))
