from stats import count_words, count_characters, sort_characters_by_count
import sys

def get_book_text(filepath):
  with open(filepath, 'r') as f:
    contents = f.read()
  return contents

def main():
  if len(sys.argv) != 2:
    print("Usage: python main.py <path_to_book>")
    sys.exit(1)
  else:
    filepath = sys.argv[1]

  contents = get_book_text(filepath)
  number_of_words = count_words(contents)
  characters = count_characters(contents)
  report_dict = sort_characters_by_count(characters)

  # Print report
  print("============ BOOKBOT ============")
  print(f"Analyzing book found at {filepath}...")
  print("----------- Word Count ----------")
  print(f"Found {number_of_words} total words")
  print("--------- Character Count -------")
  for char in report_dict:
    if char["character"].isalpha():
      print(f'{char["character"]}: {char["count"]}')

main()
