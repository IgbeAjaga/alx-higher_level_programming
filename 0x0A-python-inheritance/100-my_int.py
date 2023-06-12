#!/usr/bin/python3


class MyInt(int):
    """
    MyInt class, inherits from int
    """

    def __eq__(self, other):
        """
        Overrides the == operator and inverts its behavior
        """
        return super().__ne__(other)

    def __ne__(self, other):
        """
        Overrides the != operator and inverts its behavior
        """
        return super().__eq__(other)


if __name__ == "__main__":
    my_i = MyInt(3)
    print(my_i)
    print(my_i == 3)
    print(my_i != 3)
