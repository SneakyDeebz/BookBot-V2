def main():
    Book_path = "books/Alice_in_wonderland.txt"
    text = get_book_text(Book_path)
    word_count = get_num_words(text)
    character_count = get_character_count(text)
    chars_sorted_list = chars_dict_sorted_list(character_count)
    alice_count = get_alice_count(text)
    hatter_count = get_madhatter_count(text)
    mad_count = get_mad_count(text)

    print(f"BookBot V2: Electric Boogaloo -- Initializing Analysis of {Book_path} --")
    print()
    print(f"BookBot has found a total of {word_count} words in {Book_path}.")
    print()
    print(f"BookBot has found that Main Character Alice was found a total of {alice_count} times in {Book_path}.")
    print()
    print(f"BookBot has found that everyones favorite Mad Hatter was found a total of {hatter_count} times in {Book_path}... isn't that surprising??")
    print()
    print(f"BookBot was suprised that Mad Hatter was not mentioned but the word Mad was found {mad_count} amount of times in {Book_path}.")
    print()
    print(f"-- Initializing Character Count of {Book_path} --")
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

def get_alice_count(text, case_sensitive=False):
    if not case_sensitive:
        text = text.lower()
    words = text.split()
    return words.count('alice' if not case_sensitive else 'Alice')

def get_mad_count(text, case_sensitive=False):
    if not case_sensitive:
        text = text.lower()
    words = text.split()
    return words.count('mad' if not case_sensitive else 'Mad')

def get_madhatter_count(text, case_sensitive=False):
    if not case_sensitive:
        text = text.lower()
        phrase = "mad hatter"
    else:
        phrase = "Mad Hatter"
    
    return text.count(phrase)    
    

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