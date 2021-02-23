from task_01 import fact
import pytest
import os
import sys
import inspect


currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
sys.path.insert(0, parentdir)


@pytest.mark.hw71_mark
def test_hw71_1():
    assert fact(18) == 185794560, "Test not passed"
    assert fact(13) == 135135, "Test not passed"


if __name__ == '__main__':
    test_hw71_1()
    print('Test passed successfully')
