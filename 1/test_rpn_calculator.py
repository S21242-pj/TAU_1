from rpn_calculator import rpn

import pytest

def test_rpn_num1():
    assert rpn("42") == 42

def test_rpn_num_multiple():
    assert rpn("42 3") == 3

def test_rpn_add():
    assert rpn("42 3 +") == 45

def test_rpn_add():
    assert rpn("42 3 3 +") == 6

def test_rpn_add_inexact():
    assert rpn("0.1 0.2 +") == pytest.approx(0.3)

def test_rpn_mul():
    assert rpn("42 3 *") == 126

def test_rpn_add_mul():
    assert rpn("42 3 3 * +") == 51

def test_too_few_operands():
    with pytest.raises(Exception, match="too few operands"):
        rpn("42 3 * +")

def test_rpn_non_numeric_operand():
    with pytest.raises(Exception, match="expected a number"):
        assert rpn("42 x") == 42

@property
def divided(self):
    try:
        assert rpn("10 0 /")
        return
    except ZeroDivisionError:
        return None