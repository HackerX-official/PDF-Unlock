# PDF-Unlock — architecture

## Purpose

Python package: parse encryption metadata, generate candidates, decrypt. Non-goals: breaking third-party DRM or bulk attacking unrelated files.

## High-level flow

```mermaid
flowchart LR
  CLI[CLI] --> Core[Core engine]
  Core --> Modules[Domain modules]
  Modules --> Reporters[Reporters]
```

## Module map

| Path | Responsibility |
| --- | --- |
| `pdf_unlock/cli.py` | `unlock-pdf` entry |
| `pdf_unlock/attacks.py` | Candidate generation |
| `pdf_unlock/decrypt.py` | Unlock pipeline |
| `tests/` | pytest |

## Extension

1. Add a module under the appropriate `src/` folder.
2. Register it in the orchestrator (if applicable).
3. Add unit tests with mocks — no live network in unit tests.
4. Run `npm test` and `npm run format:check`.

## Testing strategy

- **Unit**: mocked I/O, pure parsers, reporters.
- **Integration** (if present): live targets documented in README; optional in CI or scheduled.

## Ethics & scope

Authorized engagements only. See [SECURITY.md](./SECURITY.md).
