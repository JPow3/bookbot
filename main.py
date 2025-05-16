from stats import get_num_words
from stats import get_num_letters
from stats import final_sort

def get_book_text(filepath):
    with open(filepath) as f:
        contents = f.read()
    return contents

def main():
    text = get_book_text("books/frankenstein.txt")
    num_words = get_num_words(text)
    num_letters = get_num_letters(text)    
    print("============ BOOKBOT ============")   
    print("Analyzing book found at books/frankenstein.txt...")  
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