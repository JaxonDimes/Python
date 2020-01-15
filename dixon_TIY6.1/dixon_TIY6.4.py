python_glossary = {
    'print()': 'prints commands without format in the console',
    'BLANK = []': 'creates a list to hold items and BLANK can vary',
    'for BLANK in BLANK: ': 'a FOR loop that loops through a list or dictionary for each value associated',
    'tuple': 'a static list that can only be rewritten, instead of being able to change its values',
    'language': 'the programming language that the programmer uses for their programs',
    'ASCII': 'all letters and symbols representing each numerous amounts of binary for each',
    'Boolean': 'an expression used to verify if something is true or false',
    'get()': 'a command that gets all points in a list or dictionary',
    'If statements': 'statements that follow boolean expressions to trigger code attached',
    'variables': 'a key word or symbol that you use in basic programming to represent a value'}
for item, value in python_glossary.items():
    print(f"\t{item.title()}")
    print(f"{value.title()}\n")
