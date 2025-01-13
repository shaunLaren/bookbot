def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    count = word_count(text)
    print(f"word count: {count}")

def get_book_text(book_path):
    with open(book_path) as f:
         return f.read()
    
def word_count(text):
    return len(text.split())


main()


