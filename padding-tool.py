"""Module padding-tool."""

import argparse

__version__ = "1.0.2"


def pad_file(in_file, out_file, needed_size, padding_value, chunk_size=1024 * 1024):
    input_size = os.path.getsize(in_file)

    if input_size > needed_size:
        raise ValueError(f"Input file is larger than needed_size ({input_size} > {needed_size})")

    remaining = needed_size - input_size

    if remaining == 0:
        print(f"File is already {needed_size} bytes. No padding needed.")
        return

    if in_file == out_file:
        print(f"Appending padding to file '{in_file}' to reach {needed_size} bytes.")
        with open(in_file, 'ab') as f:
            padding = bytes([padding_value]) * min(chunk_size, remaining)
            while remaining > 0:
                to_write = padding[:min(len(padding), remaining)]
                f.write(to_write)
                remaining -= len(to_write)
    else:
        print(f"Creating new padded file '{out_file}' ({needed_size} bytes).")
        total_written = 0
        with open(in_file, 'rb') as fin, open(out_file, 'wb') as fout:
            while True:
                chunk = fin.read(chunk_size)
                if not chunk:
                    break
                fout.write(chunk)
                total_written += len(chunk)

            remaining = needed_size - total_written
            if remaining > 0:
                padding = bytes([padding_value]) * min(chunk_size, remaining)
                while remaining > 0:
                    to_write = padding[:min(len(padding), remaining)]
                    fout.write(to_write)
                    remaining -= len(to_write)

def main():
    """ main """
    parser = argparse.ArgumentParser(description="Pad a binary file to a specific size with a given byte value.")
    parser.add_argument('--version', action='version', version=f"%(prog)s {__version__}")
    parser.add_argument('--in', dest='in_file', required=True, help='Input filename')
    parser.add_argument('--out', dest='out_file', required=True, help='Output filename')
    parser.add_argument('--needed_size', type=int, required=True, help='Total size of output file in bytes')
    parser.add_argument('--padding_value', type=int, choices=range(0, 256), required=False,
                        default=255, help='Byte value for padding (0-255, default: 255)')

    args = parser.parse_args()

    pad_file(args.in_file, args.out_file, args.needed_size, args.padding_value)


if __name__ == "__main__":
    main()
