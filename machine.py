import string
from rotor import Rotor


ALPHABET = string.ascii_uppercase

class Machine:
    def __init__(self, rotors, reflector):
        self.rotors = rotors
        self.reflector = reflector

    def reset(self):

        for rotor in self.rotors:
            rotor.reset()

    def encipher(self, text):
        return ''.join(self.encipher_character(x) for x in text)

    def encipher_character(self, x):
        x = x.upper()
        if x not in ALPHABET:
            return x

        contact_index = ALPHABET.index(x)
        for rotor in self.rotors:
            contact_index = rotor.get_char(contact_index)

        contact_index = self.reflector.translate(contact_index)

        for rotor in reversed(self.rotors):
            contact_index = rotor.get_char(contact_index, False)

        for rotor in self.rotors:
            if rotor.rotate() % Rotor.TURN_FREQUENCY != 0:
                break

        return ALPHABET[contact_index]
