import pytest

from distance import minimal_distance

@pytest.mark.parametrize(
    "word1, word2, expected_distance",
    [
        ("hello", "hello", 0),
        ("", "", 0),
        ("kitten", "sitting", 3),
        ("intention", "execution", 5),
        ("", "abc", 3),
        ("xyz", "", 3),
        ("Hello", "hello", 1),
        ("abcdefghijklmnopqrstuvwxyz", "zyxwvutsrqponmlkjihgfedcba", 26),
        ("café", "coffee", 4),
        ("lion", "löwe", 3),
        ("kangaroo", "koala", 6),
        ("!@#$%^*()_+-=", "abcdefghijkl", 13),
        ("a" * 1000, "b" * 1000, 1000),
        ("a" * 1000, "a" * 500 + "b" * 500, 500),
    ]
)
def test_minimal_distance(word1, word2, expected_distance):
    assert minimal_distance(word1, word2) == expected_distance
