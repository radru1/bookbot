import sys
from stats import get_word_count, get_char_counts, get_sorted_char_counts

def main():
  if len(sys.argv) != 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)
  src = sys.argv[1]
  book_text = get_book_text(src)
  word_count = get_word_count(book_text)
  char_counts = get_char_counts(book_text)
  print_report(word_count, char_counts, src)

def get_book_text(path):
  with open(path) as f:
    book_text = f.read()
    return book_text

def print_report(word_count, char_counts, path):
  print("============ BOOKBOT ============")
  print(f"Analyzing book found at {path}")
  print("----------- Word Count ----------")
  print(f"Found {word_count} total words")
  print("--------- Character Count -------")

  for count in get_sorted_char_counts(char_counts):
    print(f"{count['char']}: {count['num']}")
main()