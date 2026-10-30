import sys

import pytest


@pytest.mark.os_touching
def test_planted_marked_not_windows():
    assert sys.platform != "win32", "planted: fails on Windows only (marked)"
