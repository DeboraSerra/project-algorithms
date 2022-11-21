from challenges.challenge_encrypt_message import encrypt_message
import pytest


def test_encrypt_message():
    wrong_key()
    odd_key()
    even_key()
    raise_error_key()
    raise_error_message()


def raise_error_message():
    with pytest.raises(TypeError, match="tipo inválido para message"):
        encrypt_message(123456, 2)


def raise_error_key():
    with pytest.raises(TypeError, match="tipo inválido para key"):
        encrypt_message("AABBBCCC", "2")


def wrong_key():
    result = encrypt_message("AAABBBCCC", 10)
    assert result == "CCCBBBAAA"


def odd_key():
    result = encrypt_message("AABBCC", 3)
    assert result == "BAA_CCB"


def even_key():
    result = encrypt_message("ABBCCA", 4)
    assert result == "AC_CBBA"
