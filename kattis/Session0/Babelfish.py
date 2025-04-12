""" 
We have input of translations: "word(English)"" ""word(otherlanguage)"\n 

- store the words in a dictionary 
- search for the key in the dictionary
"""


dictionary = {}

# Read dictionary entries until a blank line
while True:
    try:
        line = input().strip()
    except EOFError:
        # No more input at all
        break
    
    # Stop if we hit an empty line (end of dictionary section)
    if not line:
        break
    
    # Each line has: English_word Foreign_word
    english, foreign = line.split()
    dictionary[foreign] = english

# Now read the foreign words in the message until EOF
while True:
    try:
        foreign_word = input().strip()
    except EOFError:
        break
    
    # Print the translation if it exists; otherwise "eh"
    if foreign_word:
        print(dictionary.get(foreign_word, "eh"))
