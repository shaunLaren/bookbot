def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    count = word_count(text)
    char_count = character_count(text)
    print(f"\n--- Begin report of {book_path} ---")
    print(f"{count} words found in the document")
    print()
    

def get_book_text(book_path):
    with open(book_path) as f:
         return f.read()
    
def word_count(text):
    return len(text.split())

def character_count(text):
    lowered_text = text.lower()
    count = {}
    for char in lowered_text:
        count[char] = count.get(char, 0) + 1
    return count
    
if __name__ == "__main__":
    main()


