from stats import * 
import sys

def get_book_text(filepath):
    with open(filepath) as f:
        file_contents = f.read()
        return file_contents


def print_report(report_dict):
    for letter in report_dict:
        print(f"{letter['char']}: {letter['num']}")

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    extracted_dict = text_to_char(get_book_text(sys.argv[1]))
    report_dict = report(extracted_dict)
    print("============ BOOKBOT ============")
    print(f"Analyzin book found at {sys.argv[1]}")
    print("------------ Word Count -------------")
    print(count_words(get_book_text(sys.argv[1])))
    print("------------ Character Count ------------")
    print_report(report_dict)
    print("============= END ===============")


main()
