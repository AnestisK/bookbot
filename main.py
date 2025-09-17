from stats import get_word_count
from stats import get_characters
from stats import sorted_chars


def main():
    print("============ BOOKBOT ============")
    print("Analyzing book found at books/frankenstein.txt...")

    content = get_book_text("./books/frankenstein.txt")
    num_words = get_word_count(content)

    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")

    char_count = get_characters(content)
    list_of_chars = sorted_chars(char_count)

    print("--------- Character Count -------")
    
    for dict in list_of_chars:
        if dict["char"].isalpha():
            print(f"{dict['char']}: {dict['num']}")

    print("============= END ===============")
    
def get_book_text(filepath):
    with open(filepath) as f:
        file_contents = f.read()
    return file_contents

main()