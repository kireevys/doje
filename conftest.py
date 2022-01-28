import pytest


class DescribeTest:
    def describe(self, *args):
        ...

    def assert_equals(self, actual, expected):
        assert actual == expected


@pytest.fixture
def test():
    return DescribeTest()
