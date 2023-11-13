"""Kttis coldputer problem.
"""

__author__ = "Bryleigh Koci"
__date__ = "October 12, 2023"


def answer(temps: str) -> int:
    """finds and returns no. of -ve of temps.
    args:
        temps(str): temps separated by space
    returns:
        int: Number of hyphens(-ne temps)
    """
    return temps.count('-')


def solve() -> None:
    """solves anser with input
    Args:
        temps (_type_): _description_
    """
    _ = input()
    data = input()
    print(answer(data))


if __name__ == "__main__":
    solve()
