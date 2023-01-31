"""Main file that takes input and returns output for Spanish vocab work."""
from wrpy import WordReference

wr = WordReference('es', 'en')

input_words = []
selected_words = []

def yes_no_bool(string: str) -> bool:
    """Interprets Y/N input into boolean"""
    return string.lower() == 'y' or string.lower() == 'yes'

def take_input():
    """Gets input words by looping"""
    while yes_no_bool(input('Add word? [Y/N]: ')):
        current_word = input(f'Word {len(input_words) + 1}: ')
        input_words.append(current_word)

# populate input words array
take_input()

# specify which definition
for word in input_words:
    print()
    translation = wr.translate(word)['translations'][0]['entries']
    definition = translation[0]
    # select specific definition if more than one exists
    if len(translation) > 1:
        # header w/ info
        print(f'=== {word} options ===')
        print(f'{"index":<8}{"definition":<30}{"translations":<25}{"examples"}')
        print('---------------------------------------------------------------------')
        # definitions w/ indexes
        for index, entry in enumerate(translation):
            translations = [to['meaning'] for to in entry['to_word']]
            examples = entry['to_example']
            print(f'{f"{index+1}:":<8}{entry["context"]:<30}{str(translations):<25}{examples}')
        definition = translation[int(input('Selection index: ')) - 1]
    selected_words.append(definition)
