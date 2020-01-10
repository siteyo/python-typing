# coding: utf-8
from typing import List, TypedDict


class Point(TypedDict):
    x: int
    y: int
    label: str


class Line(TypedDict):
    points: List[Point]
    label: str
