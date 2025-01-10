def main ():
    frankenstein = get_text("books/frankenstein.txt")
    f_word_count = get_word_count(frankenstein)
    f_char_count = get_char_count(frankenstein)
    print("--- Begin report of books/frankenstein.txt ---")
    print(f"{f_word_count} words found in the document")


    for char in f_char_count:
        print(f"The '{char}' character was found: {f_char_count[char]} times")
    print("--- End report ---")
def get_text(path):
    with open(path) as t:
        return t.read()
    
def get_word_count(text):
    return len(text.split())

def get_char_count(text):
    char_count = {}
    chars = " ".join(text.lower()).split()
    for char in chars:
        if char not in char_count:
            char_count[char] = 1
        else:
            char_count[char] += 1
    return char_count
    

main()