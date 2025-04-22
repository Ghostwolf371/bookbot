from stats import get_num_words, get_num_each_char, chars_dict_to_sorted_list
import sys


def get_book_text(path_to_file):
    return path_to_file.read()


def main():

    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>'")
        sys.exit(1)

    with open(sys.argv[1]) as f:
        file_contents = get_book_text(f)
        num_words = get_num_words(file_contents)
        char_count = get_num_each_char(file_contents)
        char_list = chars_dict_to_sorted_list(char_count)

        print("============ BOOKBOT ============")
        print(f"Analyzing book found at {sys.argv[1]}...")
        print("----------- Word Count ----------")
        print(f"Found {num_words} total words")
        print("--------- Character Count -------")
        for char_dict in char_list:
            print(f"{char_dict['char']}: {char_dict['count']}")
        print("============= END ===============")


main()
