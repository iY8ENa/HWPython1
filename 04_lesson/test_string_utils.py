import pytest
from string_utils import StringUtils

@pytest.fixture
def string_utils():
    return StringUtils()

def test_capitalize_positive(string_utils):
    """
    Позитивный тест для capitalize()
    """
    expected = "Skypro"
    actual = string_utils.capitalize("skypro")
    assert expected == actual, f"capitalize() failed. Expected '{expected}', got '{actual}'"

def test_capitalize_negative(string_utils):
    """
    Негативный тест для capitalize()
    """
    expected = "SKYPRO"
    actual = string_utils.capitalize("skypro")
    assert expected != actual, f"capitalize() failed. Expected '{expected}', got '{actual}'"

def test_trim_positive(string_utils):
    """
    Позитивный тест для trim()
    """
    expected = "skypro"
    actual = string_utils.trim("   skypro")
    assert expected == actual, f"trim() failed. Expected '{expected}', got '{actual}'"

def test_trim_negative(string_utils):
    """
    Негативный тест для trim()
    """
    expected = "   skypro"
    actual = string_utils.trim("   skypro")
    assert expected != actual, f"trim() failed. Expected '{expected}', got '{actual}'"

def test_contains_positive(string_utils):
    """
    Позитивный тест для contains()
    """
    expected = True
    actual = string_utils.contains("SkyPro", "S")
    assert expected == actual, f"contains() failed. Expected '{expected}', got '{actual}'"

def test_contains_negative(string_utils):
    """
    Негативный тест для contains()
    """
    expected = False
    actual = string_utils.contains("SkyPro", "U")
    assert expected == actual, f"contains() failed. Expected '{expected}', got '{actual}'"

def test_delete_symbol_positive(string_utils):
    """
    Позитивный тест для delete_symbol()
    """
    expected = "SyPro"
    actual = string_utils.delete_symbol("SkyPro", "k")
    assert expected == actual, f"delete_symbol() failed. Expected '{expected}', got '{actual}'"

def test_delete_symbol_negative(string_utils):
    """
    Негативный тест для delete_symbol()
    """
    expected = "SkyPro"
    actual = string_utils.delete_symbol("SkyPro", "Z")
    assert expected == actual, f"delete_symbol() failed. Expected '{expected}', got '{actual}'"