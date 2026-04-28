import pytest
import re
from app.password_generator import generate_password

def test_length_default():
pwd = generate_password()
assert len(pwd) == 12

def test_length_custom():
pwd = generate_password(16)
assert len(pwd) == 16

def test_require_upper_lower_digit():
pwd = generate_password(12, use_upper=True, use_lower=True, use_digits=True)
assert re.search(r'[A-Z]', pwd)
assert re.search(r'[a-z]', pwd)
assert re.search(r'\d', pwd)

def test_no_pools():
with pytest.raises(ValueError):
generate_password(8, False, False, False, False)
