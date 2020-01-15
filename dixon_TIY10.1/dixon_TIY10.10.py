def countWord(filename, word):
    try:
        with open(filename, encoding='utf-8') as f:
            contents = f.read()
    except FileNotFoundError:
        print(f"Apologies, {filename} does not exist.")
    else:
        occurance = contents.lower().count(word)
        words = contents.split()
        num_words = len(words)
        print(f"The file {filename} has about {num_words} words.")
        print(f"The word '{word}' occurs {occurance} times.")


filename = 'Raven.txt'
ask = input("Ask any word that may be in the Raven story.\n::")
countWord(filename, ask)

countWord(filename, 'the ')
countWord(filename, 'The')
countWord(filename, 'the')
