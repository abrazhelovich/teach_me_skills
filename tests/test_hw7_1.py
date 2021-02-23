from task_01 import fact
import pytest
import os
import sys
import inspect

currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
sys.path.insert(0, parentdir)


@pytest.mark.hw71_mark
def test_hw71():
    assert fact(7) == 105, "Test not passed"
    assert fact(4) == 8, "Test not passed"
    assert fact(3) == 3, "Test not passed"
    assert fact(18) == 185794560, "Test not passed"


if __name__ == '__main__':
    test_hw71()
    print('Test passed successfully')
