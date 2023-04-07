from gendiff.gendiff import generate_diff
from gendiff.parser import ARGS


def main():
    print(generate_diff(ARGS.first_file, ARGS.second_file))


if __name__ == '__main__':
    main()
