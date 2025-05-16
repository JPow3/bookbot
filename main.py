from stats import get_num_words
from stats import get_num_letters

def get_book_text(filepath):
    with open(filepath) as f:
        contents = f.read()
    return contents

def main():
    text = get_book_text("books/frankenstein.txt")
    num_words = get_num_words(text)
    num_letters = get_num_letters(text)    
    print(f"{num_words} words found in the document")
    print(num_letters)

main()