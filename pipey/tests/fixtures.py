import pytest


@pytest.fixture()
def mock_class_object():
    class NewObject:
        def mock_method(self):
            return True

    return NewObject()

