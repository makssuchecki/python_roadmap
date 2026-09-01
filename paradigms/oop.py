# Object-oriented programming considers basic entities as objects whose instance
# can contain both data and the corresponding methods to modify that data

class StringOps:
    def __init__(self, characters):
        self.characters = characters
    def stringify(self):
        self.string = "".join(self.characters)

sample_characters = ['p','y','t','h','o','n']
sample_string = StringOps(sample_characters)
sample_string.stringify()
sample_string.string