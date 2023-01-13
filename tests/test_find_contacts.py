import pytest
from automation.main import find_contacts


def test_exists():
    path = 'test.py'
    assert find_contacts


def test_correct_number_emails():
    path = '../assets/potential-contacts.txt'
    actual = find_contacts(path)[0]
    expected = 100
    assert actual == expected


def test_correct_number_numbers():
    path = '../assets/potential-contacts.txt'
    actual = find_contacts(path)[1]
    expected = 100
    assert actual == expected




