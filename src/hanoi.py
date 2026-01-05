from typing import TypeVar, Generic

T = TypeVar("T")


class Stack(Generic[T]):
    def __init__(self, name: str) -> None:
        self._container: list[T] = []
        self.name = name

    def push(self, value: T) -> None:
        self._container.append(value)

    def pop(self) -> T:
        return self._container.pop()

    def __repr__(self) -> str:
        return repr(self._container)


num_discs: int = 8

tower_a = Stack[int]("A")
tower_b = Stack[int]("B")
tower_c = Stack[int]("C")

for i in range(1, num_discs + 1):
    tower_a.push(i)


def hanoi(
    begin: Stack[int], end: Stack[int], temp: Stack[int], n: int, verbose: bool = False
) -> None:
    if n == 1:
        end.push(begin.pop())
        if verbose:
            print(f"{begin.name} -> {end.name}")
    else:
        hanoi(begin, temp, end, n - 1, verbose)
        hanoi(begin, end, temp, 1, verbose)
        hanoi(temp, end, begin, n - 1, verbose)


if __name__ == "__main__":
    hanoi(tower_a, tower_c, tower_b, num_discs, True)
    print(tower_a)
    print(tower_b)
    print(tower_c)
