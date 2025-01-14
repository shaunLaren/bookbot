def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    words = word_count(text)
    char_count = character_count(text)
    char_list = []
    
    for char, count in char_count.items():
        if char.isalpha():
            char_list.append({"char": char, "num": count})
    
    char_list.sort(key=sort_on, reverse=True)
    
    print(f"\n--- Begin report of {book_path} ---")
    
    print(f"{words} words found in the document")    
    
    for item in char_list:
        print(f"The '{item["char"]}' character was found {item["num"]} times")
    
    print("--- End report ---")
    

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
    
def sort_on(dict):
    return dict["num"]

main()


