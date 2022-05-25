import os
from elftools.elf.elffile import ELFFile
from io import BytesIO
import gzip
import argparse


def parse():
    parser = argparse.ArgumentParser(description='XamarinUnpacker for Android')
    parser.add_argument('-i', type=str, required=True, help='packed native library')
    parser.add_argument('-o', type=str, help='directory to unpack')
    args = parser.parse_args()
    return args


def unpack_xamarin_lib(input, output):
    with open(input, 'rb') as f:
        data = f.read()
        f = BytesIO(data)
        elffile = ELFFile(f)
        section = elffile.get_section_by_name('.dynsym')

        if output is None:
            output = os.path.join('output')

        if not os.path.isdir(output):
            os.mkdir(output)

        for symbol in section.iter_symbols():
            if symbol['st_shndx'] != 'SHN_UNDEF' and symbol.name.startswith('assembly_data_'):
                print(f'[+] extract ---------> {symbol.name}')
                dll_data = data[symbol['st_value']:symbol['st_value'] + symbol['st_size']]
                dll_data = gzip.GzipFile(fileobj=BytesIO(dll_data)).read()
                outfile = open(os.path.join(output, symbol.name[14:].replace('_dll', '.dll')), 'wb')
                outfile.write(dll_data)
                outfile.close()


if __name__ == '__main__':
    args = parse()
    unpack_xamarin_lib(args.i, args.o)
