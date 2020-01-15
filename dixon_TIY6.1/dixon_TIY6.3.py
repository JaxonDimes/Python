python_glossary = {
    'print()': 'prints commands without format in the console',
    'BLANK = []': 'creates a list to hold items and BLANK can vary',
    'for BLANK in BLANK: ': 'a FOR loop that loops through a list or dictionary for each value associated',
    'tuple': 'a static list that can only be rewritten, instead of being able to change its values',
    'language': 'the programming language that the programmer uses for their programs'}
for item in python_glossary:
    print(f"{item.title()}")
    print(f"{python_glossary.get(item)}\n")
