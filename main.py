def main():
    Book_path = "books/Alice_in_wonderland.txt"
    text = get_book_text(Book_path)
    word_count = get_num_words(text)
    print(f"Total Word Count:{word_count}")

def get_num_words(text):
    words = text.split()
    return len(words)

def get_book_text(path):
    with open(path) as f:
        return f.read()

main()