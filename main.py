import sys
from stats import count_words
from stats import count_char
from stats import sort_dict

def get_book_text(file_path):
    # opens and reads a txt file and returns it as a string

    with open(file_path) as f:
        text = f.read()
        return text

def main():
    if len(sys.argv) != 2:
        print('Usage: python3 main.py <path_to_book>')
        sys.exit(1)
    print("============ BOOKBOT ============\nAnalyzing book found at books/frankenstein.txt...\n----------- Word Count ----------")
    print(f"Found {count_words(get_book_text(sys.argv[1]))} total words\n--------- Character Count -------")
    char = count_char(get_book_text(sys.argv[1]))
    sorted_char = sort_dict(char)
    for d in sorted_char:
        if d["char"].isalpha() == True:
            print(f'{d["char"]}: {d["num"]}')
    print("============= END ===============")


main()