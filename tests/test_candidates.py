from pathlib import Path

from pdf_unlock.candidates import filename_candidates, unique


def test_unique_deduplicates():
    assert list(unique(["a", "a", "b"])) == ["a", "b"]


def test_filename_candidates_includes_stem():
    path = Path("/tmp/report-2024.pdf")
    cands = filename_candidates(path)
    assert "report-2024" in cands or "report" in cands
