# Fill in the two functions and the two classes below (look for the TODO comments).
#
# Parts 1 and 2 must use RECURSION - a function that calls itself on a smaller version
# of the problem. Do NOT use a loop for those two.
#
# Do not rename anything, because the automated tests use these names.


def count_occurrences(target, values):
    # TODO (Part 1, recursion): return how many times `target` appears in the list
    #   `values`.
    #   Base case: an empty list contains it 0 times.
    #   Recursive case: 1 (if the first item equals `target`, otherwise 0) plus the
    #   count in the rest of the list, values[1:].
    if target not in values or len(values) == 0:
        return 0
    elif values[0] == target:
        return 1 + count_occurrences(target, values[1:])
    return 0 + count_occurrences(target, values[1:])


def is_sorted(values):
    # TODO (Part 2, recursion): return True if `values` is in non-decreasing order
    #   (every item is <= the one after it), otherwise False.
    #   Base case: a list of 0 or 1 items is already sorted.
    #   Recursive case: the first two items are in order AND the rest is sorted.
    if len(values) < 2:
        return True
    if values[0] < values[1]:
        return is_sorted(values[1:])
    else:
        return False


class Rectangle:
    def __init__(self, width, height):
        # TODO (Part 3, OOP): store width and height on self
        self.width = width
        self.height = height

    def area(self):
        # TODO: return width * height
        return self.width * self.height

    def perimeter(self):
        # TODO: return 2 * (width + height)
        return 2 * (self.width + self.height)

    def __str__(self):
        # TODO: return "<width>x<height>", e.g. Rectangle(3, 4) -> "3x4"
        return f"{self.width}x{self.height}"


class Square(Rectangle):   # Part 4 - stretch (optional)
    def __init__(self, side):
        # TODO: a Square is a Rectangle whose width and height are the same. Call the
        #   Rectangle constructor with `side` for both (use super().__init__(...)).
        #   area, perimeter, and __str__ are then inherited automatically.
        super().__init__(side, side)


def main():
    # Optional scratch space - try your work here, then run: python lab07.py
    print(count_occurrences(2, [1, 2, 2, 3, 2]))   # 3
    print(is_sorted([1, 2, 3, 3.5, 4]))   # True
    print(Rectangle(3, 4).area())     # 12
    r = Rectangle(3,4)
    print(r)
    print(Square(5))                             # 5x5

    
if __name__ == "__main__":
    main()
