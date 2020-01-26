import pytest

from pipey.base import Pipeable
from pipey.extended import append_docstring
from .utils import docstring_tester

def test_Pipeable_divmod_unpack_input():
    """Using divmod, test that the `unpack_input` Pipeable kwarg behaves as expected.
    """
    # GIVEN
    a = 13
    b = 7
    Divmod = Pipeable(divmod, unpack_input=True)

    # WHEN
    result = (a, b) >> Divmod

    # THEN
    assert result == divmod(a, b)


def test_Pipeable_divmod_use_first_arg_only():
    """Using divmod, test that the `use_first_arg_only` Pipeable kwarg behaves as expected.
    """
    # GIVEN
    a = 103
    b = 193
    c = 0
    Divmod = Pipeable(divmod, use_first_arg_only=True)

    # WHEN
    normal_call_result = divmod(a, b)
    pipeable_result = (a, c) >> Divmod(b)

    # THEN
    assert normal_call_result == pipeable_result


def test_Pipeable_try_normal_call_first():
    """Using divmod, test that the `try_normal_call_first` Pipeable kwarg behaves as expected.
    """
    # GIVEN
    a = 11
    b = 12
    @Pipeable(try_normal_call_first=True)
    def NewFunc(a, b=2):
        return a + b

    # WHEN
    normal_call_result = NewFunc(a, b)
    pipeable_result = a >> NewFunc(b=b)

    # THEN
    assert normal_call_result == pipeable_result


def test_inherit_docstring():
    """Test that append_docstring appends the docstring correctly when the decorated function has no docstring.
    """
    # WHEN
    @append_docstring(docstring_tester)
    @Pipeable
    def NewFunc():
        pass

    # THEN
    assert docstring_tester.__doc__ in NewFunc.__doc__


def test_append_docstring():
    """Test that append_docstring appends the docstring correctly when the decorated function has a docstring.
    """
    # WHEN
    @append_docstring(docstring_tester)
    @Pipeable
    def NewFunc():
        """Test docstring.
        """
        pass

    # THEN
    assert docstring_tester.__doc__ in NewFunc.__doc__
    assert "Test docstring." in NewFunc.__doc__

