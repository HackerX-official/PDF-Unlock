from pdf_unlock.crypto import PADDING


def test_padding_length_is_32_bytes():
    assert len(PADDING) == 32
