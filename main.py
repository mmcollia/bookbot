from stats import * 

def get_book_text(filepath):
    with open(filepath) as f:
        file_contents = f.read()
        return file_contents


def print_report(report_dict):
    for letter in report_dict:
        print(f"{letter['char']}: {letter['num']}")

def main():
    print("============ BOOKBOT ============")
    print("Analyzin book found at books/frankenstein.txt")
    print("------------ Word Count -------------")
    print(count_words(get_book_text("books/frankenstein.txt")))
    print("------------ Character Count ------------")
    extracted_dict = text_to_char(get_book_text("books/frankenstein.txt"))
    report_dict = report(extracted_dict)
    print_report(report_dict)
    print("============= END ===============")


main()
