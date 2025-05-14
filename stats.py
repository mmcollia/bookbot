def count_words(book_text):
    counter = 0
    word_list = book_text.split()

    for word in word_list:
        counter += 1

    return f"Found {counter} total words"

def text_to_char(text):
    chars = {}
    for c in text:
        lowered = c.lower()
        if c.isalpha():
            if lowered in chars:
                chars[lowered] += 1
            else:
                chars[lowered] = 1
    return chars

def report(extracted_dict):
    list_dict = [] 
    for key in extracted_dict:
        new_dict = {}
        new_dict["char"] = key
        new_dict["num"] = extracted_dict[key]
        list_dict.append(new_dict)

    list_dict.sort(key=lambda element: element["num"], reverse=True)
    return list_dict


                

