def count_words(book_text):
    counter = 0
    word_list = book_text.split()

    for word in word_list:
        counter += 1

    return f"{counter} words found in the document"


