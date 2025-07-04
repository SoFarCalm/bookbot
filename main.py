def get_book_text(file_path):

    with open(file_path) as f:
        file_contents = f.read()
    
    print(file_contents)


def main():
    
    get_book_text('books/frankenstein.txt')

main()