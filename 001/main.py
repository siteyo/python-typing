# coding: utf-8

from types import Line, Point, MyStack

p1: Point = {"x": 10, "y": 5, "label": "S"}  # ok
p2: Point = {"x": 15, "y": 2, "label": "D"}  # ok
p3: Point = {"x": 20}  # ng

l1: Line = {"points": [p1, p2], "label": "Line"}  # ok
l2: Line = {"points": [p1, p2]}  # ng
l3: Line = "Hello"  # ng
