# coding: utf-8


class Coordinate:
    def __init__(self, x: int, y: int) -> None:
        self.x = x
        self.y = y

    def __repr__(self) -> str:
        return "Coord: " + str(self.__dict__)


def add(a: Coordinate, b: Coordinate) -> Coordinate:
    return Coordinate(a.x + b.x, a.y + b.y)


def sub(a: Coordinate, b: Coordinate) -> Coordinate:
    return Coordinate(a.x - b.x, a.y - b.y)


def main() -> None:
    one = Coordinate(100, 200)
    two = Coordinate(300, 200)
    three = Coordinate(-100, -100)
    print(sub(one, two))
    print(add(one, three))


if __name__ == "__main__":
    main()
