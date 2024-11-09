def main():
    with open("books/Alice_in_wonderland.txt") as f:
        file_contents = f.read()
        print(file_contents)

main()