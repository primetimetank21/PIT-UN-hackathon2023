"""Pytests for hello()"""
from hello import hello


def test_hello():
    """Tests for `hello()`"""
    assert hello() == "Hello John!"
    assert hello("Jill") == "Hello Jill!"
    assert hello(name="Jill") == "Hello Jill!"
    assert isinstance(hello(), str)
