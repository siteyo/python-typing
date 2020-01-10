# coding: utf-8

from types import Line, Point

p1: Point = {"x": 10, "y": 5, "label": "S"}  # ok
p2: Point = {"x": 15, "y": 2, "label": "D"}  # ok
p3: Point = {"x": 20}  # ng

l1: Line = [p1, p2]  # ok
l2: Line = [1, 2]  # ng
