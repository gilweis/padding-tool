# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),  
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

---

## [1.0.2] - 2025-07-05
### Added
- pypi repo


### Changed
- Returns exit codes 0 (success) and 1 (failure)
- README update

---

## [1.0.1] - 2025-07-01
### Added
- Read/write input and output files in chunks to support large files efficiently
- `chunk_size` internally set to 1MB for performance
- `--padding_value` now has a default value of `255`

### Changed
- Improved memory usage by eliminating `read()` of full file
- Help text updated to reflect default value for `--padding_value` (`255`)

---

## [1.0.0] - 2025-07-01
### Added
- Initial release
- CLI with `argparse`
- `--in`, `--out`, `--needed_size`, `--padding_value` arguments
- `--version` flag
- Error handling for oversized input
