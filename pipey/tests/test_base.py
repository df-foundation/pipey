import pytest

from .fixtures import mock_class_object
from pipey.base import Pipeable


def test_Pipeable_base_object_type(mock_class_object):
    """Ensure that Pipeable doesn't change the type of a function.
    """

    # WHEN
    pipeable_object = Pipeable(mock_class_object)
    assert type(pipeable_object.base_object) == type(mock_class_object)


def test_Pipeable_sum_class_object():
    """Ensure correct output of a Pipeable-wrapped `sum` function as an instantiated class object `Sum()`.
    """
    # GIVEN
    values_to_sum = [7, 12]
    Sum = Pipeable(sum)

    # WHEN
    result = values_to_sum >> Sum()

    # THEN
    assert result==19


def test_Pipeable_sum_class():
    """Ensure correct output of a Pipeable-wrapped `sum` function as an uninstanted class `Sum`.
    """
    # GIVEN
    values_to_sum = [7, 12]
    Sum = Pipeable(sum)

    # WHEN
    result = values_to_sum >> Sum

    # THEN
    assert result==19


def test_Pipeable_divmod_args():
    """Ensure correct output of a Pipeable-wrapped `divmod` function to test correct parsing of arguments.
    """
    # GIVEN
    a = 13
    b = 7
    Divmod = Pipeable(divmod)

    # WHEN
    result = a >> Divmod(b)

    # THEN
    assert result == divmod(a, b)



