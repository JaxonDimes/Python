languages = {
    'jen': 'c++',
    'sarah': 'python',
    'jane': '',
    'david': 'c#',
    'abby': ''
}
for person, language in languages.items():
    if language == '':
        print(f"Looks like {person.title()} has not taken the poll.")
    else:
        print(f"Thank You, {person.title()}. Your selected language was: {language.title()}.")
