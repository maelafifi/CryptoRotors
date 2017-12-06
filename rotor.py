import string

ALPHABET = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

class Rotor:
    TURN_FREQUENCY = len(ALPHABET)

    def __init__(self, rotor_alpha, offset=0):
        self.offset = offset
        self.rotations = 0
        self.alphabet = ALPHABET
        self.rotate(self.offset)

        self.forward_mappings = dict(zip(self.alphabet, rotor_alpha))
        self.reverse_mappings = dict(zip(rotor_alpha, self.alphabet))

    def rotate(self, rotation=1):
        self.alphabet = self.alphabet[rotation:] + self.alphabet[:rotation]
        self.rotations += rotation
        return self.rotations

    def encrypt_forward(self, character):
        return self.forward_mappings[character]

    def encrypt_backwards(self, character):
        return self.reverse_mappings[character]

    def get_char(self, index, right=True):
        x = self.alphabet[index]
        if right:
            x = self.encrypt_forward(x)
        else:
            x = self.encrypt_backwards(x)

        return self.alphabet.index(x)
