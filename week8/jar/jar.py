class Jar:
    def __init__(self, capacity: int = 12) -> None:
        if capacity < 0:
            raise ValueError
        self._capacity = capacity
        self._size = 0

    @property
    def capacity(self) -> int:
        return self._capacity

    @property
    def size(self) -> int:
        return self._size

    def withdraw(self, cookies: int) -> None:
        if self.size - cookies < 0:
            raise ValueError
        self._size -= cookies

    def deposit(self, cookies: int) -> None:
        if self.size + cookies > self.capacity:
            raise ValueError
        self._size += cookies

    def __str__(self) -> str:
        return "🍪" * self.size

