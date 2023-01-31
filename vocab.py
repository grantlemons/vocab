"""Main file that takes input and returns output for Spanish vocab work."""
from wrpy import WordReference
from def_obj import Definition

wr = WordReference('es', 'en')

input_words = []
selected_definitions = []

def take_input():
    """Gets input words by looping"""
    print('Enter empty word to exit')
    while True:
        current_word = input(f'Word {len(input_words) + 1:>2}: ')
        if current_word != '':
            input_words.append(current_word)
        else:
            break

def main():
    """Main functionality of app"""
    # populate input words array
    take_input()

    # specify which definition
    for word in input_words:
        translation = wr.translate(word)['translations'][0]['entries']
        definition = translation[0]
        # select specific definition if more than one exists
        if len(translation) > 1:
            # header w/ info
            print()
            print(f'=== {word} options ===')
            print(f'{"index":<8}{"part":<20}{"definition":<30}{"translations":<25}{"examples"}')
            print('---------------------------------------------------------------------------')
            # definitions w/ indexes
            for index, entry in enumerate(translation):
                translations = [to['meaning'] for to in entry['to_word']]
                examples = entry['to_example']
                print((f'{f"{index+1}:":<8}{entry["from_word"]["grammar"]:<20}'
                       f'{entry["context"]:<30}{str(translations):<25}{examples}'))
            definition = translation[int(input('Selection index: ')) - 1]
        selected_definitions.append(Definition(definition))

    # print objects
    print()
    print((f'{"":<2}{"Palabra":<25}{"":<2}|{"Categoría":^20}|{"Fuente":^10}'
           f'|{"Definición y diccionario":^40}|{"Contexto":^20}|'))
    print(('-----------------------------|--------------------|----------'
           '|----------------------------------------|--------------------|'))
    for definition in selected_definitions:
        print(definition)

if __name__ == "__main__":
    main()
