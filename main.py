def main():
    Book_path = "books/Alice_in_wonderland.txt"
    text = get_book_text(Book_path)
    word_count = get_num_words(text)
    character_count = get_character_count(text)
    print(f"Total Word Count:{word_count}")
    print(character_count)
        

def get_num_words(text):
    words = text.split()
    return len(words)

def get_character_count(text):
    char_count = {}
    for c in text:
        lower_case = c.lower()
        if lower_case in char_count:
            char_count[lower_case] += 1
        else:
            char_count[lower_case] = 1
    return char_count

def get_book_text(path):
    with open(path) as f:
        return f.read()

main()