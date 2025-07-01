# Binary File Padding Tool

A simple Python CLI tool to pad a binary file to a specified size using a given byte value.

## Features

- Pads any binary file to a target size
- Customizable padding byte value
- Simple command-line interface
- Version flag support

## Requirements

- Python 3.6 or higher

## Installation

Clone the repository or download the script file `pad_binary.py`.

```bash
git clone https://github.com/yourusername/binary-padding-tool.git
cd binary-padding-tool
```

> Or just download `pad_binary.py` directly.

## Usage

```bash
python pad_binary.py --in INPUT_FILE --out OUTPUT_FILE --needed_size SIZE --padding_value VALUE
```

### Arguments

| Argument           | Description                                      |
|--------------------|--------------------------------------------------|
| `--in`             | Path to the input binary file                    |
| `--out`            | Path to save the padded output file              |
| `--needed_size`    | Total desired size of the output file (in bytes) |
| `--padding_value`  | Byte value to use for padding (0–255)            |
| `--version`        | Show program version and exit                    |

### Example

```bash
python pad_binary.py --in firmware.bin --out padded_firmware.bin --needed_size 4096 --padding_value 255
```

This command reads `firmware.bin`, pads it with `0xFF` (255) bytes until the size is `4096` bytes,
and writes the result to `padded_firmware.bin`.

## Error Handling

- If the input file is larger than `--needed_size`, the program will raise an error and stop.
- Ensure that `--padding_value` is in the valid range `0–255`.

## License

MIT License

## Version

1.0.0
