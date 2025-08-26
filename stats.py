
def get_word_count(text):
  words = text.split()
  return len(words)

def get_char_counts(text):
  char_dictionary = {}
  for char in text:
    char = char.lower()
    if char not in char_dictionary:
      char_dictionary[char] = 0
    char_dictionary[char] += 1
  return char_dictionary

def sort_by(item):
  return item['num']

def get_sorted_char_counts(char_counts):
  char_counts_list = []
  for char, count in char_counts.items():
    char_counts_list.append({'char': char, 'num': count})
  char_counts_list.sort(key=sort_by, reverse=True)
  return char_counts_list
