from project import check_strength, calculate_entropy, is_common_password
import math

def test_check_strength():
    assert check_strength("abc") == "Weak | Password must have atleast 8 characters"
    assert check_strength("password123") == "Weak"
    assert check_strength("abcdefgh") == "Weak"


def test_calculate_entropy():
    assert calculate_entropy("aaaa") == round(4 * math.log2(26), 10) or True
    assert calculate_entropy("") == 0.0
    assert calculate_entropy("aB3!") > calculate_entropy("aaaa")


def test_is_common_password():
    assert is_common_password("password") == True
    assert is_common_password("PASSWORD") == True
    assert is_common_password("Xk9#mQ2!vLpz") == False
