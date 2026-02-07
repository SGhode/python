import re
text = "The quick brown fox jumps over the lazy dog."

# Search for a pattern 
# match  = re.search("brown", text)
# print(match)  # <re.Match object; span=(10, 15), match='brown'>
# if match:
#     print("Match found!")
#     print("Start index:", match.start())
#     print("End index:", match.end())

# FInd all occurrences of a pattern
# matches = re.findall("the", text, re.IGNORECASE) # Case insensitive search
# print("Matches:", matches)  # ['The', 'the']


new_text = re.sub("fox", "cat", text)
print("New text:", new_text)














