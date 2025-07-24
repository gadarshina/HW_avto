import pytest
from string_utils import StringUtils


string_utils = StringUtils()


@pytest.mark.positive
@pytest.mark.parametrize("input_str, expected", [
    ("skypro", "Skypro"),
    ("hello world", "Hello world"),
    ("python", "Python"),
    ("hi", "Hi")
])
def test_capitalize_positive(input_str, expected):
    assert string_utils.capitalize(input_str) == expected


@pytest.mark.negative
@pytest.mark.parametrize("input_str, expected", [
    ("123abc", "123abc"),
    ("", ""),
    ("   ", "   "),
])
def test_capitalize_negative(input_str, expected):
    assert string_utils.capitalize(input_str) == expected


@pytest.mark.positive
@pytest.mark.parametrize("input_str, expected", [
    ("   Skypro", "Skypro"),
    (" Hello world", "Hello world"),
    ("  123", "123"),
    (" H", "H"),
    (" I am very good", "I am very good"),
])
def test_trim_positive (input_str, expected):
    assert string_utils.trim(input_str) == expected


@pytest.mark.negative
@pytest.mark.parametrize("input_str, expected", [
    ("   ", ""),
    ("", ""),
    ("verynice", "verynice"),
])
def test_trim_negative (input_str, expected):
    assert string_utils.trim(input_str) == expected



@pytest.mark.positive
@pytest.mark.parametrize("self, string: str, symbol: str", [
        ("beer", "e", True),
        ("wi-fi", "i", True),
        ("work 4", "4",True),
        ("like7", "0", False),
])
def test_contains_positive(self, string: str, symbol: str) -> bool:
    return symbol in string



@pytest.mark.negative
@pytest.mark.parametrize("self, string: str, symbol: str", [
    ("", "e", True),
    (" ", "1", True),
    ("work 4", "5", True),
    ("like7", "7", False),
])
def test_contains_positive(self, string: str, symbol: str ) -> bool:
    return symbol in string

@pytest.mark.positive
@pytest.mark.parametrize("input_str, symbol, expected", [
        ("SkyPro","k", "SkPro"),
        ("SkyPro", "Pro", "SkPro"),
        ("SkyPro", "Sky", "Pro"),
])
def test_delete_symbol_positive(input_str, symbol, expected):
    assert string_utils.delete_symbol(input_str, symbol) == expected


@pytest.mark.negative
@pytest.mark.parametrize("input_str, symbol", [
    ("", "a"),
    ("", ""),
])
def test_delete_symbol_empty_string(input_str, symbol):
    assert string_utils.delete_symbol(input_str, symbol)

