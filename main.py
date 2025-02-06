def main ():
    book_path = "books/frankenstein.txt"
    file_contents = read_book(book_path)
    num_words = count_words(file_contents)
    num_chars = count_chars(file_contents)
    print_report(book_path, num_words, num_chars)

def read_book(book_path):
    with open(book_path) as f:
        return f.read()

def count_words(text):
    return len(text.split())

def count_chars(text):
    chars = {}
    for char in text.lower():
        chars[char] = chars.get(char, 0) + 1
    return chars

def print_report(book_path, num_words, num_chars):
    print(f"--- Begin report of {book_path} ---")
    print(f"{num_words} words found in the document \n \n")

    valid_chars = "abcdefghijklmnopqrstuvwxyz"
    for char in valid_chars:
        if char in num_chars:
            print(f"The '{char}' character was found {num_chars[char]} times")

    print("--- End report ---")

main()
