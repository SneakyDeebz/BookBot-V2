def main():
    Book_path = "books/Alice_in_wonderland.txt"
    text = get_book_text(Book_path)
    word_count = get_num_words(text)
    character_count = get_character_count(text)
    chars_sorted_list = chars_dict_sorted_list(character_count)

    print(f"BookBot V2: Electric Boogaloo -- Initializing Analysis of {Book_path} --")
    print()
    print(f"BookBot has found a total of {word_count} words in {Book_path}.")
    print()


    for item in chars_sorted_list:
        if not item ["char"].isalpha():
            continue
        print(f"The '{item['char']} character was found {item['num']} times")

    print("-- End of Report --")
    print()
    print("BookBot V2 Shutting Down")
   
def get_num_words(text):
    words = text.split()
    return len(words)

def sort_on(d):
    return d["num"]


def chars_dict_sorted_list(num_chars_dict):
    sorted_list = []
    for ch in num_chars_dict:
        sorted_list.append({"char": ch, "num": num_chars_dict[ch]})
    sorted_list.sort(reverse=True, key=sort_on)
    return sorted_list

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