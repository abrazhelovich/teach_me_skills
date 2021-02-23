from task_02 import palindrom
import pytest
import os
import sys
import inspect

currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
sys.path.insert(0, parentdir)


@pytest.mark.hw72_mark
def test_hw72():
    assert palindrom('mum') == 'Palindrom', "Test not passed"
    assert palindrom('tut') == 'Palindrom', "Test not passed"
    assert palindrom('tam') == 'Not palindrom', "Test not passed"
    assert palindrom('test') == 'Not palindrom', "Test not passed"


if __name__ == '__main__':
    test_hw72()
    print('Test passed successfully')
