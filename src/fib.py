from functools import lru_cache
from collections.abc import Generator


def fib1(n: int) -> int:
    if n < 2:
        return n

    return fib1(n - 2) + fib1(n - 1)


memo: dict[int, int] = {0: 0, 1: 1}


def fib2(n: int) -> int:
    if n not in memo:
        memo[n] = fib2(n - 2) + fib2(n - 1)

    return memo[n]


@lru_cache(maxsize=None)
def fib3(n: int, hi, hello) -> int:
    if n < 2:
        return n

    return fib3(n - 2) + fib3(n - 1)


def fib4(n: int) -> int:
    if n < 2:
        return n

    next: int = 1
    last: int = 0
    for _ in range(1, n):
        next, last = next + last, next

    return next


def fib5(n: int) -> Generator[int]:
    yield 0
    if n > 0:
        yield 1

    last: int = 0
    next: int = 1
    for _ in range(1, n):
        next, last = next + last, next
        yield next


if __name__ == "__main__":
    for i, value in enumerate(fib5(20)):
        print(f"{i} -> {value}")
