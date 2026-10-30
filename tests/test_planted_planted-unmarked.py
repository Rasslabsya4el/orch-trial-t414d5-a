import sys


def test_planted_unmarked_not_windows():
    assert sys.platform != "win32", "planted: fails on Windows only (unmarked)"
