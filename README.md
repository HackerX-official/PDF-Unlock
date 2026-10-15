# PDF-Unlock

Recover forgotten PDF passwords and write decrypted copies with qpdf or pikepdf.

## Why this exists

Users lose passwords on their own documents. This package automates ordered attacks (wordlist, dates, digits) for files you are allowed to decrypt.

## Features

- Interactive `run_unlock.sh` wrapper
- Structured attack pipeline in `pdf_unlock/`
- pytest unit tests without live PDFs

## Install

```bash
git clone https://github.com/HackerX-official/PDF-Unlock.git
cd PDF-Unlock
python3 -m venv .venv && source .venv/bin/activate && pip install -e .
```

## Quick start

```bash
./run_unlock.sh -i document.pdf -o ./out --yes
```

## Output

Unlocked PDFs in the output folder; console log of attack stage and success.

## Develop

```bash
pytest tests -q
```

## Architecture

See [ARCHITECTURE.md](./ARCHITECTURE.md) for module layout and extension points.

## Ethics

Use only on systems and content you are **authorized** to test. See [SECURITY.md](./SECURITY.md).

## License

Licensed under the [HackerX License](./LICENSE). Redistributions must retain copyright,
license text, and [NOTICE](./NOTICE) attribution per the license terms.
