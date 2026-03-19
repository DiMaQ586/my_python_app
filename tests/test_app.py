import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from app import generate_password
import string

def test_length():
    password = generate_password(10)
    assert len(password) == 10

def test_digits():
    password = generate_password(20, use_digits=True)
    assert any(char in string.digits for char in password)

def test_symbols():
    password = generate_password(20, use_symbols=True)
    assert any(char in string.punctuation for char in password)

def test_only_letters():
    password = generate_password(20)
    assert all(char in string.ascii_letters for char in password)

def test_zero_length():
    password = generate_password(0)
    assert password == ""

def test_only_letters():
    password = generate_password(20)
    assert all(char in string.ascii_letters for char in password)


def test_zero_length():
    password = generate_password(0)
    assert password == ""