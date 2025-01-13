def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    count = word_count(text)
    letter_count = character_count(text)
    print(f"Number of each letter:\n{letter_count}")
    print(f"\nWord count: {count}")

def get_book_text(book_path):
    with open(book_path) as f:
         return f.read()
    
def word_count(text):
    return len(text.split())

def character_count(text):
    lowered_text = text.lower()
    count = {}
    for letter in lowered_text:
        count[letter] = count.get(letter, 0) + 1
    return count
    
        

    

main()


