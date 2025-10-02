import pytest

#Math Test
def add(x, y):
    return x + y

def test_add():
    assert add(15, 32) == 47
#String Test
def string_build(x, y):
    concat = str(y + x)
    return concat

def test_string_build():
    assert string_build("ch", "Za") == "Zach"