def get_word_count(book_text):
    words = book_text.split()
    return len(words)

def get_characters(book_text):
    char_dict = {}
    char_list = list(book_text.lower())

    for char in char_list:
        if char in char_dict:
            char_dict[char] += 1
        else:
            char_dict[char] = 1
    
    return char_dict

def sort_on(items):
    return items["num"]

def sorted_chars(char_dict):
    list_of_dicts = []

    for key, value in char_dict.items():
        list_of_dicts.append({"char": key, "num": value})
    
    list_of_dicts.sort(reverse=True, key=sort_on)
    return list_of_dicts

