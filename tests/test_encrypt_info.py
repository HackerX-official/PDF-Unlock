from pdf_unlock.parse import EncryptInfo
from pathlib import Path


def test_supports_fast_verify_rc4_r2():
    info = EncryptInfo(
        path=Path("x.pdf"),
        revision=2,
        version=1,
        length=128,
        permissions=0,
        o_entry=b"o",
        u_entry=b"u",
        file_id=b"id",
    )
    assert info.supports_fast_verify is True


def test_not_encrypted_summary():
    info = EncryptInfo(
        path=Path("x.pdf"),
        revision=0,
        version=0,
        length=0,
        permissions=0,
        o_entry=b"",
        u_entry=b"",
        file_id=b"",
        encrypted=False,
    )
    assert "not encrypted" in info.summary
