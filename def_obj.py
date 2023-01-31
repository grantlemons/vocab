"""Class for representing definitions"""

class Definition:
    """Representation of a word definition"""
    def __init__(self, wr_definition):
        self.word = wr_definition['from_word']['source']
        self.part = wr_definition['from_word']['grammar']
        self.definition = wr_definition['context']
    def get_word(self):
        """Getter for word var"""
        return self.word
    def get_part(self):
        """Getter for part var"""
        return self.part
    def get_definition(self):
        """Getter for def var"""
        return self.definition + ' (WR)'
    def __str__(self):
        """String representation"""
        return f'{"":<2}{self.get_word():<25}{"":<2}|{self.get_part():^20}|{"":<10}|{"":<3}{self.get_definition():<35}{"":<2}|{"":^20}|'
