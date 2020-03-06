# coding: utf-8
from typing import List, TypedDict, Generic, TypeVar


class Point(TypedDict):
    x: int
    y: int
    label: str


class Line(TypedDict):
    points: List[Point]
    label: str


T = TypeVar("T")


class MyStack(Generic[T]):
    def __init__(self):
        self.__items: List[T] = []

    def stack(self, value: T) -> None:
        self.__items.append(value)

    def pop(self) -> T:
        return self.__items.pop()
