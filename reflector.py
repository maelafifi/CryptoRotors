import string

ALPHABET = string.ascii_uppercase

class Reflector:
	def __init__(self, mappings):
		self.mappings = dict(zip(ALPHABET, mappings))

		for x, y in self.mappings.items():
		    if x != self.mappings[y]:
		        raise ValueError('Mapping for {0} and {1} is invalid'.format(x, y))

	def translate(self, contact_index):
		x = self.mappings[ALPHABET[contact_index]]
		return ALPHABET.index(x)
