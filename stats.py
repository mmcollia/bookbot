def count_words(book_text):
    counter = 0
    word_list = book_text.split()

    for word in word_list:
        counter += 1

    return f"{counter} words found in the document"

def text_to_char(book_text):
    letter_dict = {
            "a": 0,
            "b": 0,
            "c": 0,
            "d": 0,
            "e": 0,
            "f": 0,
            "g": 0,
            "h": 0,
            "i": 0,
            "j": 0,
            "k": 0,
            "l": 0,
            "m": 0, 
            "n": 0,
            "o": 0,
            "p": 0,
            "q": 0,
            "r": 0,
            "s": 0,
            "t": 0,
            "u": 0,
            "v": 0,
            "w": 0,
            "x": 0,
            "y": 0,
            "z": 0
            }
    book_text = book_text.lower()
    for c in book_text:
        if c in letter_dict:
            actual_count = letter_dict[c]
            actual_count += 1
            letter_dict[c] = actual_count

    return letter_dict
