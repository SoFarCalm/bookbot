import sys
from stats import get_book_text, get_num_words, get_num_chars, sort_dictionary

# 'books/frankenstein.txt', 'books/mobydick.txt', 'books/prideandprejudice.txt'

def main():
    print(f"""============ BOOKBOT ============\nAnalyzing book found at {sys.argv[1]}...\n----------- Word Count ----------""")
    number_of_words = get_num_words(get_book_text(sys.argv[1]))
    print(f"Found {number_of_words} total words")
    print('--------- Character Count -------')
    sort_dictionary(get_num_chars(get_book_text(sys.argv[1])))

if len(sys.argv) != 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)

main()