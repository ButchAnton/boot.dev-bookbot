def count_words(text):
  length = len(text.split())
  return length

def count_characters(text):
  lowercase_text = text.lower()
  char_count = {}
  for char in lowercase_text:
    if char in char_count:
        char_count[char] += 1
    else:
        char_count[char] = 1
  return char_count
  
def sort_characters_by_count(char_dict):
  char_list = [{"character": char, "count": count} for char, count in char_dict.items()]
  char_list.sort(key=lambda x: x["count"], reverse=True)
  return char_list
