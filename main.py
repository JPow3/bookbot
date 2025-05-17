from stats import get_num_words
from stats import get_num_letters
from stats import final_sort
import sys

def get_book_text(filepath):
    with open(filepath) as f:
        contents = f.read()
    return contents

def main():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        return sys.exit(1)
    text = get_book_text(sys.argv[1])
    num_words = get_num_words(text)
    num_letters = get_num_letters(text)    
    print("============ BOOKBOT ============")   
    print(f"Analyzing book found at {sys.argv[1]}...")  
    print("----------- Word Count ----------") 
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    sorted_chars = final_sort(num_letters)
    for char_dict in sorted_chars:
        char = char_dict["char"]
        if char.isalpha():  # Only print alphabetical characters
            print(f"{char}: {char_dict['num']}")
    print("============= END ===============")

main()